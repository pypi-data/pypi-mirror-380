from dataclasses import dataclass
from dataclasses import field
from enum import StrEnum
from typing import TYPE_CHECKING

from movslib.model import Row

if TYPE_CHECKING:
    from collections.abc import Iterable


class Tags(StrEnum):
    BONIFICO = 'BONIFICO'
    ELENA = 'ELENA'
    VITO = 'VITO'
    COMMISSIONI = 'COMMISSIONI'
    AUTOSTRADA = 'AUTOSTRADA'
    BOLLETTE = 'BOLLETTE'
    LUCE = 'LUCE'
    GAS = 'GAS'
    TELEFONO = 'TELEFONO'
    CONDOMINIO = 'CONDOMINIO'


@dataclass(frozen=True)
class TagRow(Row):
    tags: set[Tags] = field(default_factory=set)


class TagRows(list[TagRow]):
    def __init__(self, name: str, iterable: 'Iterable[TagRow]' = ()) -> None:
        super().__init__(iterable)
        self.name = name
