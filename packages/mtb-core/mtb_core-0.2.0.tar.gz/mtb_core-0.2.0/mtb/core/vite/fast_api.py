"""FastAPI integration for ViteManager."""

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from .manager import ViteManager


class ViteManagerFastAPI(ViteManager):
    """Subclass of the manager for FastAPI."""

    def mount_assets(self, app: FastAPI):
        """Mount the vite assets in FastAPI."""
        app.mount(
            self.settings.static_url,
            StaticFiles(directory=self.settings.static_path.as_posix()),
            name="vite-static",
        )

    def render(self, request: Request, template_name: str | None = None, **kwargs):
        """Render vite templates."""
        if not template_name:
            template_name = self.settings.default_template

        return self.templates.TemplateResponse(request, template_name, context=kwargs)
