from __future__ import annotations

import argparse
import json
import os
import signal
import subprocess
import sys
import time
import webbrowser
from http.client import HTTPConnection
from urllib.parse import quote_plus
from pathlib import Path
from typing import Any, Dict, Optional

from . import (
    ProjectPaths,
    SessionManager,
    build_slot_index,
    make_session_id,
    ensure_project_config,
    register_project,
    discover_project_root,
)
from .config import CONFIG_DIR_NAME, CONFIG_FILENAME, ProjectConfig
from .gallery import serve_gallery
from .generator import GenerationResult, build_generator
from .defaults import DEFAULT_GENERATOR, DEFAULT_PROVIDER, available_models, default_model_for_provider
from .models import EffectiveParameters, SessionRequest
from .storage import InvalidPathError, list_manifests_for_slot


def _env_flag(name: str) -> bool:
    value = os.environ.get(name)
    if value is None:
        return False
    return value.strip().lower() in {"1", "true", "yes", "on"}


GALLERY_HOST = os.environ.get("IMAGEMCP_GALLERY_HOST", "localhost")
GALLERY_PORT = int(os.environ.get("IMAGEMCP_GALLERY_PORT", "8765"))
GALLERY_LAUNCH_TIMEOUT = float(os.environ.get("IMAGEMCP_GALLERY_START_TIMEOUT", "5"))
GALLERY_POLL_INTERVAL = float(os.environ.get("IMAGEMCP_GALLERY_POLL_INTERVAL", "0.2"))
GALLERY_ALWAYS_RESTART = _env_flag("IMAGEMCP_GALLERY_ALWAYS_RESTART")


def _project_config_path(project_root: Path) -> Path:
    return project_root / CONFIG_DIR_NAME / CONFIG_FILENAME


def _resolve_project_root(start: Path) -> Path:
    discovered = discover_project_root(start)
    if discovered:
        return discovered
    return start.resolve()


