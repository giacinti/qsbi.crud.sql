from typing import Tuple  # noqa: F401
from qsbi.backend.sql.models.reconcile import Reconcile as Model
from qsbi.api.schemas.reconcile import Reconcile as Schema
from qsbi.api.schemas.reconcile import ReconcileCreate as Create
from qsbi.api.schemas.reconcile import ReconcileRead as Read
from qsbi.api.schemas.reconcile import ReconcileUpdate as Update
from qsbi.api.schemas.reconcile import ReconcileDelete as Delete

from .base import SQLCRUDBase


class SQLCRUDReconcile(SQLCRUDBase[Model, Schema, Create, Update, Read, Delete]):
    ...


sql_crud_reconcile = SQLCRUDReconcile(Model, Schema, Create, Update, Read, Delete)
