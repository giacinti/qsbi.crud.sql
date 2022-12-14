from typing import Tuple  # noqa: F401
from qsbi.backend.sql.models.category import Category as Model
from qsbi.api.schemas.category import Category as Schema
from qsbi.api.schemas.category import CategoryCreate as Create
from qsbi.api.schemas.category import CategoryRead as Read
from qsbi.api.schemas.category import CategoryUpdate as Update
from qsbi.api.schemas.category import CategoryDelete as Delete

from .base import SQLCRUDBase


class SQLCRUDCategory(SQLCRUDBase[Model, Schema, Create, Update, Read, Delete]):
    def _fields_filter(self) -> Tuple:
        return ('id', 'name')


sql_crud_category = SQLCRUDCategory(Model, Schema, Create, Update, Read, Delete)
