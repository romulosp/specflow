"""Cooperative write lock and conservative, journaled consumer transactions."""
from contextlib import contextmanager
from pathlib import Path
import os
import tempfile
import uuid
from .storage import Fault, require, confined, link, portable


def busy(root):
    path = confined(Path(root), ".specflow/write.lock", writing=True)
    require(not path.exists(), "PROJECT_BUSY", 1)


class Transaction:
    def __init__(self, root):
        original = Path(root).absolute()
        require(not link(original), "WRITE_LINK")
        self.root = original.resolve()
        self.token = uuid.uuid4().hex.encode("ascii")
        self.lock = None
        self.entered = False

    def __enter__(self):
        self.root.mkdir(parents=True, exist_ok=True)
        control = confined(self.root, ".specflow", writing=True)
        control.mkdir(exist_ok=True)
        self.lock = confined(self.root, ".specflow/write.lock", writing=True)
        try:
            with self.lock.open("xb") as stream:
                stream.write(self.token)
        except FileExistsError as error:
            raise Fault(1, "PROJECT_BUSY") from error
        except OSError as error:
            raise Fault(2, "LOCK_IO_ERROR") from error
        self.entered = True
        return self

    def __exit__(self, typ, value, trace):
        self.entered = False
        try:
            if self.lock and not link(self.lock) and self.lock.read_bytes() == self.token:
                self.lock.unlink()
            elif typ is None:
                raise Fault(1, "LOCK_OWNERSHIP_CHANGED")
        except OSError as error:
            if typ is None:
                raise Fault(2, "LOCK_RELEASE_FAILED") from error

    def path(self, ref):
        path = confined(self.root, ref, writing=True)
        cursor = self.root
        for part in portable(ref):
            if cursor.is_dir():
                require(not any(p.name != part and p.name.casefold() == part.casefold()
                                for p in cursor.iterdir()), "PATH_CASE_CONFLICT", 1)
            else:
                require(not cursor.exists(), "PATH_PARENT_CONFLICT", 1)
            cursor = cursor / part
        return path

    @staticmethod
    def current(path):
        if not path.exists():
            return None
        require(path.is_file(), "DESTINATION_CONFLICT", 1)
        return path.read_bytes()

    def _replace(self, path, value, expected):
        require(not link(path) and self.current(path) == expected, "WRITE_CONCURRENT", 1)
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".specflow-", delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(value)
                stream.flush()
                os.fsync(stream.fileno())
            require(not link(path) and self.current(path) == expected, "WRITE_CONCURRENT", 1)
            os.replace(temporary, path)
        finally:
            if temporary and temporary.exists():
                temporary.unlink()

    def _write(self, path, value, expected):
        if expected is None:
            with path.open("xb") as stream:
                stream.write(value)
        else:
            self._replace(path, value, expected)

    def reserve(self, ref, value):
        """Control record intentionally survives a later operation rollback."""
        require(self.entered, "WRITE_LOCK_REQUIRED")
        path = self.path(ref)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            with path.open("xb") as stream:
                stream.write(value)
        except FileExistsError as error:
            raise Fault(1, "RESERVATION_CONFLICT") from error

    def apply(self, plan, mutable=()):
        require(self.entered and isinstance(plan, dict), "WRITE_LOCK_REQUIRED")
        require(all(isinstance(k, str) and isinstance(v, bytes) for k, v in plan.items()), "WRITE_DATA_INVALID")
        require(len({p.casefold() for p in plan}) == len(plan), "PATH_DUPLICATE")
        prefixes = {}
        for ref in plan:
            parts = portable(ref)
            for count in range(1, len(parts) + 1):
                prefix = "/".join(parts[:count])
                key = prefix.casefold()
                require(key not in prefixes or prefixes[key] == prefix, "PATH_PLAN_CASE_CONFLICT")
                prefixes[key] = prefix
        keys = set(plan)
        require(not any(ref[:i] in keys for ref in plan for i, char in enumerate(ref) if char == "/"), "PATH_PLAN_CONFLICT")
        paths, before, journal, directories = {}, {}, [], []
        try:
            for ref, data in plan.items():
                path = self.path(ref)
                old = self.current(path)
                require(old is None or old == data or ref in mutable, "CONTENT_CONFLICT", 1)
                paths[ref], before[ref] = path, old
            for ref, value in plan.items():
                if before[ref] == value:
                    continue
                path = self.path(ref)
                require(self.current(path) == before[ref], "WRITE_CONCURRENT", 1)
                missing = []
                parent = path.parent
                while not parent.exists():
                    missing.append(parent)
                    parent = parent.parent
                for folder in reversed(missing):
                    folder.mkdir()
                    directories.append(folder)
                # Journal before writing so partial writes can also be detected/reported.
                journal.append((ref, value, before[ref]))
                self._write(path, value, before[ref])
        except (OSError, Fault) as original:
            partial = False
            for ref, value, previous in reversed(journal):
                try:
                    path = self.path(ref)
                    current = self.current(path)
                    if current == previous:
                        continue
                    if current != value:
                        partial = True
                    elif previous is None:
                        path.unlink()
                    else:
                        self._replace(path, previous, value)
                except (Fault, OSError):
                    partial = True
            for folder in reversed(directories):
                try:
                    folder.rmdir()
                except OSError:
                    partial = True
            if partial:
                raise Fault(2, "WRITE_PARTIAL") from original
            if isinstance(original, Fault):
                raise
            raise Fault(2, "WRITE_IO_ERROR") from original
