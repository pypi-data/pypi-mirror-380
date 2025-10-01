# Copyright (c) 2024 Everypin
# GNU General Public License v3.0 (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import annotations

from logging import getLogger
from pathlib import Path

import tomli
import tomli_w
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from hardpy.common.singleton import SingletonMeta

logger = getLogger(__name__)


class DatabaseConfig(BaseModel):
    """Database configuration."""

    model_config = ConfigDict(extra="forbid")

    user: str = "dev"
    password: str = "dev"
    host: str = "localhost"
    port: int = 5984
    doc_id: str = Field(exclude=True, default="")
    url: str = Field(exclude=True, default="")

    def model_post_init(self, __context) -> None:  # noqa: ANN001,PYI063
        """Get database connection url."""
        self.url = self.get_url()

    def get_url(self) -> str:
        """Get database connection url.

        Returns:
            str: database connection url
        """
        credentials = f"{self.user}:{self.password}"
        uri = f"{self.host}:{self.port!s}"
        return f"http://{credentials}@{uri}/"


class FrontendConfig(BaseModel):
    """Frontend configuration."""

    model_config = ConfigDict(extra="forbid")

    host: str = "localhost"
    port: int = 8000
    language: str = "en"


class StandCloudConfig(BaseModel):
    """StandCloud configuration."""

    model_config = ConfigDict(extra="forbid")

    address: str = ""
    connection_only: bool = False


class HardpyConfig(BaseModel, extra="allow"):
    """HardPy configuration."""

    model_config = ConfigDict(extra="forbid")

    title: str = "HardPy TOML config"
    tests_name: str = ""
    database: DatabaseConfig = DatabaseConfig()
    frontend: FrontendConfig = FrontendConfig()
    stand_cloud: StandCloudConfig = StandCloudConfig()

    def model_post_init(self, __context) -> None:  # noqa: ANN001,PYI063
        """Get database document name."""
        self.database.doc_id = self.get_doc_id()

    def get_doc_id(self) -> str:
        """Update database document name."""
        return f"{self.frontend.host}_{self.frontend.port}"


class ConfigManager(metaclass=SingletonMeta):
    """HardPy configuration manager."""

    def __init__(self) -> None:
        self._config = HardpyConfig()
        self._test_path = Path.cwd()

    @property
    def config(self) -> HardpyConfig:
        """Get HardPy configuration.

        Returns:
            HardpyConfig: HardPy configuration
        """
        return self._config

    @property
    def tests_path(self) -> Path:
        """Get tests path.

        Returns:
            Path: HardPy tests path
        """
        return self._tests_path

    def init_config(  # noqa: PLR0913
        self,
        tests_name: str,
        database_user: str,
        database_password: str,
        database_host: str,
        database_port: int,
        frontend_host: str,
        frontend_port: int,
        frontend_language: str,
        sc_address: str = "",
        sc_connection_only: bool = False,
    ) -> None:
        """Initialize the HardPy configuration.

        Only call once to create a configuration.

        Args:
            tests_name (str): Tests suite name.
            database_user (str): Database user name.
            database_password (str): Database password.
            database_host (str): Database host.
            database_port (int): Database port.
            frontend_host (str): Operator panel host.
            frontend_port (int): Operator panel port.
            frontend_language (str): Operator panel language.
            sc_address (str): StandCloud address.
            sc_connection_only (bool): StandCloud check availability.
        """
        self._config.tests_name = tests_name
        self._config.frontend.host = frontend_host
        self._config.frontend.port = frontend_port
        self._config.frontend.language = frontend_language
        self._config.database.user = database_user
        self._config.database.password = database_password
        self._config.database.host = database_host
        self._config.database.port = database_port
        self._config.database.doc_id = self._config.get_doc_id()
        self._config.database.url = self._config.database.get_url()
        self._config.stand_cloud.address = sc_address
        self._config.stand_cloud.connection_only = sc_connection_only

    def create_config(self, parent_dir: Path) -> None:
        """Create HardPy configuration.

        Args:
            parent_dir (Path): Configuration file parent directory.
        """
        config = self._config
        if not self._config.stand_cloud.address:
            del config.stand_cloud
        if not self._config.tests_name:
            del config.tests_name
        if not self._config.database.doc_id:
            del config.database.doc_id
        config_str = tomli_w.dumps(config.model_dump())
        with Path.open(parent_dir / "hardpy.toml", "w") as file:
            file.write(config_str)

    def read_config(self, toml_path: Path) -> HardpyConfig | None:
        """Read HardPy configuration.

        Args:
            toml_path (Path): hardpy.toml file path.

        Returns:
            HardpyConfig | None: HardPy configuration
        """
        self._tests_path = toml_path
        toml_file = toml_path / "hardpy.toml"
        if not toml_file.exists():
            return None
        try:
            with Path.open(toml_path / "hardpy.toml", "rb") as f:
                toml_data = tomli.load(f)
        except tomli.TOMLDecodeError as exc:
            msg = f"Error parsing TOML: {exc}"
            logger.exception(msg)
            return None

        try:
            self._config = HardpyConfig(**toml_data)
        except ValidationError:
            logger.exception("Error parsing TOML")
            return None
        return self._config
