from typing import Tuple
from qsbi.backend.sql.models.party import Party as Model
from qsbi.api.schemas.party import Party as Schema
from qsbi.api.schemas.party import PartyCreate as Create
from qsbi.api.schemas.party import PartyRead as Read
from qsbi.api.schemas.party import PartyUpdate as Update
from qsbi.api.schemas.party import PartyDelete as Delete

from .base import SQLCRUDBase

class SQLCRUDParty(SQLCRUDBase[Model, Schema, Create, Update, Read, Delete]):
    def _fields_filter(self) -> Tuple:
        return ('id','name')

sql_crud_party = SQLCRUDParty(Model, Schema, Create, Update, Read, Delete)
