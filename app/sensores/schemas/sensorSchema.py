from datetime import datetime
from pydantic import BaseModel, Field, Json
from typing import List, Optional


class SensorResponse(BaseModel):
    id: int
    ip: str
    logitude: float
    latitude: float
    address: str
    city: str
    nome: str
    active: bool
    distance_layer: Optional[dict]

    class Config:
        from_attributes = True


class SensorResponseLastDistance(BaseModel):
    id: int
    ip: str
    nome: str
    address: str
    city: str
    logitude: float
    latitude: float
    active: bool
    distance_layer: Optional[dict]
    color_icon: str
    last_distance: float
    data_ocorrencia: datetime

    class Config:
        from_attributes = True


class SensorPagination(BaseModel):
    items: List[SensorResponse]


class SensorPaginationMaps(BaseModel):
    items: List[SensorResponseLastDistance]


class SensorRequest(BaseModel):
    ip: str = Field(...)
    address: str = Field(...)
    city: str = Field(...)
    nome: str = Field(...)
    active: Optional[bool]


class SensorRequestPatch(BaseModel):
    baixo: Optional[float]
    medio: Optional[float]
    alta: Optional[float]
