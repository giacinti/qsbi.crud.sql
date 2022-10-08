from typing import Tuple
from qsbi.backend.sql.models.currency_link import CurrencyLink as Model
from qsbi.api.schemas.currency_link import CurrencyLink as Schema
from qsbi.api.schemas.currency_link import CurrencyLinkDict as Dict
from qsbi.api.schemas.currency_link import CurrencyLinkCreate as Create
from qsbi.api.schemas.currency_link import CurrencyLinkRead as Read
from qsbi.api.schemas.currency_link import CurrencyLinkUpdate as Update
from qsbi.api.schemas.currency_link import CurrencyLinkDelete as Delete

from .base import SQLCRUDBase

class SQLCRUDCurrencyLink(SQLCRUDBase[Model, Schema, Dict, Create, Update, Read, Delete]):
    ...

sql_crud_currency_link = SQLCRUDCurrencyLink(Model, Schema, Dict, Create, Update, Read, Delete)
