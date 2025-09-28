"""Settings for ViteManager."""

from pathlib import Path
from typing import Literal

from pydantic import Field, ValidationInfo, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


def build_manifest_path(info) -> Path:
    """Build the path to the manifest file based on the settings."""
    # path: Path = info["assets_path"] if info.get("hot_reload") else info["static_path"]
    path = Path(info["static_path"])
    path = path / ".vite" / "manifest.json"

    if not path.exists():
        path = info["root"] / path

    return path


class ViteSettings(BaseSettings):
    """Application settings for Vite."""

    #! --- base settings ---
    root: Path = Field(Path("."), description="The root directory of the application's frontend.")
    entry_point: list[str] = Field(["./src/index.ts"], description="The rollup entry points.")
    default_template: Literal["svelte", "react", "vue"] = Field(
        "svelte",
        description="The default template to render, can be 'svelte', 'react' or 'vue'",
    )

    #! --- NPM settings ---
    npm_binary: str = Field("bun", description="The npm binary to use.")

    @field_validator("npm_binary", mode="before")
    @classmethod
    def find_binary_path(cls, v: str | None, _info: ValidationInfo) -> str:
        """Resolve the binary url."""
        if v:
            from shutil import which

            binary = which(v)
            if binary is None:
                raise ValueError(f"Binary for {v} not found.")
            return binary
        raise ValueError("npm binary cannot be empty")

    npm_build_script: str = Field(
        "build", description="The name of the script to build the frontend"
    )
    npm_dev_script: str = Field("dev", description="The name of the dev script for the frontend")
    npm_skip_install: bool = Field(default=False, description="Skip installation of dependencies")

    #! --- vite specifics ---

    # TODO: implement properly
    # https://vite.dev/config/server-options#server-cors
    # https://github.com/expressjs/cors#configuration-options
    cors: list[str] = Field(
        default=[], description="List of allowed origins for CORS, only used in development"
    )

    deploy_url: str | None = Field(
        None, description="URL to deploy frontend to (can be accessed statically)"
    )

    static_url: str = Field(
        "/static/", description="Route at which you serve your static assets in FastAPI."
    )

    @field_validator("static_url", mode="before")
    @classmethod
    def ensure_slash_for_static_url(cls, v: str | None, _info: ValidationInfo) -> str:
        """Ensure that the static_url ends with a forward slash."""
        if v and v.endswith("/"):
            return v

        return f"{v}/"

    static_path: Path = Field(
        Path("static/vite"), description="The path where vite will output its assets."
    )
    hot_reload: bool = Field(default=True, description="Enable hot reload.")
    is_react: bool = Field(
        default=False, deprecated=True, description="Is the frontend app react based?"
    )

    @field_validator("hot_reload", mode="before")
    @classmethod
    def detect_serve_mode(cls, v: bool | None, info: ValidationInfo) -> bool:
        """Detect serve mode based on the 'hot_reload' value and 'DEBUG' flag in data."""
        if v:
            return v
        elif info.data.get("DEBUG", None):
            return True
        return False

    # NOTE: disabled for now as it adds complexity.
    # assets_path: Path = Path("static/")

    manifest_path: Path = Field(
        default_factory=build_manifest_path, description="Automatically infered"
    )

    #! --- code gen ---
    typescript_types_file: Path | None = Field(
        None, description="If provided types added to the manager will be outputed there."
    )

    #! --- server settings ---
    server_host: str = "localhost"
    server_protocol: str = "http"
    server_port: int = 5173

    #! --- model config ---
    model_config = SettingsConfigDict(
        extra="allow",
        case_sensitive=False,
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="VITE_",
    )


# settings = ViteSettings()
