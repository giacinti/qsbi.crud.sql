from typing import Generic, TypeVar, Type, Dict, Any, Optional, List, Union, ClassVar, Tuple
from pydantic import BaseModel
from sqlalchemy import and_, select, func

from qsbi.backend.sql.models.base import Base
from qsbi.crud.sql.session import SQLCRUDSession

ModelType = TypeVar('ModelType', bound=Base)  # type: ignore
SchemaType = TypeVar('SchemaType', bound=BaseModel)
SchemaCreateType = TypeVar('SchemaCreateType', bound=BaseModel)
SchemaReadType = TypeVar('SchemaReadType', bound=BaseModel)
SchemaUpdateType = TypeVar('SchemaUpdateType', bound=BaseModel)
SchemaDeleteType = TypeVar('SchemaDeleteType', bound=BaseModel)

class SQLCRUDBase(Generic[ModelType,
                          SchemaType,
                          SchemaCreateType,
                          SchemaReadType,
                          SchemaUpdateType,
                          SchemaDeleteType]):

    schema_dict: ClassVar[dict] = {}
    
    def __init__(self,
                 model: Type[ModelType],
                 schema: Type[SchemaType],
                 schema_create_t: Type[SchemaCreateType],
                 schema_read_t: Type[SchemaReadType],
                 schema_update_t: Type[SchemaUpdateType],
                 schema_delete_t: Type[SchemaDeleteType]):
        self.model = model
        self.schema = schema
        self.schema_create_t = schema_create_t
        self.schema_read_t   = schema_read_t
        self.schema_update_t = schema_update_t
        self.schema_delete_t = schema_delete_t
        self.schema_dict[schema.__qualname__] = self

    # internal methods, use generic SchemeType
    # public CRUD methods enforce type hints
    def _fields_filter(self) -> Tuple:
        return ('id',)

    def _filter_obj(self, obj_in: SchemaType) -> Optional[SchemaType]:
        #import pdb; pdb.set_trace()
        obj_out: Optional[SchemaType] = None
        ffilter = self._fields_filter()
        oitems = obj_in.dict(exclude_unset=True).items()
        filtered_dict = { key:value for (key,value) in oitems if key in ffilter }
        # this should not happen - validation should prevent it, but...
        if len(filtered_dict) != 0:
            obj_out = self.schema(**filtered_dict)
        return obj_out
    
    async def _read(self, sess: SQLCRUDSession, obj_in: SchemaType) -> Optional[ModelType]:
        # search for object and returns first occurence, if any
        obj: Optional[ModelType] = None
        obj_search = self._filter_obj(obj_in)
        if obj_search:
            obj_list = await self._search(sess, obj_search, 1) # limit to first one
            try:
                obj = obj_list[0]
            except IndexError:
                obj = None
        return obj

    async def _search(self, sess: SQLCRUDSession, obj_in: SchemaType, limit: Optional[int] = None) -> List[ModelType]:
        obj_dict = obj_in.dict(exclude_unset=True)
        filters = list(map(lambda a: getattr(self.model, a) == obj_dict[a], obj_dict))
        query = select(self.model).filter(and_(*filters))
        if limit:
            query = query.limit(limit)
        result = await sess.db.execute(query)  # type: ignore
        return result.scalars().all()

    async def _create(self, sess: SQLCRUDSession, obj_in: SchemaType) -> ModelType:
        # TODO: check if object already exists
        obj_in_data = obj_in.dict(exclude_unset=False)
        db_obj = self.model(**obj_in_data)
        sess.db.add(db_obj)  # type: ignore
        await sess.db.commit()  # type: ignore
        await sess.db.refresh(db_obj)  # type: ignore
        return db_obj

    async def _delete(self, sess: SQLCRUDSession, obj_in: SchemaType) -> Optional[Dict]:
        db_obj = await self._read(sess, obj_in)
        result = None
        if db_obj:
            result = db_obj.as_dict()
            await sess.db.delete(db_obj)  # type: ignore
            await sess.db.commit()  # type: ignore
        return result

    async def _update(self, sess: SQLCRUDSession, obj_in: SchemaType) -> Optional[ModelType]:
        db_obj = await self._read(sess, obj_in)
        if db_obj:
            update_data = obj_in.dict(exclude_unset=True)
            for k in update_data:
                setattr(db_obj, k, update_data[k])
            sess.db.add(db_obj)  # type: ignore
            await sess.db.commit()  # type: ignore
            await sess.db.refresh(db_obj)  # type: ignore
        return db_obj
        
    def _model_to_schema(self, db_obj: Optional[ModelType]) -> Optional[SchemaType]:
        if db_obj:
            obj_in = self.schema.from_orm(db_obj)
            #import pdb; pdb.set_trace()
            return obj_in  # type: ignore
        else:
            return None

    # public CRUD methods / type hints, only schema visible from there
    async def get_by(self, attr: str, val: Any) -> Optional[SchemaType]:
        ret: Optional[SchemaType] = None
        query = select(self.model).filter(getattr(self.model,attr) == val)
        async with SQLCRUDSession() as sess:
            result = await sess.db.execute(query)  # type: ignore
            ret = self._model_to_schema(result.scalars().first())
        return ret

    async def list(self, skip: int=0, limit: int=100) -> List[Optional[SchemaType]]:
        ret: List[Optional[SchemaType]] = []
        query = select(self.model).offset(skip).limit(limit)
        async with SQLCRUDSession() as sess:
            result = await sess.db.execute(query)  # type: ignore
            ret = list(map(lambda o: self._model_to_schema(o), result.scalars().all()))
        return ret

    async def create(self, obj_c: SchemaCreateType) -> Optional[SchemaType]:
        async with SQLCRUDSession() as sess:
            obj_in = self.schema(**obj_c.dict())
            result = await self._create(sess, obj_in)
            ret = self._model_to_schema(result)
        return ret

    async def search(self, obj_in: SchemaType, limit: int=100) -> List[Optional[SchemaType]]:
        ret: List[Optional[SchemaType]] = []
        async with SQLCRUDSession() as sess:
            result = await self._search(sess, obj_in, limit)
            ret = list(map(lambda o: self._model_to_schema(o), result))
        return ret

    async def update(self, obj_u: SchemaUpdateType) -> Optional[SchemaType]:
        async with SQLCRUDSession() as sess:
            obj_in = self.schema(**obj_u.dict(exclude_unset=True))
            result = await self._update(sess, obj_in)
            ret = self._model_to_schema(result)
        return ret

    async def delete(self, obj_d: SchemaDeleteType) -> Optional[SchemaType]:
        async with SQLCRUDSession() as sess:
            obj_in = self.schema(**obj_d.dict())
            result = await self._delete(sess, obj_in)
            ret = self.schema(**result)  # type: ignore
        return ret

    async def count(self) -> int:
        query = select(func.count(self.model.id))
        async with SQLCRUDSession() as sess:
            result = await sess.db.execute(query)  # type: ignore
            ret = result.scalar_one()
        return ret


