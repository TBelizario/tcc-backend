from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.sensores.controller.sensorController import sensorController
from app.sensores.schemas.sensorSchema import (SensorPagination, SensorPaginationMaps,
                                               SensorRequest, SensorRequestPatch,
                                               SensorResponse, SensorResponseLastDistance)
from utils.dependencies import get_db


router = APIRouter(prefix="/sensores", tags=["Sensores"])


@router.get("/", response_model=SensorPagination, status_code=200)
def list(db: Session = Depends(get_db)):
    sensor = sensorController(db=db)
    return sensor.list()


@router.get("/maps", response_model=SensorPaginationMaps, status_code=200)
def list_maps(db: Session = Depends(get_db)):
    sensor = sensorController(db=db)
    return sensor.list_maps()


@router.get("/{id}", response_model=SensorResponse, status_code=200)
def list_by_id(id: int, db: Session = Depends(get_db)):
    sensor = sensorController(db=db)
    return sensor.list(id=id)


@router.post("/", response_model=SensorResponse, status_code=201)
def add(request: SensorRequest, db: Session = Depends(get_db)):
    sensor = sensorController(db)
    return sensor.add_sensor(request=request)


@router.put("/{id}", response_model=SensorResponse, status_code=200)
def put(id: int, request: SensorRequest, db: Session = Depends(get_db)):
    sensor = sensorController(db=db)
    return sensor.put(request=request, id=id)


@router.delete("/{id}", status_code=204)
def delete(id: int, db: Session = Depends(get_db)):
    sensor = sensorController(db=db)
    return sensor.delete(id=id)


@router.patch("/{id}", response_model=SensorResponse, status_code=200)
def patch(id: int, request: SensorRequestPatch, db: Session = Depends(get_db)):
    sensor = sensorController(db=db)
    return sensor.patch(request=request, id=id)
