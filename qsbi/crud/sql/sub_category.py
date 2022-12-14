from typing import Tuple  # noqa: F401
from qsbi.backend.sql.models.sub_category import SubCategory as Model
from qsbi.api.schemas.sub_category import SubCategory as Schema
from qsbi.api.schemas.sub_category import SubCategoryCreate as Create
from qsbi.api.schemas.sub_category import SubCategoryRead as Read
from qsbi.api.schemas.sub_category import SubCategoryUpdate as Update
from qsbi.api.schemas.sub_category import SubCategoryDelete as Delete

from .base import SQLCRUDBase


class SQLCRUDSubCategory(SQLCRUDBase[Model, Schema, Create, Update, Read, Delete]):
    ...


sql_crud_sub_category = SQLCRUDSubCategory(Model, Schema, Create, Update, Read, Delete)
