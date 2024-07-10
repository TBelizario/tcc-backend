from sqlalchemy import Column, Integer, String, Float, Boolean, JSON
from sqlalchemy.orm import relationship
from utils.database import Base


class SensorModel(Base):
    __tablename__ = 'sensor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(50), unique=True)
    nome = Column(String(256))
    logitude = Column(Float)
    latitude = Column(Float)
    address = Column(String(256))
    city = Column(String(256))
    active = Column(Boolean, default=True)
    distance_layer = Column(JSON, nullable=True)

    leituras = relationship("LeituraSensorModel", back_populates="sensor") 
