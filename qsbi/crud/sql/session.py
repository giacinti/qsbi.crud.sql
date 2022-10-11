from qsbi.backend.sql.async_session import async_session


class SQLCRUDSession(object):
    def __init__(self) -> None:
        self.db = async_session()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, exc_tb):
        if self.db:
            await self.db.close()  # type: ignore