def _prepare_project(
    args: argparse.Namespace,
    *,
    allow_create: bool = True,
    project_name: Optional[str] = None,
    target_override: Optional[str] = None,
) -> tuple[ProjectConfig, ProjectPaths]:
    start_root = Path(getattr(args, "project_root", ".") or ".").resolve()
    project_root = _resolve_project_root(start_root)
    config_path = _project_config_path(project_root)
    if not config_path.exists() and not allow_create:
        raise RuntimeError(
            f"Project config not found at {config_path}. Run 'imgen init' or specify --target-root."
        )
    override = target_override or getattr(args, "target_root", None)
    config = ensure_project_config(project_root, target_root=override, project_name=project_name)
    register_project(config)
    target_root = override or config.target_root
    paths = ProjectPaths.create(config.project_root, Path(target_root))
    paths.ensure_directories()
    _load_env_file(config.project_root)
    return config, paths


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="imgen", description="Image slot manager CLI")
    parser.add_argument(
        "--project-root",
        default=".",
        help="Project root directory (default: current directory)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    gen_parser = subparsers.add_parser("gen", help="Generate new variants for a slot")
    gen_parser.add_argument("--slot", required=True, help="Slot identifier (slug)")
    gen_parser.add_argument("--target-root", help="Override target asset root (default from project config)")
    gen_parser.add_argument("--prompt", help="Direct prompt string")
    gen_parser.add_argument(
        "--prompt-file",
        help="Path to prompt JSON input (use '-' for stdin)",
    )
    gen_parser.add_argument("--request-text", help="Human-readable request text")
    gen_parser.add_argument("--n", type=int, help="Number of variants to generate (default: 3)")
    size_group = gen_parser.add_mutually_exclusive_group()
    size_group.add_argument("--size", help="Image size (e.g. 1024x1024)")
    size_group.add_argument("--aspect-ratio", help="Aspect ratio (e.g. 16:9)")
    gen_parser.add_argument("--seed", type=int)
    gen_parser.add_argument("--provider", help="Provider id (e.g. openai)")
    gen_parser.add_argument("--model", help="Model id (e.g. dall-e-3)")
    gen_parser.add_argument("--session-hint", help="Hint to include in session id")
    gen_parser.add_argument(
        "--generator",
        default=None,
        help=(
            "Generator backend (default: openrouter; automatically switches to 'mock' when the provider is 'mock')"
        ),
    )
    gen_parser.add_argument(
        "--json",
        action="store_true",
        help="Emit JSON result to stdout",
    )
    gen_parser.add_argument(
        "--open-gallery",
        action="store_true",
        help="Include gallery URL in result",
    )
    gen_parser.add_argument(
        "--restart-gallery",
        action="store_true",
        help="Force-restart the gallery server for this run (also settable via IMAGEMCP_GALLERY_ALWAYS_RESTART)",
    )
    gen_parser.set_defaults(func=cmd_generate)

    init_parser = subparsers.add_parser("init", help="Initialize project configuration")
    init_parser.add_argument("--project-root", default=".")
    init_parser.add_argument("--target-root", help="Target asset root (default: public/img)")
    init_parser.add_argument("--project-name", help="Human-friendly project name")
    init_parser.add_argument("--json", action="store_true")
    init_parser.set_defaults(func=cmd_init)

    select_parser = subparsers.add_parser("select", help="Promote a specific variant")
    select_parser.add_argument("--target-root")
    select_parser.add_argument("--slot", help="Slot id (optional if session uniquely identifies)")
    select_parser.add_argument("--session", required=True, help="Session id")
    select_parser.add_argument("--index", required=True, type=int, help="Variant index")
    select_parser.add_argument("--json", action="store_true")
    select_parser.set_defaults(func=cmd_select)

    slots_parser = subparsers.add_parser("slots", help="Slot operations")
    slots_sub = slots_parser.add_subparsers(dest="slots_command", required=True)
    slots_list_parser = slots_sub.add_parser("list", help="List slots")
    slots_list_parser.add_argument("--target-root")
    slots_list_parser.add_argument("--json", action="store_true")
    slots_list_parser.set_defaults(func=cmd_slots_list)

    sessions_parser = subparsers.add_parser("sessions", help="Session operations")
    sessions_sub = sessions_parser.add_subparsers(dest="sessions_command", required=True)
    sessions_list_parser = sessions_sub.add_parser("list", help="List sessions for a slot")
    sessions_list_parser.add_argument("--target-root")
    sessions_list_parser.add_argument("--slot", required=True)
    sessions_list_parser.add_argument("--json", action="store_true")
    sessions_list_parser.set_defaults(func=cmd_sessions_list)

    session_info_parser = sessions_sub.add_parser("info", help="Show session manifest contents")
    session_info_parser.add_argument("--target-root")
    session_info_parser.add_argument("--slot", required=True)
    session_info_parser.add_argument("--session", required=True)
    session_info_parser.add_argument("--json", action="store_true")
    session_info_parser.set_defaults(func=cmd_session_info)

    gallery_parser = subparsers.add_parser("gallery", help="Gallery server")
    gallery_sub = gallery_parser.add_subparsers(dest="gallery_command", required=True)
    gallery_serve_parser = gallery_sub.add_parser("serve", help="Run the local gallery web server")
    gallery_serve_parser.add_argument("--target-root")
    gallery_serve_parser.add_argument("--host", default="127.0.0.1")
    gallery_serve_parser.add_argument("--port", type=int, default=8765)
    gallery_serve_parser.add_argument("--open-browser", action="store_true")
    gallery_serve_parser.set_defaults(func=cmd_gallery_serve)

    gallery_ensure_parser = gallery_sub.add_parser("ensure", help="Ensure the gallery server is running in the background")
    gallery_ensure_parser.add_argument("--target-root")
    gallery_ensure_parser.add_argument("--host", default=GALLERY_HOST)
    gallery_ensure_parser.add_argument("--port", type=int, default=GALLERY_PORT)
    gallery_ensure_parser.add_argument("--restart", action="store_true", help="Force a restart even if a server is detected")
    gallery_ensure_parser.set_defaults(func=cmd_gallery_ensure)

    gallery_stop_parser = gallery_sub.add_parser("stop", help="Terminate the background gallery server if it is running")
    gallery_stop_parser.add_argument("--target-root")
    gallery_stop_parser.add_argument("--host", default=GALLERY_HOST)
    gallery_stop_parser.add_argument("--port", type=int, default=GALLERY_PORT)
    gallery_stop_parser.set_defaults(func=cmd_gallery_stop)

    models_parser = subparsers.add_parser("models", help="List supported providers and models")
    models_parser.add_argument("--provider", help="Filter results to a provider id")
    models_parser.set_defaults(func=cmd_models)

    return parser


def _probe_gallery(host: str, port: int, timeout: float = 0.5) -> bool:
    """Return True if the gallery server responds successfully."""
    conn: Optional[HTTPConnection] = None
    try:
        conn = HTTPConnection(host, port, timeout=timeout)
        conn.request("GET", "/")
        response = conn.getresponse()
        response.read()
        return 200 <= response.status < 500
    except OSError:
        return False
    finally:
        if conn is not None:
            try:
                conn.close()
            except OSError:
                pass


def _gallery_pid_path(paths: ProjectPaths) -> Path:
    return paths.target_root / ".imagemcp-gallery.pid"


def _global_gallery_state_path() -> Path:
    return Path.home() / CONFIG_DIR_NAME / "gallery.json"


def _load_env_file(project_root: Path) -> None:
    env_path = project_root / ".env"
    try:
        data = env_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return
    except OSError as exc:
        print(f"[imagemcp] Warning: Unable to read {env_path}: {exc}", file=sys.stderr)
        return
    for raw_line in data.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export "):].strip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def _read_gallery_pid(paths: ProjectPaths) -> Optional[int]:
    try:
        data = _gallery_pid_path(paths).read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        return None
    if not data:
        return None
    try:
        return int(data)
    except ValueError:
        return None


def _write_gallery_pid(paths: ProjectPaths, pid: int) -> None:
    path = _gallery_pid_path(paths)
    path.write_text(str(pid), encoding="utf-8")


def _clear_gallery_pid(paths: ProjectPaths) -> None:
    path = _gallery_pid_path(paths)
    try:
        path.unlink()
    except FileNotFoundError:
        pass


def _read_global_gallery_state() -> Optional[Dict[str, str]]:
    state_path = _global_gallery_state_path()
    try:
        return json.loads(state_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def _write_global_gallery_state(paths: ProjectPaths, pid: int) -> None:
    state_path = _global_gallery_state_path()
    payload = {
        "pid": str(pid),
        "projectRoot": str(paths.project_root),
        "targetRoot": str(paths.target_root),
    }
    try:
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(json.dumps(payload), encoding="utf-8")
    except PermissionError:
        pass


def _clear_global_gallery_state() -> None:
    state_path = _global_gallery_state_path()
    try:
        state_path.unlink()
    except FileNotFoundError:
        pass
    except PermissionError:
        pass


def _launch_gallery_background(config: ProjectConfig, paths: ProjectPaths, host: str, port: int) -> subprocess.Popen[bytes]:
    try:
        target_root = paths.target_root.relative_to(paths.project_root).as_posix()
    except ValueError:
        target_root = str(paths.target_root)
    project_root = str(paths.project_root)
    cmd = [
        sys.executable,
        "-m",
        "imagemcp.cli",
        "--project-root",
        project_root,
        "gallery",
        "serve",
        "--target-root",
        target_root,
        "--host",
        host,
        "--port",
        str(port),
    ]
    process = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    _write_gallery_pid(paths, process.pid)
    _write_global_gallery_state(paths, process.pid)
    return process


def _terminate_existing_gallery(paths: ProjectPaths, host: str, port: int) -> None:
    pid = _read_gallery_pid(paths)
    state = _read_global_gallery_state()
    candidate_pids = []
    if pid is not None:
        candidate_pids.append(pid)
    if state and state.get("pid"):
        try:
            candidate_pids.append(int(state["pid"]))
        except ValueError:
            pass
    if not candidate_pids:
        return
    for candidate in candidate_pids:
        try:
            os.kill(candidate, signal.SIGTERM)
        except ProcessLookupError:
            continue
        except PermissionError:
            print(
                f"[imagemcp] Warning: Unable to terminate existing gallery process {candidate} due to permissions.",
                file=sys.stderr,
            )
            continue
    deadline = time.time() + GALLERY_LAUNCH_TIMEOUT
    while time.time() < deadline:
        if not _probe_gallery(host, port):
            break
        time.sleep(GALLERY_POLL_INTERVAL)
    _clear_gallery_pid(paths)
    _clear_global_gallery_state()


def _ensure_gallery_available(
    config: ProjectConfig,
    paths: ProjectPaths,
    host: str,
    port: int,
    force_restart: bool = False,
) -> None:
    state = _read_global_gallery_state()
    if state:
        if state.get("projectRoot") != str(paths.project_root) or state.get("targetRoot") != str(paths.target_root):
            force_restart = True
    if force_restart:
        _terminate_existing_gallery(paths, host, port)
    if _probe_gallery(host, port):
        _register_project_with_gallery(config, host, port)
        return
    print(
        f"[imagemcp] No gallery server detected at http://{host}:{port}/. Starting one in the background...",
        file=sys.stderr,
    )
    try:
        process = _launch_gallery_background(config, paths, host, port)
    except OSError as exc:
        print(f"[imagemcp] Warning: Failed to launch gallery server: {exc}", file=sys.stderr)
        return
    deadline = time.time() + GALLERY_LAUNCH_TIMEOUT
    while time.time() < deadline:
        if _probe_gallery(host, port):
            print(
                f"[imagemcp] Gallery server is now available at http://{host}:{port}/ (pid {process.pid}).",
                file=sys.stderr,
            )
            return
        time.sleep(GALLERY_POLL_INTERVAL)
    print(
        f"[imagemcp] Warning: Gallery server did not become ready at http://{host}:{port}/."
        " It may still be starting; check logs if the endpoint remains unreachable.",
        file=sys.stderr,
    )


def _register_project_with_gallery(config: ProjectConfig, host: str, port: int) -> None:
    payload = {
        "projectId": config.project_id,
        "projectName": config.project_name,
        "projectRoot": str(config.project_root),
        "targetRoot": config.target_root,
    }
    try:
        conn = HTTPConnection(host, port, timeout=1.5)
        conn.request(
            "POST",
            "/api/register",
            body=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        conn.getresponse().read()
    except Exception:
        pass
    finally:
        try:
            conn.close()
        except Exception:
            pass


def cmd_generate(args: argparse.Namespace) -> int:
    try:
        config, paths = _prepare_project(args)
    except InvalidPathError as exc:
        return _fail(str(exc))
    except RuntimeError as exc:
        return _fail(str(exc))
    manager = SessionManager(paths)

    session_id = make_session_id(args.session_hint)
    ctx = manager.create_context(args.slot, session_id)
    manager.ensure_session_dir(ctx)

    payload = _load_prompt_payload(args.prompt, args.prompt_file)
    if not payload.prompt:
        return _fail("A prompt is required via --prompt or --prompt-file")

    count = args.n if args.n is not None else payload.count or 3
    if count <= 0:
        return _fail("--n must be at least 1")

    size = args.size or payload.size
    aspect_ratio = args.aspect_ratio or payload.aspect_ratio
    seed = args.seed if args.seed is not None else payload.seed
    provider = args.provider or payload.provider or DEFAULT_PROVIDER
    model = args.model or payload.model or default_model_for_provider(provider)
    generator_name = (
        (args.generator if args.generator else None)
        or payload.generator
        or ("mock" if provider == "mock" else DEFAULT_GENERATOR)
    )

    request_text = args.request_text or payload.request_text or f"Generate {count} variants for {args.slot}"

    try:
        generator = build_generator(ctx.session_dir, generator_name)
    except Exception as exc:  # pragma: no cover - depends on generator backend
        return _handle_generator_exception(exc, config)

    try:
        generation: GenerationResult = generator.generate(
            payload.prompt,
            count,
            size=size,
            aspect_ratio=aspect_ratio,
            seed=seed,
            provider=provider,
            model=model,
            provider_options=payload.provider_options,
        )
    except Exception as exc:  # pragma: no cover - depends on generator backend
        return _handle_generator_exception(exc, config)

    request = SessionRequest(request_text=request_text, created_by="cli")
    effective = EffectiveParameters(
        prompt=payload.prompt,
        n=count,
        size=size,
        aspect_ratio=aspect_ratio,
        seed=seed,
        provider=provider,
        model=model,
        generator=generator_name,
        provider_options=payload.provider_options,
    )

    manifest = manager.build_manifest(
        ctx,
        request=request,
        effective=effective,
        image_artifacts=generation.images,
        warnings=generation.warnings,
        auto_selected_index=0,
    )
    manager.promote_variant(ctx, manifest, 0)

    force_restart_gallery = args.restart_gallery or GALLERY_ALWAYS_RESTART
    _ensure_gallery_available(config, paths, GALLERY_HOST, GALLERY_PORT, force_restart_gallery)

    gallery_url = _default_gallery_url(config.project_id, args.slot)
    result = {
        "ok": True,
        "slot": args.slot,
        "sessionId": session_id,
        "selectedIndex": manifest.selected_index,
        "selectedPath": manifest.selected_path,
        "sessionDir": str(ctx.session_dir.relative_to(paths.project_root)),
        "warnings": manifest.warnings,
        "galleryUrl": gallery_url,
        "projectId": config.project_id,
        "projectName": config.project_name,
        "targetRoot": config.target_root,
        "generator": generator_name,
    }
    if args.open_gallery:
        webbrowser.open(gallery_url, new=2)

    if args.json:
        _print_json(result)
    else:
        _print_human_result(result)
    return 0


def cmd_init(args: argparse.Namespace) -> int:
    project_root = Path(args.project_root or ".").resolve()
    target_root = args.target_root
    project_name = args.project_name
    config = ensure_project_config(project_root, target_root=target_root, project_name=project_name)
    register_project(config)
    payload = {
        "ok": True,
        "projectId": config.project_id,
        "projectName": config.project_name,
        "projectRoot": str(config.project_root),
        "targetRoot": config.target_root,
        "configPath": str(config.config_path()),
    }
    if args.json:
        _print_json(payload)
    else:
        print(f"Project '{config.project_name}' initialized at {payload['configPath']}")
        print(f"Target root: {config.target_root}")
        print(f"Project id: {config.project_id}")
    return 0


def cmd_select(args: argparse.Namespace) -> int:
    try:
        config, paths = _prepare_project(args)
    except (InvalidPathError, RuntimeError) as exc:
        return _fail(str(exc))
    manager = SessionManager(paths)
    try:
        slot_id = args.slot or _infer_slot(paths, args.session)
    except LookupError as exc:
        return _fail(str(exc))
    ctx = manager.create_context(slot_id, args.session)
    if not ctx.manifest_path.exists():
        return _fail("Session manifest not found")
    manifest = manager.read_manifest(ctx)
    if args.index < 0 or args.index >= len(manifest.images):
        return _fail("Variant index out of range")
    manager.promote_variant(ctx, manifest, args.index)
    result = {
        "ok": True,
        "slot": ctx.slot,
        "sessionId": ctx.session_id,
        "selectedIndex": manifest.selected_index,
        "selectedPath": manifest.selected_path,
        "projectId": config.project_id,
        "projectName": config.project_name,
    }
    if args.json:
        _print_json(result)
    else:
        _print_human_result(result)
    return 0


def cmd_slots_list(args: argparse.Namespace) -> int:
    try:
        config, paths = _prepare_project(args, allow_create=False)
    except (InvalidPathError, RuntimeError) as exc:
        return _fail(str(exc))
    summaries = build_slot_index(paths)
    if args.json:
        payload = {
            "projectId": config.project_id,
            "projectName": config.project_name,
            "targetRoot": config.target_root,
            "slots": {
                slot: {
                    "sessionCount": summary.session_count,
                    "selectedPath": summary.selected_path,
                    "selectedIndex": summary.selected_index,
                    "lastUpdated": summary.last_updated.isoformat() if summary.last_updated else None,
                    "warnings": summary.warnings,
                }
                for slot, summary in summaries.items()
            },
        }
        _print_json(payload)
    else:
        if not summaries:
            print("No slots found.")
            return 0
        for slot, summary in summaries.items():
            last_updated = summary.last_updated.isoformat() if summary.last_updated else "-"
            print(
                f"{slot}: {summary.selected_path or 'n/a'} (#{summary.selected_index if summary.selected_index is not None else '-'})"
                f", sessions={summary.session_count}, updated={last_updated}"
            )
    return 0


def cmd_sessions_list(args: argparse.Namespace) -> int:
    try:
        config, paths = _prepare_project(args, allow_create=False)
    except (InvalidPathError, RuntimeError) as exc:
        return _fail(str(exc))
    manifests = list_manifests_for_slot(paths, args.slot)
    manifests.sort(key=lambda m: m.created_at)
    if args.json:
        payload = {
            "projectId": config.project_id,
            "projectName": config.project_name,
            "targetRoot": config.target_root,
            "slot": args.slot,
            "sessions": [
                {
                    "sessionId": manifest.session_id,
                    "selectedIndex": manifest.selected_index,
                    "selectedPath": manifest.selected_path,
                    "createdAt": manifest.created_at.isoformat(),
                    "completedAt": manifest.completed_at.isoformat(),
                    "warnings": manifest.warnings,
                }
                for manifest in manifests
            ],
        }
        _print_json(payload)
    else:
        if not manifests:
            print("No sessions found for slot.")
            return 0
        for manifest in manifests:
            print(f"{manifest.session_id}: selected #{manifest.selected_index} -> {manifest.selected_path}")
    return 0


def cmd_session_info(args: argparse.Namespace) -> int:
    try:
        config, paths = _prepare_project(args, allow_create=False)
    except (InvalidPathError, RuntimeError) as exc:
        return _fail(str(exc))
    manager = SessionManager(paths)
    ctx = manager.create_context(args.slot, args.session)
    if not ctx.manifest_path.exists():
        return _fail("Session manifest not found")
    manifest = manager.read_manifest(ctx)
    if args.json:
        payload = manifest.to_dict()
        payload["projectId"] = config.project_id
        payload["projectName"] = config.project_name
        _print_json(payload)
    else:
        print(json.dumps(manifest.to_dict(), indent=2))
    return 0


def cmd_gallery_serve(args: argparse.Namespace) -> int:
    try:
        config, paths = _prepare_project(
            args,
            allow_create=True,
            project_name=getattr(args, "project_name", None),
            target_override=args.target_root,
        )
    except (InvalidPathError, RuntimeError) as exc:
        return _fail(str(exc))
    url = f"http://{args.host}:{args.port}/"
    if args.open_browser:
        webbrowser.open(url, new=2)
    try:
        serve_gallery(config, paths, host=args.host, port=args.port)
    except OSError as exc:
        return _fail(f"Gallery failed to start: {exc}")
    return 0


def cmd_gallery_ensure(args: argparse.Namespace) -> int:
    try:
        config, paths = _prepare_project(args)
    except (InvalidPathError, RuntimeError) as exc:
        return _fail(str(exc))
    host = args.host or GALLERY_HOST
    port = args.port or GALLERY_PORT
    force_restart = args.restart or GALLERY_ALWAYS_RESTART
    _ensure_gallery_available(config, paths, host, port, force_restart)
    return 0


def cmd_gallery_stop(args: argparse.Namespace) -> int:
    try:
        _, paths = _prepare_project(args, allow_create=False)
    except (InvalidPathError, RuntimeError) as exc:
        return _fail(str(exc))
    host = args.host or GALLERY_HOST
    port = args.port or GALLERY_PORT
    _terminate_existing_gallery(paths, host, port)
    return 0


def cmd_models(args: argparse.Namespace) -> int:
    models = available_models()
    if args.provider:
        provider = args.provider.strip().lower()
        options = models.get(provider)
        if not options:
            known = ", ".join(sorted(models)) or "(none)"
            return _fail(f"Unknown provider '{provider}'. Known providers: {known}")
        print(f"Provider: {provider}")
        for model in options:
            print(f"  - {model}")
        return 0
    for provider in sorted(models):
        print(f"Provider: {provider}")
        for model in models[provider]:
            print(f"  - {model}")
    return 0


def _load_prompt_payload(prompt: Optional[str], prompt_file: Optional[str]) -> "PromptPayload":
    prompt_text = prompt
    request_text: Optional[str] = None
    provider_options: Dict[str, Any] = {}
    provider: Optional[str] = None
    model: Optional[str] = None
    size_override: Optional[str] = None
    aspect_override: Optional[str] = None
    seed_override: Optional[int] = None
    count_override: Optional[int] = None
    generator_override: Optional[str] = None

    if prompt_file:
        raw = _read_input(prompt_file)
        try:
            parsed = json.loads(raw)
            if isinstance(parsed, dict):
                prompt_text = prompt_text or parsed.get("prompt")
                request_text = parsed.get("requestText")
                provider_options_data = parsed.get("providerOptions", {}) or {}
                if isinstance(provider_options_data, dict):
                    provider_options = provider_options_data
                prompt_text = prompt_text or parsed.get("text")
                provider = parsed.get("provider") or provider
                model = parsed.get("model") or model
                generator_override = parsed.get("generator") or generator_override
                size_override = parsed.get("size") or size_override
                aspect_override = parsed.get("aspectRatio") or aspect_override
                seed_value = parsed.get("seed")
                if isinstance(seed_value, int):
                    seed_override = seed_value
                count_value = parsed.get("n") or parsed.get("count")
                if isinstance(count_value, int):
                    count_override = count_value
            elif isinstance(parsed, str):
                prompt_text = prompt_text or parsed
        except json.JSONDecodeError:
            prompt_text = prompt_text or raw

    return PromptPayload(
        prompt=prompt_text or "",
        request_text=request_text,
        provider_options=provider_options,
        provider=provider,
        model=model,
        generator=generator_override,
        size=size_override,
        aspect_ratio=aspect_override,
        seed=seed_override,
        count=count_override,
    )


def _read_input(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


def _infer_slot(paths: ProjectPaths, session_id: str) -> str:
    if not paths.sessions_root.exists():
        raise LookupError("No session data available")
    matches = []
    for directory in paths.sessions_root.iterdir():
        if not directory.is_dir():
            continue
        try:
            slug, rest = directory.name.split("_", 1)
        except ValueError:
            continue
        if rest == session_id:
            matches.append(slug)
    if not matches:
        raise LookupError("Session id not found")
    if len(matches) > 1:
        raise LookupError("Multiple slots share this session id; specify --slot")
    return matches[0]


def _default_gallery_url(project_id: str, slot: str) -> str:
    project_param = quote_plus(project_id)
    slot_param = quote_plus(slot)
    return f"http://{GALLERY_HOST}:{GALLERY_PORT}/?project={project_param}&slot={slot_param}"


def _print_json(payload: Any) -> None:
    json.dump(payload, sys.stdout)
    sys.stdout.write("\n")


def _print_human_result(payload: Dict[str, Any]) -> None:
    if payload.get("ok"):
        slot = payload.get("slot")
        path = payload.get("selectedPath")
        print(f"Slot '{slot}' promoted {path}")
        if payload.get("warnings"):
            print("Warnings:")
            for warning in payload["warnings"]:
                print(f"  - {warning}")
        if payload.get("galleryUrl"):
            print(f"Gallery: {payload['galleryUrl']}")
    else:
        print(payload)


def _fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 1


def _handle_generator_exception(exc: Exception, config: ProjectConfig) -> int:
    message = str(exc)
    env_hint = config.project_root / ".env"
    key_notice = "OpenRouter API key is missing"
    if key_notice in message:
        guidance = (
            "OpenRouter API key is missing. Set OPENROUTER_API_KEY in your environment.\n"
            f"Add a line like OPENROUTER_API_KEY=sk-... to {env_hint} and rerun the command; no extra 'source .env' step is required because the CLI reloads the file automatically.\n"
            "If the key is unavailable, ask the user to provide a valid OpenRouter API token before continuing."
        )
        return _fail(guidance)
    if "not a valid model ID" in message:
        guidance = (
            "OpenRouter rejected the requested model. Use the default `google/gemini-2.5-flash-image-preview` or consult "
            "resource setup://imgen-parameters. Run `imgen models` to list supported options."
        )
        return _fail(guidance)
    return _fail(f"Generator error ({exc.__class__.__name__}): {message}")


class PromptPayload:
    def __init__(
        self,
        *,
        prompt: str,
        request_text: Optional[str],
        provider_options: Dict[str, Any],
        provider: Optional[str],
        model: Optional[str],
        generator: Optional[str],
        size: Optional[str],
        aspect_ratio: Optional[str],
        seed: Optional[int],
        count: Optional[int],
    ) -> None:
        self.prompt = prompt
        self.request_text = request_text
        self.provider_options = provider_options
        self.provider = provider
        self.model = model
        self.generator = generator
        self.size = size
        self.aspect_ratio = aspect_ratio
        self.seed = seed
        self.count = count


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    return args.func(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
