from typing import Tuple
from qsbi.backend.sql.models.currency import Currency as Model
from qsbi.api.schemas.currency import Currency as Schema
from qsbi.api.schemas.currency import CurrencyDict as Dict
from qsbi.api.schemas.currency import CurrencyCreate as Create
from qsbi.api.schemas.currency import CurrencyRead as Read
from qsbi.api.schemas.currency import CurrencyUpdate as Update
from qsbi.api.schemas.currency import CurrencyDelete as Delete

from .base import SQLCRUDBase

class SQLCRUDCurrency(SQLCRUDBase[Model, Schema, Dict, Create, Update, Read, Delete]):
    def _fields_filter(self) -> Tuple:
        return ('id','name','nickname','code')

sql_crud_currency = SQLCRUDCurrency(Model, Schema, Dict, Create, Update, Read, Delete)
