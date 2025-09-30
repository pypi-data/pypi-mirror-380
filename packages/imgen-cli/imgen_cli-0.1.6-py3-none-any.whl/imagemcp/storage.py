from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional, Tuple

from .config import CONFIG_DIR_NAME
from .models import SessionManifest
from ._compat import dataclass

_SLOT_SESSION_PATTERN = re.compile(r"^(?P<slot>[a-z0-9_-]+)_(?P<session>.+)$")


class InvalidPathError(ValueError):
    """Raised when a resolved path escapes the allowed project root."""


@dataclass()
class ProjectPaths:
    project_root: Path
    target_root: Path
    sessions_root: Path

    @classmethod
    def create(cls, project_root: Path, target_root: Path) -> "ProjectPaths":
        project_root = project_root.resolve()
        target_root = _ensure_within_root((project_root / target_root).resolve(), project_root)
        sessions_root = _ensure_within_root(
            (project_root / CONFIG_DIR_NAME / ".sessions").resolve(),
            project_root,
        )
        return cls(
            project_root=project_root,
            target_root=target_root,
            sessions_root=sessions_root,
        )

    def ensure_directories(self) -> None:
        self.target_root.mkdir(parents=True, exist_ok=True)
        self.sessions_root.mkdir(parents=True, exist_ok=True)

    def target_for_slot(self, slot: str, extension: str = ".png") -> Path:
        return self.target_root / f"{slot}{extension}"

    def session_dir(self, slot: str, session_id: str) -> Path:
        safe_slot = _validate_slug(slot)
        session_dir = self.sessions_root / f"{safe_slot}_{session_id}"
        return _ensure_within_root(session_dir.resolve(), self.project_root)

    def iter_session_dirs(self) -> Iterator[Tuple[str, Path]]:
        if not self.sessions_root.exists():
            return iter(())
        for item in sorted(self.sessions_root.iterdir()):
            if not item.is_dir():
                continue
            match = _SLOT_SESSION_PATTERN.match(item.name)
            if not match:
                continue
            slot = match.group("slot")
            yield slot, item

    def manifest_path(self, session_dir: Path) -> Path:
        return session_dir / "session.json"


def _validate_slug(value: str) -> str:
    if not re.fullmatch(r"[a-z0-9_-]+", value):
        raise ValueError(f"Invalid slot id '{value}'. Use lowercase letters, numbers, '-', '_' only.")
    return value


def _ensure_within_root(path: Path, root: Path) -> Path:
    resolved_path = path.resolve()
    resolved_root = root.resolve()
    if not resolved_path.is_relative_to(resolved_root):
        raise InvalidPathError(f"Path {resolved_path} escapes root {resolved_root}")
    return resolved_path


def write_manifest(manifest: SessionManifest, manifest_path: Path) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open("w", encoding="utf-8") as fh:
        json.dump(manifest.to_dict(), fh, indent=2)
        fh.write("\n")


def load_manifest(manifest_path: Path) -> SessionManifest:
    with manifest_path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    return SessionManifest.from_dict(data)


def list_manifests_for_slot(paths: ProjectPaths, slot: str) -> List[SessionManifest]:
    manifests: List[SessionManifest] = []
    safe_slot = _validate_slug(slot)
    if not paths.sessions_root.exists():
        return manifests
    for dir_path in sorted(paths.sessions_root.glob(f"{safe_slot}_*")):
        manifest_path = paths.manifest_path(dir_path)
        if manifest_path.exists():
            manifests.append(load_manifest(manifest_path))
    return manifests


def list_all_slots(paths: ProjectPaths) -> Dict[str, List[SessionManifest]]:
    result: Dict[str, List[SessionManifest]] = {}
    if not paths.sessions_root.exists():
        return result
    for slot, session_dir in paths.iter_session_dirs():
        manifest_path = paths.manifest_path(session_dir)
        if not manifest_path.exists():
            continue
        manifest = load_manifest(manifest_path)
        key = manifest.slot or slot
        result.setdefault(key, []).append(manifest)
    return result


def most_recent_session(manifests: Iterable[SessionManifest]) -> Optional[SessionManifest]:
    latest: Optional[SessionManifest] = None
    for manifest in manifests:
        if latest is None or manifest.completed_at > latest.completed_at:
            latest = manifest
    return latest


__all__ = [
    "ProjectPaths",
    "InvalidPathError",
    "write_manifest",
    "load_manifest",
    "list_manifests_for_slot",
    "list_all_slots",
    "most_recent_session",
]
