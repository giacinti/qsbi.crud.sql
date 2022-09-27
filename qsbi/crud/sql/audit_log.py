from qsbi.backend.sql.models.audit_log import AuditLog as Model
from qsbi.api.schemas.audit_log import AuditLog as Schema
from qsbi.api.schemas.audit_log import AuditLogDict as Dict
from qsbi.api.schemas.audit_log import AuditLogCreate as Create
from qsbi.api.schemas.audit_log import AuditLogRead as Read
from qsbi.api.schemas.audit_log import AuditLogUpdate as Update
from qsbi.api.schemas.audit_log import AuditLogDelete as Delete

from .base import SQLCRUDBase

class SQLCRUDAuditLog(SQLCRUDBase[Model, Schema, Dict, Create, Update, Read, Delete]):
    ...


sql_crud_audit_log = SQLCRUDAuditLog(Model, Schema, Dict, Create, Update, Read, Delete)
