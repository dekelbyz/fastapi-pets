from pets.dto import CreatePetDto, UpdatePetDto
from pets.model import Pet
from sqlalchemy.orm import Session
from redis import Redis


class PetService:
    def insert_pet(self, pet: CreatePetDto, db: Session, redis: Redis):
        # redis validation wether pet already exists or not.


        animal_exists = redis.sismember('pet_name', pet.name)
        if animal_exists:
            raise

        new_pet = Pet(name=pet.name, animal_type=pet.animal_type)
        db.add(new_pet)
        db.commit()
        redis.sadd(f'pet_name', pet.name)

        redis.setex(f'recently_inserted_pets::{pet.animal_type}::{pet.name}', 60, '1')

        return new_pet

    def get_animal_inserted_last_minute(self, redis: Redis):
        horses = redis.keys('*recently_inserted_pets::horse*')
        cows = redis.keys('*recently_inserted_pets::cow*')
        cats = redis.keys('*recently_inserted_pets::cat*')
        dogs = redis.keys('*recently_inserted_pets::dog*')
        
        counter = {
            'horses': f'{len(horses)}',
            'cows': f'{len(cows)}',
            'cats': f'{len(cats)}',
            'dogs': f'{len(dogs)}'
        }
        return counter

    def get_all(self, db: Session, animal_type, limit):
        if animal_type:
            return db.query(Pet).filter(Pet.animal_type == animal_type).limit(limit).all()
        return db.query(Pet).limit(limit).all()

    def get_one(self, db: Session, id: int):
        return db.query(Pet).filter(Pet.id == id).one()

    def remove_one(self, db: Session, id: int, redis: Redis, pet_name):
        db.query(Pet).filter(Pet.id == id).delete()
        db.commit()
        redis.srem('pet_name', pet_name)

    def update_one(self, db: Session, old_pet: Pet, new_pet: UpdatePetDto, redis: Redis):
        if new_pet.name:
            redis.srem('pet_name', old_pet.name)
            old_pet.name = new_pet.name
            redis.sadd('pet_name', new_pet.name)

        old_pet.animal_type = new_pet.animal_type if new_pet.animal_type else old_pet.animal_type
        db.commit()
        return old_pet

    def get_by_date(self, date, db: Session):
        return db.query(Pet).filter(Pet.created > date).all()
