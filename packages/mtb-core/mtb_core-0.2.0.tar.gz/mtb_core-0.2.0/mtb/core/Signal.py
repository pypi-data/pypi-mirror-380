import logging
import sys
from collections.abc import Iterable

log = logging.getLogger(__name__)


class MtbImportHook:
    """A small import hook that can block imports by prefix.

    By default it blocks imports starting with "mtb." unless explicitly allowed.
    Use install_mtb_import_hook() to insert an instance into sys.meta_path and
    uninstall_mtb_import_hook() to remove it.
    """

    def __init__(
        self,
        block_prefix: str = "mtb.",
        allowlist: Iterable[str] | None = None,
        *,
        enabled: bool = True,
    ):
        self.block_prefix = block_prefix
        self.allowlist = tuple(allowlist or ())
        self.enabled = bool(enabled)

    def find_spec(self, fullname: str, path, target=None):
        if not self.enabled:
            return None
        if fullname.startswith(self.block_prefix):
            for allowed in self.allowlist:
                if fullname.startswith(allowed):
                    return None
            # Block the import with an informative error
            msg = f"Import of '{fullname}' is blocked by MtbImportHook"
            log.warning(msg)
            raise ImportError(msg)
        return None

    def __repr__(self) -> str:
        return (
            f"MtbImportHook(block_prefix={self.block_prefix!r}, "
            f"allowlist={self.allowlist!r}, enabled={self.enabled})"
        )


def install_mtb_import_hook(
    block_prefix: str = "mtb.", allowlist: Iterable[str] | None = None, position: int = 0
) -> MtbImportHook:
    """Install and return a new MtbImportHook instance into sys.meta_path.

    Parameters
    ----------
    block_prefix : str
        Import prefix to block.
    allowlist : Iterable[str] | None
        Prefixes that are exempt from blocking.
    position : int
        Index to insert the hook into sys.meta_path.
    """
    hook = MtbImportHook(block_prefix=block_prefix, allowlist=allowlist)
    sys.meta_path.insert(position, hook)
    log.debug("Installed %s at meta_path position %d", hook, position)
    return hook


def uninstall_mtb_import_hook(hook: MtbImportHook) -> None:
    """Remove a previously installed MtbImportHook from sys.meta_path."""
    try:
        sys.meta_path.remove(hook)
        log.debug("Uninstalled %s", hook)
    except ValueError:
        log.debug("Hook %s was not installed", hook)


if __name__ == "__main__":
    hook = install_mtb_import_hook(block_prefix="mtb.blocked", allowlist=("mtb.allowed",))
    try:
        try:
            pass  # should be blocked
        except Exception as exc:
            print("Import hook blocked import as expected:", exc)
    finally:
        uninstall_mtb_import_hook(hook)
