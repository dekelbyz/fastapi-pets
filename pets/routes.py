from fastapi import APIRouter, Depends
from redisdb import init_redis_pool
from pets.services import PetService
from typing import List
from pets.dto import AnimalType, CreatePetDto, GetPetDto, UpdatePetDto
from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Optional
from database import get_db



service = PetService()
router = APIRouter(prefix='/pets', tags=['pets'])


@router.post('/', response_model=GetPetDto, status_code=201)
def create_pet(
    pet: CreatePetDto,
    db: Session = Depends(get_db),
    redis=Depends(init_redis_pool)
):
    try:
        return service.insert_pet(pet=pet, db=db, redis=redis)
    except:
        raise HTTPException(
            status_code=409, detail='this name is already taken.')


@router.get('/', response_model=List[GetPetDto])
def get_all(
        limit: Optional[int] = 100,
        animal_type: Optional[AnimalType] = None,
        db: Session = Depends(get_db)):
    return service.get_all(db, animal_type, limit)


@router.get('/{pet_id}', response_model=GetPetDto)
def get_one(pet_id: int, db: Session = Depends(get_db)):
    try:
        return service.get_one(db, pet_id)
    except:
        raise HTTPException(
            status_code=404, detail='could not find animal with this id.')


@router.delete('/{pet_id}')
def remove_one(
    pet_id, db: Session = Depends(get_db),
    redis: Session = (Depends(init_redis_pool)
                      )):
    pet = get_one(pet_id, db)
    service.remove_one(db, pet_id, redis, pet.name)
    return []


@router.put('/{pet_id}', response_model=GetPetDto)
def update_one(pet_id: int,
               new_pet: UpdatePetDto,
               db: Session = Depends(get_db),
               redis: Session = (Depends(init_redis_pool))
               ):
    old_pet = get_one(pet_id, db)
    return service.update_one(db, old_pet, new_pet, redis)


@router.get('/by_date/{creation_date}', response_model=List[GetPetDto])
def get_by_date(creation_date: str, db: Session = Depends(get_db)):
    return service.get_by_date(date=creation_date, db=db)

@router.get('/added_last_minute/')
def get_pets_added_last_minute(redis: Session = (Depends(init_redis_pool))):
    return service.get_animal_inserted_last_minute(redis=redis)