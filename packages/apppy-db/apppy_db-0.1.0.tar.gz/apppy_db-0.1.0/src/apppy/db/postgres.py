import psycopg
from fastapi_lifespan_manager import LifespanManager
from psycopg.rows import DictRow, dict_row
from psycopg_pool.pool_async import AsyncConnectionPool as DBConnAsyncPool
from pydantic import Field

from apppy.env import EnvSettings
from apppy.logger import WithLogger


class PostgresClientSettings(EnvSettings):
    db_conn: str = Field(alias="APP_POSTGRES_DB_CONN")
    db_host: str = Field(alias="APP_POSTGRES_DB_HOST")
    db_password: str = Field(alias="APP_POSTGRES_DB_PASSWORD", exclude=True)

    db_pool_min_size: int = Field(alias="APP_POSTGRES_DB_POOL_MIN_SIZE", default=4)
    db_pool_max_size: int | None = Field(alias="APP_POSTGRES_DB_POOL_MAX_SIZE", default=None)
    db_pool_timeout: float = Field(alias="APP_POSTGRES_DB_POOL_TIMEOUT", default=30)


class PostgresClient(WithLogger):
    def __init__(self, settings: PostgresClientSettings, lifespan: LifespanManager) -> None:
        self._settings = settings

        self._conninfo: str = (
            f"host={settings.db_host} password={settings.db_password} {settings.db_conn}"
        )
        self._db_pool_async: DBConnAsyncPool | None = None
        lifespan.add(self.__open_db_pool_async)

    async def __open_db_pool_async(self):
        self._logger.info("Opening Postgres psycopg_pool_async")
        if not self._db_pool_async or self._db_pool_async.closed:
            self._db_pool_async = DBConnAsyncPool(
                conninfo=self._conninfo,
                open=False,
                min_size=self._settings.db_pool_min_size,
                max_size=self._settings.db_pool_max_size,
                timeout=self._settings.db_pool_timeout,
            )
            self._logger.info(
                "Opened Postgres psycopg_pool_async",
                extra={
                    "min_size": self._settings.db_pool_min_size,
                    "max_size": self._settings.db_pool_max_size,
                },
            )

        await self._db_pool_async.open(wait=True)
        yield {"db_pool_async": self._db_pool_async}

        self._logger.info("Closing Postgres psycopg_pool_async")
        try:
            await self._db_pool_async.close()
        except Exception:
            self._logger.exception("Error while closing Postgres psycopg_pool_async")

    @property
    def db_pool_async(self) -> DBConnAsyncPool:
        if self._db_pool_async is None:
            raise Exception("Postgres db_pool_async is uninitialized")

        return self._db_pool_async

    async def db_query_async(self, query: str, params: dict | None = None) -> list[DictRow]:
        async with (
            self.db_pool_async.connection() as db_conn,
            psycopg.AsyncClientCursor(db_conn, row_factory=dict_row) as db_cursor_async,
        ):
            await db_cursor_async.execute(query=query, params=params)
            result_set = await db_cursor_async.fetchall()

            return result_set
