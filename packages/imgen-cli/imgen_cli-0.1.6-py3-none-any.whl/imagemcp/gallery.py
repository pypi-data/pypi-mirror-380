from __future__ import annotations

import http.server
import json
import mimetypes
import socketserver
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional
from urllib.parse import parse_qs, quote, unquote, urlparse

from . import SessionManager, build_slot_index
from .config import (
    ProjectConfig,
    ensure_project_config,
    get_project_index_path,
    load_project_index,
    register_project,
)
from .models import format_ts
from .storage import InvalidPathError, ProjectPaths, list_manifests_for_slot, load_manifest


@dataclass
class ProjectInfo:
    project_id: str
    project_name: str
    project_root: Path
    target_root: str


@dataclass
class ProjectContext:
    info: ProjectInfo
    paths: ProjectPaths
    manager: SessionManager


class ProjectRegistry:
    def __init__(self, default_config: ProjectConfig, default_paths: ProjectPaths) -> None:
        self._default_id = default_config.project_id
        self._contexts: Dict[str, ProjectContext] = {}
        self._index_path = get_project_index_path()
        self.register_config(default_config, default_paths)

    def register_config(
        self,
        config: ProjectConfig,
        paths: Optional[ProjectPaths] = None,
    ) -> None:
        info = ProjectInfo(
            project_id=config.project_id,
            project_name=config.project_name,
            project_root=config.project_root,
            target_root=config.target_root,
        )
        if paths is None:
            paths = ProjectPaths.create(config.project_root, Path(config.target_root))
            paths.ensure_directories()
        context = ProjectContext(info=info, paths=paths, manager=SessionManager(paths))
        self._contexts[info.project_id] = context

    def list_projects(self) -> List[ProjectInfo]:
        projects: Dict[str, ProjectInfo] = {
            context.info.project_id: context.info for context in self._contexts.values()
        }
        for entry in load_project_index():
            info = ProjectInfo(
                project_id=entry.project_id,
                project_name=entry.project_name,
                project_root=entry.project_root,
                target_root=entry.target_root,
            )
            projects[info.project_id] = info
        return list(projects.values())

    def get_context(self, project_id: Optional[str]) -> ProjectContext:
        if not project_id:
            project_id = self._default_id
        context = self._contexts.get(project_id)
        if context:
            return context
        for info in self.list_projects():
            if info.project_id == project_id:
                paths = ProjectPaths.create(info.project_root, Path(info.target_root))
                paths.ensure_directories()
                context = ProjectContext(info=info, paths=paths, manager=SessionManager(paths))
                self._contexts[project_id] = context
                return context
        raise KeyError(project_id)

    def default_project(self) -> ProjectInfo:
        return self.get_context(self._default_id).info



class GalleryServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

    def __init__(self, address: tuple[str, int], registry: ProjectRegistry) -> None:
        handler = _make_handler(registry)
        super().__init__(address, handler)
        self.registry = registry


def serve_gallery(
    config: ProjectConfig,
    paths: ProjectPaths,
    host: str = "127.0.0.1",
    port: int = 8765,
) -> None:
    registry = ProjectRegistry(config, paths)
    with GalleryServer((host, port), registry) as server:
        print(f"Gallery serving at http://{host}:{port}/")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("Stopping gallery...")


