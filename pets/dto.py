from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AnimalType(str, Enum):
    CAT = 'cat'
    DOG = 'dog'
    HORSE = 'horse'
    COW = 'cow'

class CreatePetDto(BaseModel):
    name: str
    animal_type: AnimalType

class GetPetDto(CreatePetDto):
    id: int
    created: datetime

    class Config:
        orm_mode=True

class UpdatePetDto(BaseModel):
    name: Optional[str]
    animal_type: Optional[AnimalType]

    