from pydantic import BaseModel, ConfigDict, field_validator, PrivateAttr
from sqlmodel import SQLModel, Field
from typing import Literal, Callable, Optional, Any
from datetime import datetime, timezone
from enum import Enum

# class ExternalValueQuery(SQLModel, table=True):
#     external_value_id: str
#     keys: str


class EVType(Enum):
    data = "data"
    resource = "resource"

class ExternalValue(SQLModel, table=True):
    ref: str = Field(default=None, primary_key=True)
    
    # query: dict # same query as was used for fetching the data
    query: str = '{"json_query": "in_stringformat"}'
    value: Optional[str] = None
    kind: str # object kind/type
    ev_type: EVType = Field(default=EVType.data)
    plugin: str


    resolved_at: Optional[datetime] = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    # # Fält som finns i modellen och JSON men inte i databasen
    # cached_value: bool = Field(default=True, sa_column=None, exclude=True)
    
    # Privat attribut för callable (inte i JSON eller databas)
    _callable: Optional[Callable] = PrivateAttr(default=None)
    
    @field_validator('ev_type', mode='before')
    @classmethod
    def validate_ev_type(cls, v):
        if isinstance(v, str):
            return EVType(v)
        return v

