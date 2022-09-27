from qsbi.backend.sql.models.transact import Transact as Model
from qsbi.api.schemas.transact import Transact as Schema
from qsbi.api.schemas.transact import TransactDict as Dict
from qsbi.api.schemas.transact import TransactCreate as Create
from qsbi.api.schemas.transact import TransactRead as Read
from qsbi.api.schemas.transact import TransactUpdate as Update
from qsbi.api.schemas.transact import TransactDelete as Delete

from .base import SQLCRUDBase

class SQLCRUDTransact(SQLCRUDBase[Model, Schema, Dict, Create, Update, Read, Delete]):
    ...


sql_crud_transact = SQLCRUDTransact(Model, Schema, Dict, Create, Update, Read, Delete)
