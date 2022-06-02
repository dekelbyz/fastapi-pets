
from sqlalchemy import Column, String, DateTime, Integer, func
from database import Base

class Pet(Base):
    __tablename__ = 'pets'
    id = Column(Integer(), primary_key=True)
    name = Column(String(50), unique=True)
    animal_type = Column(String(50))
    created = Column(DateTime(), default=func.now())




