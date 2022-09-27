from qsbi.backend.sql.models.user import User as Model
from qsbi.api.schemas.user import User as Schema
from qsbi.api.schemas.user import UserDict as Dict
from qsbi.api.schemas.user import UserCreate as Create
from qsbi.api.schemas.user import UserRead as Read
from qsbi.api.schemas.user import UserUpdate as Update
from qsbi.api.schemas.user import UserDelete as Delete

from .base import SQLCRUDBase

class SQLCRUDUser(SQLCRUDBase[Model, Schema, Dict, Create, Update, Read, Delete]):
    ...


sql_crud_user = SQLCRUDUser(Model, Schema, Dict, Create, Update, Read, Delete)
