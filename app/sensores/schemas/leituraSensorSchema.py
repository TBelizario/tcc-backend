from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class LeiturasSensor(BaseModel):
    data_ocorrencia: datetime
    valor: float


class LeituraSensorPaginationResponse(BaseModel):
    id: int = None
    ip: str = None
    logitude: float = None
    latitude: float = None
    active: bool = None
    items: List[LeiturasSensor]

    class Config:
        from_attributes = True


class LeituraSensorRequest(BaseModel):
    sensor_id: int = Field(...)
    data_ocorrencia: datetime = Field(...)
    valor: float = Field(...)
