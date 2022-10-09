from typing import AsyncGenerator

from qsbi.backend.sql.session import async_session

class SQLCRUDSession(object):
    def __init__(self) -> None:
        self.db = async_session()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        if self.db:
            await self.db.close()  # type: ignore


""" async def sql_get_session() -> AsyncGenerator:
    async with SQLCRUDSession() as sess:
        yield sess """

