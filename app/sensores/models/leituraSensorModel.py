from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from utils.database import Base
from sqlalchemy.sql import func

class LeituraSensorModel(Base):
    __tablename__ = 'leitura_sensor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sensor_id = Column("sensor_id", Integer, ForeignKey("sensor.id"))
    data_ocorrencia = Column(DateTime(timezone=True), default=func.now())
    valor = Column(Float)

    sensor = relationship("SensorModel", back_populates="leituras")
