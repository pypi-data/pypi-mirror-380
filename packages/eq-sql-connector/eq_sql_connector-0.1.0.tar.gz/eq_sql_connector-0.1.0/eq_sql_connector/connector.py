import json
import logging
import struct
from abc import ABC
from types import SimpleNamespace
from typing import Optional

import pandas as pd
import pyodbc
from msal_bearer import Authenticator, get_user_name
from sqlalchemy import URL, Engine, QueuePool, create_engine, text, bindparam

logger = logging.getLogger(__name__)


def get_object_from_json(text: str):
    if isinstance(text, list):
        obj = [json.loads(x, object_hook=lambda d: SimpleNamespace(**d)) for x in text]
    else:
        obj = json.loads(text, object_hook=lambda d: SimpleNamespace(**d))
    return obj


def get_sql_driver() -> str:
    """Get name of ODBC SQL driver

    Raises:
        ValueError: Raised if required ODBC driver is not installed.

    Returns:
        str: ODBC driver name
    """

    drivers = pyodbc.drivers()

    for driver in drivers:
        if "18" in driver and "SQL Server" in driver:
            return driver

    for driver in drivers:
        if "17" in driver and "SQL Server" in driver:
            return driver

    raise ValueError("ODBC driver 17 or 18 for SQL server is required.")


def get_connection_string(
    server: str, database: str, driver: str = get_sql_driver()
) -> str:
    """Build database connection string

    Args:
        server (str): Server url
        database (str): Database name
        driver (str): ODBC driver name. Defaults to get_sql_driver().

    Returns:
        str: Database connection string
    """
    return f"DRIVER={driver};SERVER={server};DATABASE={database};"


_eq_tenant_id = "3aa4a235-b6e2-48d5-9195-7fcf05b459b0"
_clientID = "9ed0d36d-1034-475a-bdce-fa7b774473fb"  # pdm-tools works for all :)
_scopes = ["https://database.windows.net/.default"]


class Connector(ABC):
    def __init__(
        self,
        authenticator: Optional[Authenticator] = None,
        url_prod: Optional[str] = None,
        url_dev: Optional[str] = None,
    ) -> None:
        self._use_dev = False
        if url_dev is not None:
            self._url_dev = url_dev
            self.set_use_dev(True)
        else:
            self._url_dev = ""

        if url_prod is not None:
            self._url_prod = url_prod
            self.set_use_dev(False)
        else:
            self._url_prod = ""

        if authenticator is None:
            authenticator = Authenticator(
                tenant_id=_eq_tenant_id,
                client_id=_clientID,
                scopes=_scopes,
                user_name=f"{get_user_name()}@equinor.com",
            )
        self.set_Authenticator(authenticator=authenticator)

    def set_url_prod(self, url: str) -> None:
        """Setter for property _url_prod.

        Args:
            url (str): URL to set.
        """
        self._url_prod = url

    def set_url_dev(self, url: str) -> None:
        """Setter for property _url_dev.

        Args:
            url (str): URL to set.
        """
        self._url_dev = url

    def set_use_dev(self, use_dev: bool):
        """Setter for global property _use_dev.
        If _use_dev is True, the API URL will be set to the development URL,
        otherwise it will be set to the production URL.

        Args:
            use_dev (bool): Value to set _use_dev to.

        Raises:
            TypeError: In case input use_dev is not a boolean.
        """
        if not isinstance(use_dev, bool):
            raise TypeError("Input use_dev shall be boolean.")

        self._use_dev = use_dev

    def get_url(self) -> str:
        """Getter for URL. Will return the dev URL if _use_dev is True, otherwise will return the production URL.
        Returns:
            str: API URL
        """
        if self._use_dev:
            return self._url_dev
        else:
            return self._url_prod

    def set_Authenticator(self, authenticator: Authenticator) -> None:
        """Setter for property authenticator.

        Args:
            authenticator (Authenticator): Authenticator to set.
        """
        if not isinstance(authenticator, Authenticator):
            raise TypeError("Input authenticator shall be of type Authenticator.")

        self.authenticator = authenticator


class DBConnector(Connector):
    def __init__(
        self,
        database,
        authenticator: Optional[Authenticator] = None,
        url_prod: Optional[str] = None,
        url_dev: Optional[str] = None,
    ) -> None:
        super().__init__(
            authenticator=authenticator, url_prod=url_prod, url_dev=url_dev
        )

        self.Engine = None
        self.conn_string = get_connection_string(
            server=self.get_url(), database=database
        )

    def query(
        self,
        sql: str,
        params: Optional[dict] = None,
    ) -> pd.DataFrame:
        """Query SQL database using pd.read_sql

        Args:
            sql (str): SQL query for database
            connection (Optional[Connection], optional): Database Connection object. Defaults to None, which resolves to get_connection().
            params (Optional[dict], optional): SQL parameters. Defaults to None.

        Returns:
            pd.DataFrame: Result from pd.read_sql
        """

        # Format SQL query and parameters
        if isinstance(params, dict) and "param" in params:
            pass
        else:
            params = {"param": params}

        sql_clause = text(sql)
        sql_clause = sql_clause.bindparams(bindparam("param", expanding=True))

        return pd.read_sql(sql_clause, self.get_engine(), params=params)

    def reset_engine(self) -> None:
        """Reset cached Engine"""

        if self.Engine is not None:
            self.Engine.dispose()
            self.Engine = None

    def get_engine(self, conn_string="", token="", reset=False) -> Engine:
        """Getter of cached Engine. Will create one if not existing.

        Args:
            conn_string (str, optional): Connection string for odbc connection. Defaults to "" to support just getting cached engine.
            token (str, optional): Token string. Defaults to "" to support just getting cached engine.
            reset (bool, optional): Set true to reset engine, i.e., not get cached engine. Defaults to False.
        """

        def get_token_struct(token: str) -> bytes:
            """Convert token string to token byte struct for use in connection string

            Args:
                token (str): Token as string

            Returns:
                (bytes): Token as bytes
            """
            tokenb = bytes(token, "UTF-8")
            exptoken = b""
            for i in tokenb:
                exptoken += bytes({i})
                exptoken += bytes(1)

            tokenstruct = struct.pack("=i", len(exptoken)) + exptoken

            return tokenstruct

        if conn_string is None or conn_string == "":
            conn_string = self.conn_string

        if not conn_string == self.conn_string:
            reset = True

        if token == "":
            token = self.authenticator.get_token()

        if reset:
            self.reset_engine()

        if self.Engine is None:
            if not isinstance(conn_string, str) and len(conn_string) > 0:
                raise TypeError("Not able to create engine without connection string.")
            SQL_COPT_SS_ACCESS_TOKEN = 1256
            self.Engine = create_engine(
                URL.create("mssql+pyodbc", query={"odbc_connect": conn_string}),
                connect_args={
                    "attrs_before": {SQL_COPT_SS_ACCESS_TOKEN: get_token_struct(token)},
                    "timeout": 60,
                },
                poolclass=QueuePool,
                pool_size=10,
                max_overflow=5,
                pool_timeout=30,
                pool_recycle=1800,
                query_cache_size=1200,
            )

        return self.Engine
