from pydantic import BaseModel, Field, Json
from typing import List, Optional


class SensorResponse(BaseModel):
    id: int
    ip: str
    logitude: float
    latitude: float
    active: bool
    distance_layer: Optional[dict]

    class Config:
        from_attributes = True


class SensorResponseLastDistance(BaseModel):
    id: int
    ip: str
    logitude: float
    latitude: float
    active: bool
    distance_layer: Optional[dict]
    color_icon: str
    last_distance: float

    class Config:
        from_attributes = True


class SensorPagination(BaseModel):
    items: List[SensorResponse]


class SensorPaginationMaps(BaseModel):
    items: List[SensorResponseLastDistance]


class SensorRequest(BaseModel):
    ip: str = Field(...)
    logitude: float = Field(...)
    latitude: float = Field(...)
    active: bool = Field(...)
    distance_layer: Optional[dict]


class SensorRequestPatch(BaseModel):
    baixo: Optional[float]
    medio: Optional[float]
    alta: Optional[float]
