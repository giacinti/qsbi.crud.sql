from dataclasses import dataclass
from typing import ClassVar, Optional, List


@dataclass(frozen=True)
class CRUDModule(object):
    modules_dict: ClassVar[dict] = {}
    name: str
    classname: Optional[str]
    specific: Optional[List[str]] = None

    def __post_init__(self):
        self.modules_dict[self.name] = self

    @classmethod
    def get_module(cls, name: str) -> Optional['CRUDModule']:
        # potentiall raise a KeyError exception
        return cls.modules_dict[name]

    @classmethod
    def get_modules_list(cls, lst) -> List[Optional['CRUDModule']]:
        if not lst:
            lst = cls.modules_dict.values()
        mod_list = list(map(cls.get_module, lst))
        return mod_list
