# ruff: noqa: S704 - Unsafe use of `Markup` detected

"""
Generic ViteManager.

Example usage with FastAPI:

```python
from contextlib import asynccontextmanager
from vite_manager import ViteManager
from pathlib import Path

# you can optionally pass settings and custom templates
vite = ViteManager(root=Path("frontend"))

@asynccontextmanager
async def lifespan(_app: FastAPI):
    await vite.start()
    yield
    await vite.stop()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def homepage(request: Request):
    return vite.render(request, "index.html")

```
"""


# from .loader import vite_asset, vite_asset_url, vite_hmr_client


# from .settings import settings

# __version__ = "0.3.2"

# __all__ = ["vite_asset_url", "vite_hmr_client", "vite_asset"]  # , "settings"]

from pathlib import Path
from typing import Annotated, Any

from jinja2 import ChoiceLoader, DictLoader, Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup
from mtb.core import Singleton
from pydantic import BaseModel, Field, WithJsonSchema
from starlette.templating import Jinja2Templates

from .loader import ViteLoader
from .runner import ViteRunner
from .settings import ViteSettings
from .shared import log


class HybridTemplates(Jinja2Templates):
    """Make the starlette jinja2 templates support both memory and disk templates."""

    def __init__(
        self, directory: str | Path, memory_templates: dict[str, str] | None = None, **env_options
    ):
        memory_templates = memory_templates or {}

        fs_loader = FileSystemLoader(str(directory))
        dict_loader = DictLoader(memory_templates)

        # combine loaders
        loader = ChoiceLoader([dict_loader, fs_loader])

        env = Environment(
            loader=loader, autoescape=select_autoescape(["html", "xml"]), **env_options
        )
        super().__init__(env=env)
        # self.env = env


class ViteManager(metaclass=Singleton):
    settings: ViteSettings
    runner: ViteRunner

    def __init__(
        self,
        templates_dir: Path | None = None,
        **kwargs: Annotated[
            Any, Field(alias="settings"), WithJsonSchema(ViteSettings.model_json_schema())
        ],
    ):
        log.info("Initializing ViteManager...")
        self.settings = ViteSettings.model_validate(kwargs)

        log.info(self.settings)

        self.loader = ViteLoader(self.settings)

        if templates_dir is None:
            templates_dir = Path(__file__).parent / "templates"

        templates = HybridTemplates(
            templates_dir,
            {
                "svelte": (Path(__file__).parent / "templates" / "index.html").read_text(
                    encoding="utf8"
                )
            },
        )

        templates.env.globals["vite_hmr_client"] = self.vite_hmr_client
        templates.env.globals["vite_asset"] = self.vite_asset
        templates.env.globals["entrypoint"] = "src/main.ts"

        log.info("Templates patched")

        self._types_to_generate: list[type[BaseModel]] = []
        self.templates = templates
        self.runner = ViteRunner(self.settings)

    def add_types(self, types: list[type[BaseModel]]):
        self._types_to_generate.extend(types)

    async def generate_types(self, *, utility=False):
        if self.settings.typescript_types_file is None:
            if len(self._types_to_generate) > 0:
                log.warning("No path provided for typescript types generation")
                log.warning(f"but you provided {len(self._types_to_generate)} types to generate")
                return
            return

        log.info(f"Found {len(self._types_to_generate)} types to generate")
        log.info(self._types_to_generate)
        res = []
        for t in self._types_to_generate:
            log.info(f"Generating type {t}")
            from mtb.core.codegen import typescript

            res.append(typescript.pydantic_to_ts(t, utility=utility))

        Path(self.settings.typescript_types_file).write_text("\n".join(res))

    @property
    def build(self):
        return self.runner.build

    @property
    def start(self):
        return self.runner.start

    @property
    def stop(self):
        return self.runner.stop

    def vite_hmr_client(self) -> Markup:
        """Generate the script tag for the Vite WS client for HMR.

        Only used in development, in production this method returns
        an empty string.

        If react is enabled,

        Returns
        -------
            str -- The script tag or an empty string.
        """
        tags: list = []
        tags.append(self.loader.generate_vite_react_hmr())
        tags.append(self.loader.generate_vite_ws_client())
        return Markup("\n".join(tags))

    def vite_asset(self, path: str, scripts_attrs: dict[str, str] | None = None) -> Markup:
        """
        Generate all assets include tags for the file in argument.

        Generates all scripts tags for this file and all its dependencies
        (JS and CSS) by reading the manifest file (for production only).
        In development Vite imports all dependencies by itself.
        Place this tag in <head> section of yout page
        (this function marks automaticaly <script> as "async" and "defer").

        Arguments:
            path {str} -- Path to a Vite asset to include.

        Keyword Arguments:
            scripts_attrs {Optional[Dict[str, str]]} -- Override attributes added to scripts tags. (default: {None})
            with_imports {bool} -- If generate assets for dependant assets of this one. (default: {True})

        Returns
        -------
            str -- All tags to import this asset in yout HTML page.
        """
        return Markup(self.loader.generate_vite_asset(path, scripts_attrs=scripts_attrs))

    def vite_asset_url(self, path: str) -> str:
        """
        Generate only the URL of an asset managed by ViteJS.

        Warning, this function does not generate URLs for dependant assets.

        Arguments:
            path {str} -- Path to a Vite asset.

        Returns
        -------
            [type] -- The URL of this asset.
        """
        return self.loader.generate_vite_asset(path)
