from typing import Generic, TypeVar, Type, Dict, Any, Optional, List, Union, ClassVar
from pydantic import BaseModel
from sqlalchemy import and_, select, func

from qsbi.backend.sql.models.base import Base
from qsbi.api.crud.session import CRUDSession

ModelType = TypeVar('ModelType', bound=Base)
SchemaType = TypeVar('SchemaType', bound=BaseModel)
SchemaDictType = TypeVar('SchemaDictType', bound=BaseModel)
SchemaCreateType = TypeVar('SchemaCreateType', bound=BaseModel)
SchemaReadType = TypeVar('SchemaReadType', bound=BaseModel)
SchemaUpdateType = TypeVar('SchemaUpdateType', bound=BaseModel)
SchemaDeleteType = TypeVar('SchemaDeleteType', bound=BaseModel)

class SQLCRUDBase(Generic[ModelType,
                          SchemaType,
                          SchemaDictType,
                          SchemaCreateType,
                          SchemaReadType,
                          SchemaUpdateType,
                          SchemaDeleteType]):

    schema_dict: ClassVar[dict] = {}
    
    def __init__(self,
                 model: Type[ModelType],
                 schema: Type[SchemaType],
                 schema_dict_t: Type[SchemaDictType],
                 schema_create_t: Type[SchemaCreateType],
                 schema_read_t: Type[SchemaReadType],
                 schema_update_t: Type[SchemaUpdateType],
                 schema_delete_t: Type[SchemaDeleteType]):
        self.model = model
        self.schema = schema
        self.schema_dict_t = schema_dict_t
        self.schema_create_t = schema_create_t
        self.schema_read_t   = schema_read_t
        self.schema_update_t = schema_update_t
        self.schema_delete_t = schema_delete_t
        self.schema_dict[schema.__qualname__] = self

    # internal methods, use generic SchemeType
    # public CRUD methods enforce type hints
    async def _read_or_create(self, sess: CRUDSession, obj_in: SchemaType, auto_create: bool = False) -> ModelType:
        db_obj = await self._read(sess, obj_in)
        if not db_obj and auto_create:
            db_obj = await self._create(sess, obj_in)
        return db_obj
    
    async def _read(self, sess: CRUDSession, obj_in: SchemaType) -> Optional[ModelType]:
        # search for object and returns first occurence, if any
        obj_list = await self._search(sess, obj_in)
        try:
            obj = obj_list[0]
        except IndexError:
            obj = None
        return obj

    async def _schem2model_dict(self, sess: CRUDSession, obj_in: SchemaType, exclude_unset: bool = False, auto_create: bool = False) -> Dict:
        dict = obj_in.dict(exclude_unset=exclude_unset)
        # not needed in simplified setup
        # all schemas uses only id references
        # for k in dict:
        #     v = getattr(obj_in,k)
        #     if isinstance(v, BaseModel):
        #         creator = self.schema_dict[v.__class__.__qualname__]
        #         dict[k]=await creator._read_or_create(sess,v,auto_create)
        return dict

    async def _search(self, sess: CRUDSession, obj_in: SchemaType, limit: Optional[int] = None) -> List[ModelType]:
        obj_dict = await self._schem2model_dict(sess, obj_in, exclude_unset=True, auto_create=False)
        filters = list(map(lambda a: getattr(self.model, a) == obj_dict[a], obj_dict))
        query = select(self.model).filter(and_(*filters))
        if limit:
            query = query.limit(limit)
        result = await sess.db.execute(query)
        return result.scalars().all()

    async def _create(self, sess: CRUDSession, obj_in: SchemaType) -> ModelType:
        obj_in_data = await self._schem2model_dict(sess, obj_in, auto_create=True)
        #import pdb; pdb.set_trace()
        db_obj = self.model(**obj_in_data)
        sess.db.add(db_obj)
        await sess.db.commit()
        await sess.db.refresh(db_obj)
        return db_obj

    async def _delete(self, sess: CRUDSession, obj_in: SchemaType) -> Optional[Dict]:
        #import pdb; pdb.set_trace()
        db_obj = await self._read(sess, obj_in)
        result = None
        if db_obj:
            result = db_obj.as_dict()
            await sess.db.delete(db_obj)
            await sess.db.commit()
        return result

    async def _update(self, sess: CRUDSession, obj_in: SchemaType) -> Optional[ModelType]:
        #import pdb; pdb.set_trace()
        db_obj = await self._read(sess, obj_in)
        if db_obj:
            update_data = await self._schem2model_dict(sess, obj_in, exclude_unset=True, auto_create=True)
            for k in update_data:
                setattr(db_obj, k, update_data[k])
            sess.db.add(db_obj)
            await sess.db.commit()
            await sess.db.refresh(db_obj)
        return db_obj
        

    # public CRUD methods / type hints, only schema visible from there
    # we assume ModelType can directly be 'casted' into SchemaType
    async def get_by(self, sess: CRUDSession, attr: str, val: Any) -> Optional[ModelType]:
        query = select(self.model).filter(getattr(self.model,attr) == val)
        result = await sess.db.execute(query)
        return result.scalars().first()

    async def list(self, sess: CRUDSession, skip: int=0, limit: int=100) -> List[SchemaType]:
        query = select(self.model).offset(skip).limit(limit)
        result = await sess.db.execute(query)
        return result.scalars().all()

    async def create(self, sess: CRUDSession, obj_in: SchemaCreateType) -> SchemaType:
        result = await self._create(sess, obj_in)
        return result

    async def search(self, sess: CRUDSession, obj_in: SchemaCreateType, limit: int=100) -> List[SchemaType]:
        result = await self._search(sess, obj_in, limit)
        return result

    async def update(self, sess: CRUDSession, obj_in: SchemaUpdateType) -> Optional[SchemaType]:
        result = await self._update(sess, obj_in)
        return result

    async def delete(self, sess: CRUDSession, obj_in: SchemaDeleteType) -> Optional[SchemaDictType]:
        result = await self._delete(sess, obj_in)
        return result

    async def count(self, sess: CRUDSession) -> int:
        query = select(func.count(self.model.id))
        result = await sess.db.execute(query)
        return result.scalar_one()


