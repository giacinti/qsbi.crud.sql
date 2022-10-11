from typing import Tuple  # noqa: F401
from qsbi.backend.sql.models.scheduled import Scheduled as Model
from qsbi.api.schemas.scheduled import Scheduled as Schema
from qsbi.api.schemas.scheduled import ScheduledCreate as Create
from qsbi.api.schemas.scheduled import ScheduledRead as Read
from qsbi.api.schemas.scheduled import ScheduledUpdate as Update
from qsbi.api.schemas.scheduled import ScheduledDelete as Delete

from .base import SQLCRUDBase


class SQLCRUDScheduled(SQLCRUDBase[Model, Schema, Create, Update, Read, Delete]):
    ...


sql_crud_scheduled = SQLCRUDScheduled(Model, Schema, Create, Update, Read, Delete)