def _make_handler(registry: ProjectRegistry):

    class Handler(http.server.BaseHTTPRequestHandler):
        server_version = "ImageGallery/1.0"

        def do_GET(self) -> None:  # noqa: N802 (HTTP method name)
            parsed = urlparse(self.path)
            if parsed.path == "/":
                return self._serve_app(parsed)
            if parsed.path == "/media":
                return self._handle_media(parsed)
            if parsed.path == "/selected":
                return self._handle_selected(parsed)
            if parsed.path.startswith("/api/"):
                return self._handle_api(parsed)
            self._not_found()

        def do_POST(self) -> None:  # noqa: N802
            if self.path == "/select":
                return self._handle_select(redirect=True)
            if self.path == "/api/select":
                return self._handle_select(redirect=False)
            if self.path == "/api/register":
                return self._handle_register()
            self._not_found()

        def _handle_media(self, parsed) -> None:
            params = parse_qs(parsed.query)
            project_id = params.get("project", [None])[0]
            slot = params.get("slot", [None])[0]
            session_id = params.get("session", [None])[0]
            filename = params.get("file", [None])[0]
            if not slot or not session_id or not filename:
                return self._not_found()
            context = self._get_context(project_id)
            if context is None:
                return self._not_found()
            try:
                ctx = context.manager.create_context(slot, session_id)
            except (ValueError, InvalidPathError):
                return self._not_found()
            manifest_path = ctx.manifest_path
            if not manifest_path.exists():
                return self._not_found()
            manifest = context.manager.read_manifest(ctx)
            allowed = {image.filename for image in manifest.images}
            allowed.update({image.raw_filename for image in manifest.images if image.raw_filename})
            if filename not in allowed:
                return self._not_found()
            file_path = ctx.session_dir / filename
            if not file_path.exists():
                return self._not_found()
            content_type = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"
            with file_path.open("rb") as fh:
                data = fh.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def _handle_selected(self, parsed) -> None:
            params = parse_qs(parsed.query)
            project_id = params.get("project", [None])[0]
            slot = params.get("slot", [None])[0]
            if slot is None:
                return self._bad_request("Missing slot")
            context = self._get_context(project_id)
            if context is None:
                return self._not_found()
            try:
                target_path = context.paths.target_for_slot(slot)
            except (ValueError, InvalidPathError):
                return self._not_found()
            if not target_path.exists():
                return self._not_found()
            content_type = mimetypes.guess_type(str(target_path))[0] or "application/octet-stream"
            with target_path.open("rb") as fh:
                data = fh.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def _handle_select(self, redirect: bool) -> None:
            length = int(self.headers.get("Content-Length", "0"))
            body = self.rfile.read(length).decode("utf-8")
            params = parse_qs(body)
            project_id = params.get("project", [None])[0]
            slot = params.get("slot", [None])[0]
            session_id = params.get("session", [None])[0]
            index_raw = params.get("index", [None])[0]
            if slot is None or session_id is None or index_raw is None:
                return self._bad_request("Missing parameters")
            try:
                index = int(index_raw)
            except ValueError:
                return self._bad_request("Invalid index")
            context = self._get_context(project_id)
            if context is None:
                return self._not_found()
            try:
                ctx = context.manager.create_context(slot, session_id)
            except (ValueError, InvalidPathError):
                return self._not_found()
            if not ctx.manifest_path.exists():
                return self._not_found()
            manifest = context.manager.read_manifest(ctx)
            if index < 0 or index >= len(manifest.images):
                return self._bad_request("Index out of range")
            context.manager.promote_variant(ctx, manifest, index)
            if redirect:
                redirect_to = "/"
                self.send_response(303)
                self.send_header("Location", redirect_to)
                self.end_headers()
                return
            response = {
                "ok": True,
                "projectId": context.info.project_id,
                "slot": slot,
                "sessionId": session_id,
                "selectedIndex": index,
            }
            self._write_json(response)

        def _handle_api(self, parsed) -> None:
            parts = [segment for segment in parsed.path.strip("/").split("/") if segment]
            if len(parts) == 1 and parts[0] == "api":
                return self._write_json({"ok": True})
            if len(parts) == 2 and parts[0] == "api" and parts[1] == "projects":
                return self._handle_api_projects()
            if len(parts) >= 2 and parts[0] == "api" and parts[1] == "slots":
                params = parse_qs(parsed.query)
                project_id = params.get("project", [None])[0]
                if len(parts) == 2:
                    return self._handle_api_slots(project_id)
                slot = unquote(parts[2])
                if len(parts) == 3:
                    return self._handle_api_slot(project_id, slot)
                if len(parts) == 4 and parts[3] == "sessions":
                    return self._handle_api_slot_sessions(project_id, slot)
                if len(parts) == 5 and parts[3] == "sessions":
                    session_id = unquote(parts[4])
                    return self._handle_api_session_detail(project_id, slot, session_id)
            self._not_found()

        def _handle_api_projects(self) -> None:
            projects = []
            for info in registry.list_projects():
                projects.append(
                    {
                        "projectId": info.project_id,
                        "projectName": info.project_name,
                        "projectRoot": str(info.project_root),
                        "targetRoot": info.target_root,
                    }
                )
            default_info = registry.default_project()
            self._write_json(
                {
                    "projects": projects,
                    "defaultProjectId": default_info.project_id,
                }
            )

        def _handle_api_slots(self, project_id: Optional[str]) -> None:
            context = self._get_context(project_id)
            if context is None:
                return self._not_found()
            summaries = build_slot_index(context.paths)
            items = []
            for slot, summary in sorted(summaries.items()):
                last_updated = summary.last_updated
                items.append(
                    {
                        "slot": slot,
                        "sessionCount": summary.session_count,
                        "selectedPath": summary.selected_path,
                        "selectedIndex": summary.selected_index,
                        "lastUpdated": format_ts(last_updated) if last_updated else None,
                        "warningCount": len(summary.warnings),
                        "selectedImageUrl": self._selected_image_url(context.info.project_id, slot),
                    }
                )
            self._write_json(
                {
                    "projectId": context.info.project_id,
                    "projectName": context.info.project_name,
                    "slots": items,
                }
            )

        def _handle_api_slot(self, project_id: Optional[str], slot: str) -> None:
            context = self._get_context(project_id)
            if context is None:
                return self._not_found()
            try:
                manifests = list_manifests_for_slot(context.paths, slot)
            except (ValueError, InvalidPathError):
                return self._not_found()
            manifests.sort(key=lambda m: m.completed_at, reverse=True)
            summaries = [self._summarize_session(context, manifest) for manifest in manifests]
            variants: List[Dict[str, object]] = []
            slot_selected_hash = None
            current_selection = None
            if manifests:
                latest_manifest = manifests[0]
                if latest_manifest.images:
                    selected_index = latest_manifest.selected_index
                    if 0 <= selected_index < len(latest_manifest.images):
                        selected_image = latest_manifest.images[selected_index]
                        slot_selected_hash = selected_image.sha256
                        current_selection = {
                            "projectId": context.info.project_id,
                            "projectName": context.info.project_name,
                            "slot": latest_manifest.slot,
                            "sessionId": latest_manifest.session_id,
                            "variantIndex": selected_index,
                            "completedAt": format_ts(latest_manifest.completed_at),
                            "processed": {
                                "url": self._variant_media_url(
                                    context.info.project_id,
                                    latest_manifest.slot,
                                    latest_manifest.session_id,
                                    selected_image.filename,
                                ),
                                "filename": selected_image.filename,
                                "width": selected_image.width,
                                "height": selected_image.height,
                                "mediaType": selected_image.media_type,
                            },
                            "raw": (
                                {
                                    "url": self._variant_media_url(
                                        context.info.project_id,
                                        latest_manifest.slot,
                                        latest_manifest.session_id,
                                        selected_image.raw_filename,
                                    ),
                                    "filename": selected_image.raw_filename,
                                }
                                if selected_image.raw_filename
                                else None
                            ),
                            "slotImageUrl": self._selected_image_url(context.info.project_id, latest_manifest.slot),
                        }
            for manifest in manifests:
                variants.extend(self._map_manifest_variants(context, manifest, slot_selected_hash))
            variants.sort(key=lambda item: item["capturedAt"], reverse=True)
            self._write_json(
                {
                    "projectId": context.info.project_id,
                    "projectName": context.info.project_name,
                    "slot": slot,
                    "sessions": summaries,
                    "variants": variants,
                    "currentSelection": current_selection,
                }
            )

        def _handle_api_slot_sessions(self, project_id: Optional[str], slot: str) -> None:
            context = self._get_context(project_id)
            if context is None:
                return self._not_found()
            try:
                manifests = list_manifests_for_slot(context.paths, slot)
            except (ValueError, InvalidPathError):
                return self._not_found()
            manifests.sort(key=lambda m: m.completed_at, reverse=True)
            summaries = [self._summarize_session(context, manifest) for manifest in manifests]
            variants: List[Dict[str, object]] = []
            slot_selected_hash = None
            current_selection = None
            if manifests:
                latest_manifest = manifests[0]
                if latest_manifest.images:
                    selected_index = latest_manifest.selected_index
                    if 0 <= selected_index < len(latest_manifest.images):
                        selected_image = latest_manifest.images[selected_index]
                        slot_selected_hash = selected_image.sha256
                        current_selection = {
                            "projectId": context.info.project_id,
                            "projectName": context.info.project_name,
                            "slot": latest_manifest.slot,
                            "sessionId": latest_manifest.session_id,
                            "variantIndex": selected_index,
                            "completedAt": format_ts(latest_manifest.completed_at),
                            "processed": {
                                "url": self._variant_media_url(
                                    context.info.project_id,
                                    latest_manifest.slot,
                                    latest_manifest.session_id,
                                    selected_image.filename,
                                ),
                                "filename": selected_image.filename,
                                "width": selected_image.width,
                                "height": selected_image.height,
                                "mediaType": selected_image.media_type,
                            },
                            "raw": (
                                {
                                    "url": self._variant_media_url(
                                        context.info.project_id,
                                        latest_manifest.slot,
                                        latest_manifest.session_id,
                                        selected_image.raw_filename,
                                    ),
                                    "filename": selected_image.raw_filename,
                                }
                                if selected_image.raw_filename
                                else None
                            ),
                            "slotImageUrl": self._selected_image_url(context.info.project_id, latest_manifest.slot),
                        }
            for manifest in manifests:
                variants.extend(self._map_manifest_variants(context, manifest, slot_selected_hash))
            variants.sort(key=lambda item: item["capturedAt"], reverse=True)
            self._write_json(
                {
                    "projectId": context.info.project_id,
                    "projectName": context.info.project_name,
                    "slot": slot,
                    "sessions": summaries,
                    "variants": variants,
                    "currentSelection": current_selection,
                }
            )

        def _handle_api_session_detail(self, project_id: Optional[str], slot: str, session_id: str) -> None:
            context = self._get_context(project_id)
            if context is None:
                return self._not_found()
            ctx, manifest = self._resolve_session(context, slot, session_id)
            if manifest is None or ctx is None:
                return self._not_found()
            detail = manifest.to_dict()
            variants = []
            for index, image in enumerate(manifest.images):
                processed_url = self._variant_media_url(context.info.project_id, manifest.slot, session_id, image.filename)
                raw_url = None
                if image.raw_filename:
                    raw_url = self._variant_media_url(context.info.project_id, manifest.slot, session_id, image.raw_filename)
                variants.append(
                    {
                        "index": index,
                        "selected": index == manifest.selected_index,
                        "processed": {
                            "url": processed_url,
                            "filename": image.filename,
                            "width": image.width,
                            "height": image.height,
                            "mediaType": image.media_type,
                        },
                        "raw": {
                            "url": raw_url,
                            "filename": image.raw_filename,
                        }
                        if raw_url
                        else None,
                        "sha256": image.sha256,
                        "original": {
                            "width": image.original_width,
                            "height": image.original_height,
                        },
                        "cropFraction": image.crop_fraction,
                    }
                )
            detail["variants"] = variants
            detail["projectId"] = context.info.project_id
            detail["projectName"] = context.info.project_name
            self._write_json(detail)
        def _find_session_dir(self, session_id: str):
            root = paths.sessions_root
            if not root.exists():
                return None
            for candidate in root.glob(f"*_{session_id}"):
                if candidate.is_dir():
                    return candidate
            return None

        def _serve_app(self, parsed=None) -> None:
            body = _app_html()
            self._write_html(body)

        def _write_html(self, body: str) -> None:
            data = body.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def _write_json(self, payload) -> None:
            data = json.dumps(payload).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def _get_context(self, project_id: Optional[str]) -> Optional[ProjectContext]:
            try:
                return registry.get_context(project_id)
            except KeyError:
                return None

        def _selected_image_url(self, project_id: str, slot: str) -> str:
            params = {
                "project": project_id,
                "slot": slot,
            }
            encoded = "&".join(f"{quote(str(key))}={quote(str(value))}" for key, value in params.items())
            return f"/selected?{encoded}"

        def _variant_media_url(
            self,
            project_id: str,
            slot: str,
            session_id: str,
            filename: str,
        ) -> str:
            params = {
                "project": project_id,
                "slot": slot,
                "session": session_id,
                "file": filename,
            }
            encoded = "&".join(f"{quote(str(key))}={quote(str(value))}" for key, value in params.items())
            return f"/media?{encoded}"

        def _resolve_session(
            self,
            context: ProjectContext,
            slot: str,
            session_id: str,
        ) -> tuple[Optional[object], Optional[object]]:
            try:
                ctx = context.manager.create_context(slot, session_id)
            except (ValueError, InvalidPathError):
                return None, None
            if not ctx.manifest_path.exists():
                return None, None
            try:
                manifest = context.manager.read_manifest(ctx)
            except FileNotFoundError:
                return None, None
            return ctx, manifest

        def _summarize_session(self, context: ProjectContext, manifest) -> Dict[str, object]:
            summary: Dict[str, object] = {
                "projectId": context.info.project_id,
                "projectName": context.info.project_name,
                "slot": manifest.slot,
                "sessionId": manifest.session_id,
                "completedAt": format_ts(manifest.completed_at),
                "createdAt": format_ts(manifest.created_at),
                "variantCount": len(manifest.images),
                "selectedIndex": manifest.selected_index,
                "selectedPath": manifest.selected_path,
                "warnings": list(manifest.warnings),
                "provider": manifest.effective.provider,
                "model": manifest.effective.model,
                "size": manifest.effective.size or manifest.effective.aspect_ratio,
                "prompt": manifest.effective.prompt,
                "requestText": manifest.request.request_text,
            }
            return summary

        def _map_manifest_variants(
            self,
            context: ProjectContext,
            manifest,
            slot_selected_hash: Optional[str],
        ) -> List[Dict[str, object]]:
            results: List[Dict[str, object]] = []
            session_selected_hash: Optional[str] = None
            if 0 <= manifest.selected_index < len(manifest.images):
                session_selected_hash = manifest.images[manifest.selected_index].sha256
            for index, image in enumerate(manifest.images):
                processed = {
                    "url": self._variant_media_url(
                        context.info.project_id,
                        manifest.slot,
                        manifest.session_id,
                        image.filename,
                    ),
                    "filename": image.filename,
                    "width": image.width,
                    "height": image.height,
                    "mediaType": image.media_type,
                }
                raw = None
                if image.raw_filename:
                    raw = {
                        "url": self._variant_media_url(
                            context.info.project_id,
                            manifest.slot,
                            manifest.session_id,
                            image.raw_filename,
                        ),
                        "filename": image.raw_filename,
                    }
                results.append(
                    {
                        "projectId": context.info.project_id,
                        "projectName": context.info.project_name,
                        "slot": manifest.slot,
                        "sessionId": manifest.session_id,
                        "variantIndex": index,
                        "processed": processed,
                        "raw": raw,
                        "sessionWarnings": list(manifest.warnings),
                        "sessionProvider": manifest.effective.provider,
                        "sessionModel": manifest.effective.model,
                        "sessionSize": manifest.effective.size or manifest.effective.aspect_ratio,
                        "sessionPrompt": manifest.effective.prompt,
                        "sessionRequest": manifest.request.request_text,
                        "sessionCompletedAt": format_ts(manifest.completed_at),
                        "sessionCreatedAt": format_ts(manifest.created_at),
                        "capturedAt": format_ts(manifest.completed_at),
                        "isSessionSelected": session_selected_hash is not None
                        and image.sha256 == session_selected_hash,
                        "isSlotSelected": slot_selected_hash is not None
                        and image.sha256 == slot_selected_hash,
                        "sha256": image.sha256,
                        "cropFraction": image.crop_fraction,
                        "original": {
                            "width": image.original_width,
                            "height": image.original_height,
                        },
                    }
                )
            return results

        def _not_found(self) -> None:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Not Found")

        def _bad_request(self, message: str) -> None:
            data = message.encode("utf-8")
            self.send_response(400)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)

        def log_message(self, format: str, *args) -> None:  # noqa: A003 - match BaseHTTPRequestHandler signature
            return  # Silence default logging to keep CLI output clean

    return Handler
