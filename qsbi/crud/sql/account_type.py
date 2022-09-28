from typing import Tuple
from qsbi.backend.sql.models.account_type import AccountType as Model
from qsbi.api.schemas.account_type import AccountType as Schema
from qsbi.api.schemas.account_type import AccountTypeDict as Dict
from qsbi.api.schemas.account_type import AccountTypeCreate as Create
from qsbi.api.schemas.account_type import AccountTypeRead as Read
from qsbi.api.schemas.account_type import AccountTypeUpdate as Update
from qsbi.api.schemas.account_type import AccountTypeDelete as Delete

from .base import SQLCRUDBase

class SQLCRUDAccountType(SQLCRUDBase[Model, Schema, Dict, Create, Update, Read, Delete]):
    def _fields_filter(self) -> Tuple:
        return ('id','name')


sql_crud_account_type = SQLCRUDAccountType(Model, Schema, Dict, Create, Update, Read, Delete)
