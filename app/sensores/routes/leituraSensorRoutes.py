from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.sensores.controller.leituraSensorController import leituraSensorController
from app.sensores.schemas.leituraSensorSchema import LeituraSensorPaginationResponse, LeituraSensorRequest, LeiturasSensor
from utils.dependencies import get_db


router = APIRouter(prefix="/leitura-sensores", tags=["Leituras Sensores"])


@router.get("/{sensor_id}", response_model=LeituraSensorPaginationResponse, status_code=200)
def list_by_id(sensor_id: int, db: Session = Depends(get_db)):
    leitura = leituraSensorController(db=db)
    return leitura.list_leituras_by_sensor(id=sensor_id)


@router.post("/", response_model=LeiturasSensor, status_code=201)
def add(request: LeituraSensorRequest, db: Session = Depends(get_db)):
    leitura = leituraSensorController(db)
    return leitura.add(request=request)
