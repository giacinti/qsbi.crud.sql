from typing import Generator

from qsbi.api.crud.session import CRUDSession
from qsbi.backend.sql.session import async_session

class SQLCRUDSession(CRUDSession):
    def __init__(self):
        self.db = async_session()

    async def close(self):
        if self.db:
            await self.db.close()


async def sql_get_session() -> Generator:
    async with SQLCRUDSession() as sess:
        yield sess

