from sqlalchemy import Column, Integer, String, Float, Boolean, JSON
from sqlalchemy.orm import relationship
from utils.database import Base


class SensorModel(Base):
    __tablename__ = 'sensor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(50), unique=True)
    logitude = Column(Float)
    latitude = Column(Float)
    active = Column(Boolean, default=True)
    distance_layer = Column(JSON, nullable=True)

    leituras = relationship("LeituraSensorModel", back_populates="sensor") 
