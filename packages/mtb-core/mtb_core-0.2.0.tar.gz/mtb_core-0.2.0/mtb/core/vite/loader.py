"""Basic module wrapper around vite."""

import json
import textwrap
from typing import TYPE_CHECKING, ClassVar
from urllib.parse import urljoin

from .shared import log

if TYPE_CHECKING:
    from .settings import ViteSettings


class ViteLoader:
    """Manages vite settings."""

    instance = None
    manifest: ClassVar[dict]

    def __new__(cls, settings: "ViteSettings"):
        """Singleton manifest loader."""
        if cls.instance is not None:
            log.info("Reusing instance")
            return cls.instance
        cls.manifest = {}
        cls.instance = super().__new__(cls)
        cls.settings = settings
        cls.instance.parse_manifest()

        return cls.instance

    def parse_manifest(self) -> None:
        """
        Read and parse the Vite manifest file.

        Raises
        ------
            RuntimeError: if cannot load the file or JSON in file is malformed.
        """
        if self.settings.hot_reload:
            log.info("Using hot reload mode. Skipping manifest parsing.")
            return

    def load_manifest(self):
        """Load manifest."""
        if self.settings.manifest_path.exists():
            with self.settings.manifest_path.open("r") as manifest_file:
                manifest_content = manifest_file.read()
            try:
                ViteLoader.manifest = json.loads(manifest_content)
            except Exception as e:
                raise RuntimeError(
                    f"Cannot read Vite manifest file at {self.settings.manifest_path}"
                ) from e

    def generate_vite_server_url(self, path: str | None = None) -> str:
        """
        Generate an URL to and asset served by the Vite development server.

        Keyword Arguments:
            path {Optional[str]} -- Path to the asset. (default: {None})

        Returns
        -------
            str -- Full URL to the asset.
        """
        base_path = f"{self.settings.server_protocol}://{self.settings.server_host}:{self.settings.server_port}"
        return urljoin(
            base_path,
            urljoin(self.settings.static_url, path if path is not None else ""),
        )

    def generate_script_tag(self, src: str, attrs: dict[str, str] | None = None) -> str:
        """Generate an HTML script tag."""
        attrs_str = ""
        if attrs is not None:
            attrs_str = " ".join([f'{key}="{value}"' for key, value in attrs.items()])

        return f'<script {attrs_str} src="{src}"></script>'

    def generate_stylesheet_tag(self, href: str) -> str:
        """
        Generate and HTML <link> stylesheet tag for CSS.

        Arguments:
            href {str} -- CSS file URL.

        Returns
        -------
            str -- CSS link tag.
        """
        return f'<link rel="stylesheet" href="{href}" />'

    def generate_vite_ws_client(self) -> str:
        """
        Generate the script tag for the Vite WS client for HMR.

        Only used in development, in production this method returns
        an empty string.

        Returns
        -------
            str -- The script tag or an empty string.
        """
        if not self.settings.hot_reload:
            return ""

        return self.generate_script_tag(
            self.generate_vite_server_url("@vite/client"),
            {"type": "module"},
        )

    def generate_vite_react_hmr(self) -> str:
        """
        Generate the script tag for the Vite WS client for HMR.

        Only used in development, in production this method returns
        an empty string.

        Returns
        -------
            str -- The script tag or an empty string.
        """
        if self.settings.is_react and self.settings.hot_reload:
            return f"""
                <script type="module">
                import RefreshRuntime from '{self.generate_vite_server_url()}@react-refresh'
                RefreshRuntime.injectIntoGlobalHook(window)
                window.$RefreshReg$ = () => {{}}
                window.$RefreshSig$ = () => (type) => type
                window.__vite_plugin_react_preamble_installed__=true
                </script>
                """
        return ""

    def generate_vite_asset(self, path: str, scripts_attrs: dict[str, str] | None = None) -> str:
        """
        Generate all assets include tags for the file in argument.

        Returns
        -------
            str -- All tags to import this asset in yout HTML page.
        """
        if self.settings.hot_reload:
            return self.generate_script_tag(
                self.generate_vite_server_url(path),
                {"type": "module", "async": "", "defer": ""},
            )
        if not self.manifest:
            self.load_manifest()

        if path not in self.manifest:
            import rich

            rich.print(self.manifest)
            raise RuntimeError(
                textwrap.dedent(f"""
                Cannot find {path} in Vite manifest at {self.settings.manifest_path}
                """)
            )

        tags = []
        manifest_entry: dict = self.manifest[path]
        if not scripts_attrs:
            scripts_attrs = {"type": "module", "async": "", "defer": ""}

        # Add dependent CSS
        if "css" in manifest_entry:
            for css_path in manifest_entry.get("css", []):
                tags.append(
                    self.generate_stylesheet_tag(urljoin(self.settings.static_url, css_path))
                )

        # Add dependent "vendor"
        if "imports" in manifest_entry:
            for vendor_path in manifest_entry.get("imports", []):
                tags.append(self.generate_vite_asset(vendor_path, scripts_attrs=scripts_attrs))

        # Add the script by itself
        tags.append(
            self.generate_script_tag(
                urljoin(self.settings.static_url, manifest_entry["file"]),
                attrs=scripts_attrs,
            )
        )

        return "\n".join(tags)
