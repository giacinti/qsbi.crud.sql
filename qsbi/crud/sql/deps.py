from typing import Generator

from .session import CRUDSession

async def get_session() -> Generator:
    async with CRUDSession() as sess:
        yield sess
