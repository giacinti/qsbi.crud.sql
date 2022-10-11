from typing import Tuple  # noqa: F401
from qsbi.backend.sql.models.account import Account as Model
from qsbi.api.schemas.account import Account as Schema
from qsbi.api.schemas.account import AccountCreate as Create
from qsbi.api.schemas.account import AccountRead as Read
from qsbi.api.schemas.account import AccountUpdate as Update
from qsbi.api.schemas.account import AccountDelete as Delete

from .base import SQLCRUDBase


class SQLCRUDAccount(SQLCRUDBase[Model, Schema, Create, Update, Read, Delete]):
    def _fields_filter(self) -> Tuple:
        return ('id', 'name')


sql_crud_account = SQLCRUDAccount(Model, Schema, Create, Update, Read, Delete)
