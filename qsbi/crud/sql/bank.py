from typing import Tuple
from qsbi.backend.sql.models.bank import Bank as Model
from qsbi.api.schemas.bank import Bank as Schema
from qsbi.api.schemas.bank import BankDict as Dict
from qsbi.api.schemas.bank import BankCreate as Create
from qsbi.api.schemas.bank import BankRead as Read
from qsbi.api.schemas.bank import BankUpdate as Update
from qsbi.api.schemas.bank import BankDelete as Delete

from .base import SQLCRUDBase

class SQLCRUDBank(SQLCRUDBase[Model, Schema, Dict, Create, Update, Read, Delete]):
    def _fields_filter(self) -> Tuple:
        return ('id','name')

sql_crud_bank = SQLCRUDBank(Model, Schema, Dict, Create, Update, Read, Delete)
