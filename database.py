from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine('postgresql://admin:admin@127.0.0.1:5432/pet_store')

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()

def get_db():
    database: Session = SessionLocal()
    try: 
        yield database
    finally: 
        database.close()