def _app_html() -> str:
    return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>ImageMCP Gallery</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    :root {
      color-scheme: dark;
      --bg: #0b0b0f;
      --bg-surface: #15151a;
      --bg-panel: #1f1f28;
      --accent: #38bdf8;
      --accent-soft: rgba(56, 189, 248, 0.16);
      --accent-strong: rgba(56, 189, 248, 0.32);
      --text: #f5f5f5;
      --text-soft: #cbd5f5;
      --border: rgba(148, 163, 184, 0.18);
      --warning: #f97316;
      --warning-soft: rgba(249, 115, 22, 0.2);
      font-family: "Inter", "SF Pro Text", "Segoe UI", system-ui, sans-serif;
    }

    * { box-sizing: border-box; }

    body {
      margin: 0;
      min-height: 100vh;
      background: linear-gradient(160deg, #0b0b0f 0%, #11111a 40%, #060608 100%);
      color: var(--text);
    }

    a { color: var(--accent); text-decoration: none; }

    #app { min-height: 100vh; display: flex; flex-direction: column; }

    .top-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 1rem 1.5rem;
      background: rgba(12, 12, 20, 0.75);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 20;
    }

    .brand {
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      font-size: 0.9rem;
      color: var(--text-soft);
    }

    .project-switcher {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.35rem 0.55rem;
      border-radius: 999px;
      background: rgba(148, 163, 184, 0.12);
      border: 1px solid rgba(148, 163, 184, 0.18);
      font-size: 0.8rem;
    }

    .project-switcher label {
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--text-soft);
    }

    .project-switcher select {
      background: transparent;
      border: none;
      color: var(--text);
      font-size: 0.85rem;
      font-weight: 600;
      outline: none;
      appearance: none;
      padding-right: 1.4rem;
      position: relative;
      cursor: pointer;
    }

    .project-switcher select option {
      color: #0f172a;
    }

    .view-actions,
    .top-actions {
      display: flex;
      gap: 0.75rem;
      align-items: center;
    }

    main {
      flex: 1;
      padding: 1.5rem;
      max-width: 1280px;
      width: 100%;
      margin: 0 auto;
    }

    .view {
      display: none;
      flex-direction: column;
      gap: 1rem;
    }

    .view.active { display: flex; }

    .view-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .view-header h1 {
      font-size: 1.6rem;
      margin: 0;
    }

    .view-subtitle {
      display: inline-block;
      margin-top: 0.35rem;
      font-size: 0.85rem;
      color: var(--text-soft);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }

    .slot-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 1.25rem;
    }

    .slot-card {
      background: var(--bg-panel);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      cursor: pointer;
      transition: transform 0.2s ease, border 0.2s ease, box-shadow 0.2s ease;
      position: relative;
    }

    .slot-card:hover {
      transform: translateY(-3px);
      border-color: var(--accent);
      box-shadow: 0 16px 36px rgba(15, 118, 209, 0.18);
    }

    .slot-card[data-active="true"] {
      border-color: var(--accent);
      box-shadow: 0 12px 28px rgba(14, 165, 233, 0.22);
    }

    .slot-card.has-warning {
      border-color: var(--warning-soft);
      box-shadow: 0 0 0 1px var(--warning-soft);
    }

    .thumb {
      width: 100%;
      aspect-ratio: 4 / 3;
      border-radius: 10px;
      overflow: hidden;
      background: linear-gradient(135deg, rgba(148, 163, 184, 0.08), rgba(30, 41, 59, 0.16));
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }

    .thumb img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }

    .thumb-placeholder {
      font-size: 0.8rem;
      color: var(--text-soft);
      text-transform: uppercase;
      letter-spacing: 0.1em;
    }

    .slot-meta {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }

    .slot-meta h2 {
      margin: 0;
      font-size: 1rem;
      font-weight: 600;
      color: var(--text);
    }

    .slot-meta span {
      font-size: 0.85rem;
      color: var(--text-soft);
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 0.15rem 0.45rem;
      border-radius: 999px;
      background: var(--accent-soft);
      color: var(--accent);
      font-weight: 600;
    }

    .badge-warning {
      background: var(--warning-soft);
      color: var(--warning);
    }

    .badge-info {
      background: rgba(59, 130, 246, 0.25);
      color: #93c5fd;
    }

    .ghost-button,
    .primary-button {
      border-radius: 8px;
      border: 1px solid transparent;
      padding: 0.45rem 0.9rem;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      background: none;
      color: var(--text);
      transition: all 0.18s ease;
    }

    .ghost-button {
      border-color: rgba(148, 163, 184, 0.2);
      background: rgba(148, 163, 184, 0.08);
    }

    .ghost-button:hover {
      border-color: var(--accent);
      color: var(--accent);
    }

    .ghost-button[data-active="true"] {
      border-color: var(--accent);
      background: var(--accent-soft);
      color: var(--accent);
    }

    .primary-button {
      background: var(--accent);
      color: #020617;
      border-color: rgba(14, 165, 233, 0.4);
      box-shadow: 0 10px 30px rgba(14, 165, 233, 0.3);
    }

    .primary-button:hover {
      box-shadow: 0 18px 36px rgba(14, 165, 233, 0.35);
      transform: translateY(-1px);
    }

    .primary-button[disabled],
    .ghost-button[disabled] {
      opacity: 0.5;
      cursor: not-allowed;
      box-shadow: none;
    }

    .empty-state {
      padding: 2.5rem;
      border: 1px dashed rgba(148, 163, 184, 0.24);
      border-radius: 12px;
      text-align: center;
      color: var(--text-soft);
      margin-top: 1rem;
    }

    .slot-layout {
      display: grid;
      grid-template-columns: minmax(240px, 280px) 1fr;
      gap: 1.5rem;
    }

    .session-panel {
      background: rgba(15, 15, 25, 0.55);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 1rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      max-height: calc(100vh - 200px);
      overflow-y: auto;
    }

    .session-panel h2 {
      margin: 0;
      font-size: 1rem;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-soft);
    }

    .session-list {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }

    .session-item {
      border-radius: 10px;
      padding: 0.6rem 0.75rem;
      border: 1px solid transparent;
      background: rgba(148, 163, 184, 0.05);
      text-align: left;
      color: inherit;
      cursor: pointer;
      transition: all 0.18s ease;
    }

    .session-item strong {
      display: block;
      font-size: 0.85rem;
      color: var(--text);
    }

    .session-item span {
      display: block;
      font-size: 0.75rem;
      color: var(--text-soft);
    }

    .session-item:hover {
      border-color: var(--accent);
      background: var(--accent-soft);
    }

    .session-item.active {
      border-color: var(--accent);
      background: rgba(2, 132, 199, 0.28);
      box-shadow: 0 10px 24px rgba(14, 165, 233, 0.22);
    }

    .session-detail {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .session-summary {
      background: rgba(12, 12, 20, 0.6);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 1rem 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .summary-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.75rem;
      align-items: baseline;
      justify-content: space-between;
    }

    .summary-row h2 {
      margin: 0;
      font-size: 1.2rem;
    }

    .prompt-block {
      background: rgba(148, 163, 184, 0.08);
      border-radius: 10px;
      padding: 0.75rem;
      font-size: 0.9rem;
      line-height: 1.5;
      color: var(--text-soft);
      white-space: pre-wrap;
    }

    .warnings {
      border-radius: 12px;
      border: 1px solid var(--warning-soft);
      background: rgba(249, 115, 22, 0.08);
      padding: 0.85rem 1rem;
      color: var(--warning);
    }

    .warnings ul {
      margin: 0.5rem 0 0;
      padding-left: 1.1rem;
      color: var(--text);
    }

    .variant-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 1.25rem;
    }

    .variant-card {
      position: relative;
      border-radius: 14px;
      border: 1px solid var(--border);
      background: rgba(17, 24, 39, 0.55);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      padding: 0.75rem;
    }

    .variant-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
    }

    .variant-badges {
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem;
    }

    .variant-session {
      font-size: 0.78rem;
      color: var(--text-soft);
      white-space: nowrap;
    }

    .variant-card.is-selected {
      border-color: var(--accent);
      box-shadow: 0 16px 36px rgba(14, 165, 233, 0.28);
    }

    .variant-thumb {
      position: relative;
      border-radius: 10px;
      overflow: hidden;
      background: rgba(148, 163, 184, 0.08);
      aspect-ratio: 4 / 3;
    }

    .variant-thumb img {
      width: 100%;
      height: 100%;
      object-fit: contain;
      background: #0d1117;
    }

    .badge-selected {
      position: absolute;
      top: 0.75rem;
      left: 0.75rem;
      background: rgba(34, 197, 94, 0.24);
      color: #4ade80;
      padding: 0.25rem 0.6rem;
      border-radius: 999px;
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      font-weight: 600;
      backdrop-filter: blur(8px);
    }

    .variant-info {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
      font-size: 0.78rem;
      color: var(--text-soft);
    }

    .variant-info strong {
      font-size: 0.85rem;
      color: var(--text);
    }

    .variant-stats {
      display: flex;
      flex-wrap: wrap;
      gap: 0.55rem;
      font-size: 0.75rem;
      color: var(--text-soft);
    }

    .variant-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
    }

    .overlay {
      position: fixed;
      inset: 0;
      background: rgba(8, 8, 12, 0.85);
      backdrop-filter: blur(14px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 50;
    }

    .overlay.hidden { display: none; }

    .overlay-card {
      width: min(90vw, 640px);
      max-height: 80vh;
      overflow-y: auto;
      background: rgba(12, 12, 20, 0.95);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      box-shadow: 0 24px 64px rgba(2, 132, 199, 0.35);
    }

    .overlay-card h2 {
      margin: 0;
    }

    .overlay-grid {
      display: grid;
      grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
      gap: 0.75rem 1rem;
      font-size: 0.85rem;
    }

    .overlay-grid dt {
      font-weight: 600;
      color: var(--text-soft);
    }

    .overlay-grid dd {
      margin: 0;
      color: var(--text);
      word-break: break-word;
    }

    pre.metadata-json {
      background: rgba(15, 23, 42, 0.7);
      padding: 0.9rem;
      border-radius: 10px;
      overflow-x: auto;
      border: 1px solid rgba(148, 163, 184, 0.16);
      font-size: 0.75rem;
      color: var(--text-soft);
    }

    .toast {
      position: fixed;
      bottom: 1.5rem;
      left: 50%;
      transform: translateX(-50%);
      padding: 0.75rem 1.2rem;
      border-radius: 999px;
      background: rgba(15, 23, 42, 0.82);
      border: 1px solid rgba(56, 189, 248, 0.35);
      color: var(--text);
      font-size: 0.85rem;
      box-shadow: 0 10px 30px rgba(14, 165, 233, 0.25);
      z-index: 60;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }

    .toast.visible { opacity: 1; }

    .hidden { display: none !important; }

    @media (max-width: 720px) {
      .top-bar {
        flex-direction: column;
        align-items: flex-start;
        gap: 0.75rem;
      }
      .top-actions {
        width: 100%;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 0.6rem;
      }
      .project-switcher {
        width: 100%;
        justify-content: space-between;
      }
    }

    @media (max-width: 960px) {
      main { padding: 1rem; }
      .slot-layout {
        grid-template-columns: 1fr;
      }
      .session-panel { max-height: none; }
    }
  </style>
</head>
<body>
  <div id="app">
    <header class="top-bar">
      <div class="brand">ImageMCP Gallery</div>
      <div class="top-actions">
        <div class="project-switcher">
          <label for="project-select">Project</label>
          <select id="project-select"></select>
        </div>
        <button id="refresh-slots" class="ghost-button" type="button">Refresh</button>
        <a href="https://github.com/severindeutschmann/ImageMCP" target="_blank" rel="noreferrer" class="ghost-button" style="display:inline-flex;align-items:center;">
          Docs ↗
        </a>
      </div>
    </header>
    <main>
      <section id="slots-view" class="view active">
        <div class="view-header">
          <div>
            <h1>Image Slots</h1>
            <span id="project-label" class="view-subtitle"></span>
          </div>
          <div class="view-actions">
            <button id="filter-warnings" class="ghost-button" data-active="false" type="button">Warnings only</button>
          </div>
        </div>
        <div id="slot-grid" class="slot-grid"></div>
        <div id="slots-empty" class="empty-state hidden">
          No image slots yet. Run <code>imgen gen --slot &lt;name&gt; ...</code> to create the first session.
        </div>
      </section>

      <section id="slot-detail" class="view hidden">
        <div class="view-header">
          <div style="display:flex;gap:0.75rem;align-items:center;">
            <button id="back-to-slots" class="ghost-button" type="button">↩ All slots</button>
            <div>
              <h1 id="slot-title">Slot</h1>
              <span id="slot-subtitle" style="font-size:0.85rem;color:var(--text-soft);"></span>
            </div>
          </div>
          <div class="view-actions">
            <button id="open-selected" class="ghost-button" type="button">Open selected</button>
            <button id="refresh-slot" class="ghost-button" type="button">Refresh</button>
          </div>
        </div>
        <div class="slot-layout">
          <aside class="session-panel">
            <h2>Sessions</h2>
            <div id="session-list" class="session-list"></div>
            <div id="sessions-empty" class="empty-state hidden">No sessions yet for this slot.</div>
          </aside>
          <section class="session-detail">
            <div id="session-summary" class="session-summary hidden"></div>
            <div id="session-warnings" class="warnings hidden"></div>
            <div id="variant-grid" class="variant-grid"></div>
            <div id="variant-empty" class="empty-state hidden">No variants yet. Generate images to populate this gallery.</div>
          </section>
        </div>
      </section>
    </main>
  </div>

  <div id="metadata-overlay" class="overlay hidden">
    <div class="overlay-card">
      <div style="display:flex;justify-content:space-between;align-items:center;gap:1rem;">
        <h2 id="metadata-title">Variant details</h2>
        <button id="metadata-close" class="ghost-button" type="button">Close</button>
      </div>
      <dl id="metadata-grid" class="overlay-grid"></dl>
      <pre id="metadata-json" class="metadata-json"></pre>
    </div>
  </div>

  <div id="toast" class="toast hidden"></div>

  <script>
    (function() {
      const state = {
        projects: [],
        projectId: null,
        projectName: null,
        slots: [],
        slot: null,
        sessions: [],
        variants: [],
        sessionFilter: null,
        currentSelection: null,
        filterWarnings: false,
        pendingSlot: null,
      };

      const urlParams = new URLSearchParams(window.location.search);
      const initialProjectParam = urlParams.get('project');
      const initialSlotParam = urlParams.get('slot');
      state.pendingSlot = initialSlotParam;

      const slotGrid = document.getElementById('slot-grid');
      const slotsEmpty = document.getElementById('slots-empty');
      const slotsEmptyDefault = slotsEmpty ? slotsEmpty.innerHTML : '';
      const slotsView = document.getElementById('slots-view');
      const slotDetailView = document.getElementById('slot-detail');
      const slotTitle = document.getElementById('slot-title');
      const slotSubtitle = document.getElementById('slot-subtitle');
      const sessionList = document.getElementById('session-list');
      const sessionsEmpty = document.getElementById('sessions-empty');
      const sessionSummary = document.getElementById('session-summary');
      const sessionWarnings = document.getElementById('session-warnings');
      const variantGrid = document.getElementById('variant-grid');
      const variantEmpty = document.getElementById('variant-empty');
      const toast = document.getElementById('toast');
      const metadataOverlay = document.getElementById('metadata-overlay');
      const metadataGrid = document.getElementById('metadata-grid');
      const metadataJson = document.getElementById('metadata-json');
      const metadataTitle = document.getElementById('metadata-title');

      const projectSelect = document.getElementById('project-select');
      const projectLabel = document.getElementById('project-label');

      if (projectLabel) {
        projectLabel.textContent = 'Loading projects…';
      }

      const refreshSlotsBtn = document.getElementById('refresh-slots');
      const refreshSlotBtn = document.getElementById('refresh-slot');
      const filterWarningsBtn = document.getElementById('filter-warnings');
      const backToSlotsBtn = document.getElementById('back-to-slots');
      const openSelectedBtn = document.getElementById('open-selected');
      const metadataCloseBtn = document.getElementById('metadata-close');

      function showToast(message, kind = 'info') {
        toast.textContent = message;
        toast.dataset.kind = kind;
        toast.classList.remove('hidden');
        toast.classList.add('visible');
        clearTimeout(showToast._timer);
        showToast._timer = setTimeout(() => {
          toast.classList.remove('visible');
        }, 2600);
      }

      function escapeHtml(text) {
        if (text === null || text === undefined) return '';
        return String(text)
          .replace(/&/g, '&amp;')
          .replace(/</g, '&lt;')
          .replace(/>/g, '&gt;')
          .replace(/"/g, '&quot;')
          .replace(/'/g, '&#39;');
      }

      function formatTimestamp(ts) {
        if (!ts) return 'n/a';
        try {
          const date = new Date(ts);
          if (Number.isNaN(date.getTime())) return ts;
          return date.toLocaleString();
        } catch (error) {
          return ts;
        }
      }

      function getProjectById(projectId) {
        if (!projectId) return null;
        return state.projects.find((item) => item.projectId === projectId) || null;
      }

      function getProjectName(projectId) {
        const project = getProjectById(projectId);
        if (!project) return null;
        return project.projectName || project.projectId;
      }

      function updateDocumentTitle() {
        if (state.projectName) {
          document.title = `ImageMCP Gallery · ${state.projectName}`;
        } else {
          document.title = 'ImageMCP Gallery';
        }
      }

      function updateProjectSummary() {
        if (!projectLabel) return;
        if (!state.projectId) {
          projectLabel.textContent = 'No project selected';
          return;
        }
        const label = getProjectName(state.projectId) || state.projectId;
        projectLabel.textContent = `Project: ${label}`;
      }

      function renderProjectSelector() {
        if (!projectSelect) return;
        if (!state.projects.length) {
          projectSelect.innerHTML = '<option value="">No projects</option>';
          projectSelect.disabled = true;
          return;
        }
        projectSelect.disabled = false;
        projectSelect.innerHTML = state.projects
          .map((project) => `<option value="${escapeHtml(project.projectId)}">${escapeHtml(project.projectName || project.projectId)}</option>`)
          .join('');
        if (state.projectId) {
          projectSelect.value = state.projectId;
        }
      }

      function updateUrlState() {
        const params = new URLSearchParams();
        if (state.projectId) {
          params.set('project', state.projectId);
        }
        if (state.slot) {
          params.set('slot', state.slot);
        }
        const next = params.toString();
        const target = next ? `${window.location.pathname}?${next}` : window.location.pathname;
        const current = `${window.location.pathname}${window.location.search}`;
        if (target !== current) {
          window.history.replaceState(null, '', target);
        }
      }

      function resetSlotView() {
        slotDetailView.classList.remove('active');
        slotDetailView.classList.add('hidden');
        slotsView.classList.remove('hidden');
        slotsView.classList.add('active');
        state.slot = null;
        state.sessions = [];
        state.variants = [];
        state.sessionFilter = null;
        state.currentSelection = null;
        sessionList.innerHTML = '';
        sessionSummary.classList.add('hidden');
        sessionWarnings.classList.add('hidden');
        sessionWarnings.innerHTML = '';
        variantGrid.innerHTML = '';
        variantEmpty.classList.add('hidden');
      }

      function setProject(projectId, { skipReload = false, updateUrl = true, preserveSlot = false } = {}) {
        if (!projectId) {
          return;
        }
        if (state.projectId === projectId) {
          if (!skipReload) {
            loadSlots();
          }
          return;
        }
        const project = getProjectById(projectId);
        state.projectId = projectId;
        state.projectName = project ? (project.projectName || project.projectId) : projectId;
        if (projectSelect) {
          projectSelect.value = projectId;
        }
        if (!preserveSlot) {
          resetSlotView();
          state.pendingSlot = null;
          state.slots = [];
          renderSlots();
        }
        updateProjectSummary();
        updateDocumentTitle();
        if (updateUrl) {
          updateUrlState();
        }
        if (!skipReload) {
          loadSlots();
        }
      }

      async function loadProjects() {
        try {
          const res = await fetch('/api/projects');
          if (!res.ok) throw new Error('Failed to load projects');
          const data = await res.json();
          state.projects = Array.isArray(data.projects) ? data.projects : [];
          const defaultProjectId = data.defaultProjectId || (state.projects[0] && state.projects[0].projectId) || null;
          renderProjectSelector();
          let desiredProject = initialProjectParam;
          if (!desiredProject || !getProjectById(desiredProject)) {
            desiredProject = state.projectId || defaultProjectId;
          }
          if (desiredProject) {
            const project = getProjectById(desiredProject);
            state.projectId = desiredProject;
            state.projectName = project ? (project.projectName || project.projectId) : desiredProject;
            if (projectSelect) {
              projectSelect.value = desiredProject;
            }
          } else {
            state.projectId = null;
            state.projectName = null;
          }
          updateProjectSummary();
          updateDocumentTitle();
          if (state.projectId) {
            await loadSlots({ initial: true });
          } else {
            renderSlots();
          }
          if ((!initialProjectParam || !getProjectById(initialProjectParam)) && state.projectId) {
            updateUrlState();
          }
          if (projectSelect) {
            projectSelect.disabled = !state.projects.length;
          }
        } catch (error) {
          console.error(error);
          showToast('Unable to load projects', 'error');
        }
      }

      async function loadSlots(options = {}) {
        const { initial = false, forceReload = false } = options;
        if (!state.projectId) {
          state.slots = [];
          renderSlots();
          updateProjectSummary();
          return;
        }
        try {
          const params = new URLSearchParams({ project: state.projectId });
          if (forceReload) {
            params.set('_', Date.now().toString());
          }
          const fetchOptions = forceReload ? { cache: 'no-store' } : {};
          const res = await fetch(`/api/slots?${params.toString()}`, fetchOptions);
          if (!res.ok) throw new Error('Failed to load slots');
          const data = await res.json();
          state.slots = data.slots || [];
          if (data.projectId) {
            state.projectId = data.projectId;
          }
          if (data.projectName) {
            state.projectName = data.projectName;
          } else {
            state.projectName = getProjectName(state.projectId) || state.projectName;
          }
          renderProjectSelector();
          updateProjectSummary();
          updateDocumentTitle();
          renderSlots();
          if (state.slot) {
            const summary = state.slots.find((item) => item.slot === state.slot);
            if (summary && !state.currentSelection && summary.selectedImageUrl) {
              state.currentSelection = { slotImageUrl: summary.selectedImageUrl };
            }
            updateSlotHeader();
          }
          if (initial && state.pendingSlot) {
            const desiredSlot = state.pendingSlot;
            state.pendingSlot = null;
            if (desiredSlot) {
              const summary = state.slots.find((item) => item.slot === desiredSlot);
              if (summary) {
                await selectSlot(desiredSlot);
              }
            }
          }
        } catch (error) {
          console.error(error);
          showToast('Unable to load slots', 'error');
        }
      }

      function renderSlots() {
        const items = state.filterWarnings
          ? state.slots.filter((slot) => slot.warningCount > 0)
          : state.slots;
        filterWarningsBtn.dataset.active = state.filterWarnings ? 'true' : 'false';
        filterWarningsBtn.textContent = state.filterWarnings ? 'Showing warnings only' : 'Warnings only';
        if (!items.length) {
          slotGrid.innerHTML = '';
          if (slotsEmpty) {
            if (!state.projectId) {
              slotsEmpty.textContent = 'Select or initialize a project to view its image slots.';
            } else {
              slotsEmpty.innerHTML = slotsEmptyDefault;
            }
            slotsEmpty.classList.remove('hidden');
          }
          return;
        }
        if (slotsEmpty) {
          slotsEmpty.classList.add('hidden');
          slotsEmpty.innerHTML = slotsEmptyDefault;
        }
        slotGrid.innerHTML = items
          .map((slot) => {
            const warningBadge = slot.warningCount
              ? `<span class="badge badge-warning">⚠ ${slot.warningCount} warning${slot.warningCount === 1 ? '' : 's'}</span>`
              : '';
            const image = slot.selectedImageUrl
              ? `<img src="${slot.selectedImageUrl}" alt="${escapeHtml(slot.slot)} preview">`
              : '<div class="thumb-placeholder">No preview</div>';
            const updated = slot.lastUpdated ? formatTimestamp(slot.lastUpdated) : 'never';
            const active = state.slot && state.slot === slot.slot;
            return `
              <article class="slot-card ${slot.warningCount ? 'has-warning' : ''}" data-slot="${escapeHtml(slot.slot)}" data-active="${active ? 'true' : 'false'}">
                <div class="thumb">${image}</div>
                <div class="slot-meta">
                  <h2>${escapeHtml(slot.slot)}</h2>
                  <span>Sessions: ${slot.sessionCount}</span>
                  <span>Updated: ${escapeHtml(updated)}</span>
                  ${warningBadge}
                </div>
              </article>
            `;
          })
          .join('');
      }

      async function selectSlot(slotId) {
        state.slot = slotId;
        slotsView.classList.remove('active');
        slotsView.classList.add('hidden');
        slotDetailView.classList.remove('hidden');
        slotDetailView.classList.add('active');
        await loadSlotData(slotId);
      }

      async function loadSlotData(slotId, options = {}) {
        if (!state.projectId) return;
        const { forceReload = false, preserveFilter = false } = options;
        const previousFilter = preserveFilter ? state.sessionFilter : null;
        try {
          const params = new URLSearchParams({ project: state.projectId });
          if (forceReload) {
            params.set('_', Date.now().toString());
          }
          const fetchOptions = forceReload ? { cache: 'no-store' } : {};
          const res = await fetch(`/api/slots/${encodeURIComponent(slotId)}/sessions?${params.toString()}`, fetchOptions);
          if (!res.ok) throw new Error('Failed to load slot data');
          const data = await res.json();
          state.slot = data.slot || slotId;
          if (data.projectId) {
            state.projectId = data.projectId;
          }
          if (data.projectName) {
            state.projectName = data.projectName;
          } else {
            state.projectName = getProjectName(state.projectId) || state.projectName;
          }
          state.sessions = Array.isArray(data.sessions) ? data.sessions : [];
          state.variants = Array.isArray(data.variants) ? data.variants : [];
          if (preserveFilter && previousFilter) {
            const hasFilter = state.sessions.some((session) => session.sessionId === previousFilter);
            state.sessionFilter = hasFilter ? previousFilter : null;
          } else {
            state.sessionFilter = null;
          }
          state.currentSelection = data.currentSelection || null;
          updateProjectSummary();
          updateDocumentTitle();
          updateSlotHeader();
          renderSlots();
          renderSessionList();
          renderSessionSummary();
          renderVariantFeed();
          updateUrlState();
        } catch (error) {
          console.error(error);
          showToast('Unable to load slot data', 'error');
        }
      }

      function updateSlotHeader() {
        slotTitle.textContent = state.slot || 'Slot';
        const latestSession = state.sessions.length ? state.sessions[0] : null;
        const subtitleParts = [];
        if (state.projectName || state.projectId) {
          subtitleParts.push(`Project ${state.projectName || state.projectId}`);
        }
        if (latestSession) {
          subtitleParts.push(`Updated ${formatTimestamp(latestSession.completedAt)}`);
        } else {
          subtitleParts.push('No sessions yet');
        }
        slotSubtitle.textContent = subtitleParts.join(' • ');
        const slotUrl = (state.currentSelection && state.currentSelection.slotImageUrl)
          || (state.sessions.length && state.projectId
            ? `/selected?project=${encodeURIComponent(state.projectId)}&slot=${encodeURIComponent(state.slot)}`
            : null);
        openSelectedBtn.dataset.url = slotUrl || '';
        openSelectedBtn.disabled = !slotUrl;
      }

      function renderSessionList() {
        if (!state.sessions.length) {
          sessionList.innerHTML = '';
          sessionsEmpty.classList.remove('hidden');
          return;
        }
        sessionsEmpty.classList.add('hidden');
        const activeSession = state.sessionFilter;
        const latest = state.sessions[0];
        const items = [];
        items.push(`
          <button class="session-item ${activeSession ? '' : 'active'}" data-session="__all__" type="button">
            <strong>All sessions</strong>
            <span>${state.sessions.length} total • Last ${escapeHtml(formatTimestamp(latest.completedAt))}</span>
          </button>
        `);
        state.sessions.forEach((session) => {
          const isActive = activeSession === session.sessionId;
          const warningBadge = session.warnings && session.warnings.length
            ? `<span>⚠ ${session.warnings.length} warning${session.warnings.length === 1 ? '' : 's'}</span>`
            : '';
          items.push(`
            <button class="session-item ${isActive ? 'active' : ''}" data-session="${escapeHtml(session.sessionId)}" type="button">
              <strong>${escapeHtml(formatTimestamp(session.completedAt))}</strong>
              <span>#${session.selectedIndex} • ${session.variantCount} variant${session.variantCount === 1 ? '' : 's'}</span>
              ${warningBadge}
            </button>
          `);
        });
        sessionList.innerHTML = items.join('');
      }

      function renderSessionSummary() {
        if (!state.sessions.length) {
          sessionSummary.classList.add('hidden');
          sessionWarnings.classList.add('hidden');
          sessionSummary.innerHTML = '';
          sessionWarnings.innerHTML = '';
          return;
        }
        const summarySession = state.sessionFilter
          ? state.sessions.find((item) => item.sessionId === state.sessionFilter)
          : state.sessions[0];
        if (!summarySession) {
          sessionSummary.classList.add('hidden');
          sessionWarnings.classList.add('hidden');
          return;
        }
        if (!state.sessionFilter) {
          sessionSummary.innerHTML = `
            <div class="summary-row">
              <div>
                <h2>All Sessions</h2>
                <span>${state.sessions.length} total runs</span>
              </div>
              <div style="font-size:0.82rem;color:var(--text-soft);text-align:right;">
                <div>Latest completed ${escapeHtml(formatTimestamp(summarySession.completedAt))}</div>
                <div>Pick a session to inspect prompts &amp; warnings.</div>
              </div>
            </div>
          `;
          sessionSummary.classList.remove('hidden');
          sessionWarnings.classList.add('hidden');
          sessionWarnings.innerHTML = '';
          return;
        }
        const provider = summarySession.provider || 'provider?';
        const model = summarySession.model || 'model?';
        const size = summarySession.size || 'size?';
        const prompt = summarySession.prompt || 'No prompt recorded';
        const requestText = summarySession.requestText || '—';
        sessionSummary.innerHTML = `
          <div class="summary-row">
            <div>
              <h2>Session ${escapeHtml(summarySession.sessionId)}</h2>
              <span>Completed ${escapeHtml(formatTimestamp(summarySession.completedAt))}</span>
            </div>
            <div style="font-size:0.82rem;color:var(--text-soft);text-align:right;">
              <div>${escapeHtml(provider)} • ${escapeHtml(model)}</div>
              <div>${escapeHtml(size)}</div>
            </div>
          </div>
          <div style="font-size:0.85rem;color:var(--text-soft);">Request: ${escapeHtml(requestText)}</div>
          <div class="prompt-block">${escapeHtml(prompt)}</div>
          <div style="font-size:0.75rem;color:var(--text-soft);">Created ${escapeHtml(formatTimestamp(summarySession.createdAt))}</div>
        `;
        sessionSummary.classList.remove('hidden');
        if (summarySession.warnings && summarySession.warnings.length) {
          sessionWarnings.innerHTML = `
            <strong>Warnings</strong>
            <ul>${summarySession.warnings.map((item) => `<li>${escapeHtml(item)}</li>`).join('')}</ul>
          `;
          sessionWarnings.classList.remove('hidden');
        } else {
          sessionWarnings.classList.add('hidden');
          sessionWarnings.innerHTML = '';
        }
      }

      function renderVariantFeed() {
        let variants = state.variants;
        if (state.sessionFilter) {
          variants = variants.filter((variant) => variant.sessionId === state.sessionFilter);
        }
        if (!variants.length) {
          variantGrid.innerHTML = '';
          variantEmpty.classList.remove('hidden');
          return;
        }
        variantEmpty.classList.add('hidden');
        variantGrid.innerHTML = variants
          .map((variant) => {
            const cropPercent = typeof variant.cropFraction === 'number'
              ? `${(variant.cropFraction * 100).toFixed(1)}%`
              : '0%';
            const originalLabel = variant.original && variant.original.width
              ? `Original ${variant.original.width}×${variant.original.height}`
              : 'Original n/a';
            const badges = [];
            if (variant.isSlotSelected) {
              badges.push('<span class="badge badge-info">Current slot</span>');
            }
            if (!variant.isSlotSelected && variant.isSessionSelected) {
              badges.push('<span class="badge badge-info">Session pick</span>');
            }
            if (variant.sessionWarnings && variant.sessionWarnings.length) {
              badges.push(`<span class="badge badge-warning">⚠ ${variant.sessionWarnings.length}</span>`);
            }
            const providerLine = [
              variant.sessionProvider || 'provider?',
              variant.sessionModel || 'model?',
              variant.sessionSize || 'size?',
            ].filter(Boolean).join(' • ');
            return `
              <article class="variant-card ${variant.isSlotSelected ? 'is-selected' : ''}" data-session="${escapeHtml(variant.sessionId)}" data-index="${variant.variantIndex}">
                <div class="variant-header">
                  <div class="variant-badges">${badges.join('')}</div>
                  <span class="variant-session">${escapeHtml(formatTimestamp(variant.sessionCompletedAt))}</span>
                </div>
                <div class="variant-thumb">
                  ${variant.isSlotSelected ? '<span class="badge-selected">Slot</span>' : ''}
                  <img src="${variant.processed.url}" alt="Variant ${variant.variantIndex}">
                </div>
                <div class="variant-info">
                  <strong>Session ${escapeHtml(variant.sessionId)} · #${variant.variantIndex}</strong>
                  <div>${escapeHtml(providerLine)}</div>
                  <div class="variant-stats">
                    <span>${variant.processed.width}×${variant.processed.height}</span>
                    <span>${escapeHtml(originalLabel)}</span>
                    <span>Crop ${cropPercent}</span>
                  </div>
                </div>
                <div class="variant-actions">
                  ${variant.raw ? `<button class="ghost-button" data-action="open-raw" data-session="${escapeHtml(variant.sessionId)}" data-index="${variant.variantIndex}" type="button">View raw</button>` : ''}
                  <button class="ghost-button" data-action="metadata" data-session="${escapeHtml(variant.sessionId)}" data-index="${variant.variantIndex}" type="button">Metadata</button>
                  <button class="primary-button" data-action="promote" data-session="${escapeHtml(variant.sessionId)}" data-index="${variant.variantIndex}" type="button" ${variant.isSlotSelected ? 'disabled' : ''}>Use this variant</button>
                </div>
              </article>
            `;
          })
          .join('');
      }

      function getVariant(sessionId, index) {
        return state.variants.find(
          (variant) => variant.sessionId === sessionId && variant.variantIndex === Number(index),
        );
      }

      function openMetadata(sessionId, index) {
        const variant = getVariant(sessionId, index);
        if (!variant) return;
        metadataTitle.textContent = `Variant #${variant.variantIndex} · Session ${variant.sessionId}`;
        const rows = [
          ['Slot', variant.slot],
          ['Session completed', formatTimestamp(variant.sessionCompletedAt)],
          ['Variant index', variant.variantIndex],
          ['Processed file', variant.processed.filename],
          ['Processed size', `${variant.processed.width}×${variant.processed.height}`],
          ['Media type', variant.processed.mediaType],
          ['Raw file', variant.raw ? variant.raw.filename : '—'],
          ['Crop fraction', typeof variant.cropFraction === 'number' ? variant.cropFraction.toFixed(3) : '—'],
          ['Original size', variant.original && variant.original.width ? `${variant.original.width}×${variant.original.height}` : '—'],
          ['Provider', variant.sessionProvider || '—'],
          ['Model', variant.sessionModel || '—'],
          ['Requested size', variant.sessionSize || '—'],
          ['Prompt', variant.sessionPrompt || '—'],
          ['Request text', variant.sessionRequest || '—'],
          ['SHA-256', variant.sha256],
        ];
        metadataGrid.innerHTML = rows
          .map(([label, value]) => `<dt>${escapeHtml(label)}</dt><dd>${escapeHtml(value || '—')}</dd>`)
          .join('');
        metadataJson.textContent = JSON.stringify(variant, null, 2);
        metadataOverlay.classList.remove('hidden');
      }

      function closeMetadata() {
        metadataOverlay.classList.add('hidden');
      }

      async function promoteVariant(sessionId, index) {
        const variant = getVariant(sessionId, index);
        if (!variant) return;
        try {
          const body = new URLSearchParams({
            slot: variant.slot,
            session: variant.sessionId,
            index: String(variant.variantIndex),
          });
          if (state.projectId) {
            body.set('project', state.projectId);
          }
          const res = await fetch('/api/select', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body,
          });
          if (!res.ok) throw new Error('Promote failed');
          showToast(`Promoted session ${variant.sessionId} #${variant.variantIndex}`);
          await loadSlotData(variant.slot, { forceReload: true, preserveFilter: true });
          await loadSlots({ forceReload: true });
        } catch (error) {
          console.error(error);
          showToast('Unable to promote variant', 'error');
        }
      }

      slotGrid.addEventListener('click', (event) => {
        const card = event.target.closest('.slot-card');
        if (!card) return;
        const slotId = card.dataset.slot;
        if (slotId) {
          selectSlot(slotId).catch((error) => console.error(error));
        }
      });

      sessionList.addEventListener('click', (event) => {
        const button = event.target.closest('.session-item');
        if (!button) return;
        const sessionId = button.dataset.session;
        state.sessionFilter = sessionId && sessionId !== '__all__' ? sessionId : null;
        renderSessionList();
        renderSessionSummary();
        renderVariantFeed();
      });

      variantGrid.addEventListener('click', (event) => {
        const button = event.target.closest('button');
        if (!button) return;
        const action = button.dataset.action;
        const sessionId = button.dataset.session;
        const index = button.dataset.index;
        if (!sessionId || index === undefined) return;
        if (action === 'metadata') {
          openMetadata(sessionId, index);
        } else if (action === 'promote') {
          promoteVariant(sessionId, index);
        } else if (action === 'open-raw') {
          const variant = getVariant(sessionId, index);
          if (variant && variant.raw && variant.raw.url) {
            window.open(variant.raw.url, '_blank');
          }
        }
      });

      if (projectSelect) {
        projectSelect.addEventListener('change', (event) => {
          const nextProject = event.target.value;
          if (!nextProject || nextProject === state.projectId) {
            return;
          }
          state.pendingSlot = null;
          setProject(nextProject);
        });
      }

      refreshSlotsBtn.addEventListener('click', () => {
        loadSlots({ forceReload: true });
      });

      refreshSlotBtn.addEventListener('click', async () => {
        if (state.slot) {
          await loadSlotData(state.slot, { forceReload: true, preserveFilter: true });
          await loadSlots({ forceReload: true });
        }
      });

      filterWarningsBtn.addEventListener('click', () => {
        state.filterWarnings = !state.filterWarnings;
        renderSlots();
      });

      backToSlotsBtn.addEventListener('click', () => {
        resetSlotView();
        updateUrlState();
        loadSlots();
      });

      openSelectedBtn.addEventListener('click', () => {
        const url = openSelectedBtn.dataset.url;
        if (url) {
          window.open(url, '_blank');
        }
      });

      metadataCloseBtn.addEventListener('click', closeMetadata);
      metadataOverlay.addEventListener('click', (event) => {
        if (event.target === metadataOverlay) {
          closeMetadata();
        }
      });

      loadProjects();
    })();
  </script>
</body>
</html>
"""


__all__ = ["serve_gallery", "GalleryServer"]
