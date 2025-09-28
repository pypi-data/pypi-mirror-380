import asyncio
import logging
import os
from asyncio.futures import Future
from asyncio.streams import StreamReader
from asyncio.subprocess import Process
from collections.abc import Coroutine
from typing import TYPE_CHECKING, ClassVar, Optional

from .shared import log

if TYPE_CHECKING:
    from .settings import ViteSettings


class ViteRunner:
    """Vite client utility."""

    _instance: Optional["ViteRunner"] = None
    process: ClassVar[Process]
    logger: logging.Logger = logging.getLogger(__name__)
    future: ClassVar[Future | None] = None
    tasks: ClassVar[set[Coroutine]] = set()
    settings: ClassVar["ViteSettings"]

    def __new__(cls, settings: "ViteSettings"):
        """Singleton loader."""
        if cls._instance is not None:
            log.info("Reusing instance")
            return cls._instance

        cls._instance = super().__new__(cls)
        cls.settings = settings
        cls._env = None
        return cls._instance

    @classmethod
    def get_env(cls):
        if cls._env is None:
            log.info("Setting up vite environment")
            env = os.environ.copy()
            env_overrides = {
                "VITE_WS_URL": "ws://localhost:8000",
                "VITE_ENTRY": os.pathsep.join(cls.settings.entry_point),
                "VITE_STATIC_URL": cls.settings.static_url,
                "VITE_STATIC_PATH": cls.settings.static_path.resolve().as_posix(),
            }
            if cls.settings.deploy_url:
                env_overrides.update({"VITE_WS_URL": cls.settings.deploy_url})

            env.update(env_overrides)
            cls._env = env

        return cls._env

    @classmethod
    async def install(cls):
        """Install dependencies."""
        if cls.settings.npm_skip_install:
            log.info("Skipping installation as npm_skip_install is set")
            return

        log.info("Installing dependencies")
        env = cls.get_env()

        await (
            await asyncio.create_subprocess_shell(
                f"{cls.settings.npm_binary} install",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                restore_signals=True,
                cwd=cls.settings.root.as_posix(),
                env=env,
            )
        ).wait()

    @classmethod
    async def start(cls):
        """
        Create Vite client session object instance.

        Returns
        -------
            Future

        """
        if not (cls.settings.root / "package.json").exists():
            raise FileNotFoundError(f"No package.json found in root directory: {cls.settings.root}")

        await cls.install()
        env = cls.get_env()

        log.info("Running the dev script")
        cls.process = await asyncio.create_subprocess_shell(
            f"{cls.settings.npm_binary} run {cls.settings.npm_dev_script}",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            restore_signals=True,
            cwd=cls.settings.root.as_posix(),
            env=env,
        )
        cls.logger.info("⚡ Starting Vite Asset Service for Live Reload functionality")

        cls.future = asyncio.ensure_future(
            asyncio.gather(
                cls.process.wait(),
                cls._read_from_stdout(stream=cls.process.stdout),
                cls._read_from_stderr(stream=cls.process.stderr),
            ),
        )

        return cls

    @classmethod
    async def stop(cls):
        """Close Redis client."""
        # cls.log.debug("Stopping ViteJS Development Server")
        log.info("⚡ Stopping Vite Asset Service")

        if cls.process:
            try:
                cls.process.terminate()
            except OSError:
                # Ignore 'no such process' error
                cls.logger.debug(
                    "...Process previously terminated. Skipping cleanup.",
                )

    @classmethod
    async def build(cls):
        """
        Create Vite client session object instance.

        Returns
        -------
            Future

        """
        env = cls.get_env()

        await cls.install()

        cls.process = await asyncio.create_subprocess_exec(
            cls.settings.npm_binary,
            "run",
            cls.settings.npm_build_script,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            restore_signals=True,
            cwd=cls.settings.root.as_posix(),
            env=env,
        )
        log.info("⚡ Vite is building application assets")

        cls.future = asyncio.gather(
            asyncio.ensure_future(cls.process.wait()),
            cls._read_from_stdout(stream=cls.process.stdout),
            cls._read_from_stderr(stream=cls.process.stderr),
        )
        return cls

    @classmethod
    async def _read_from_stdout(cls, stream: StreamReader | None):
        if stream:
            while chunk := await stream.readline():
                cls.logger.info(f"{chunk.decode('utf-8').strip()}")

    @classmethod
    async def _read_from_stderr(cls, stream: StreamReader | None):
        if stream:
            while chunk := await stream.readline():
                cls.logger.error(f"{chunk.decode('utf-8').strip()}")
