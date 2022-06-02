from fastapi import FastAPI
from pets.routes import router as pets_router
import database
import uvicorn

app = FastAPI()
app.include_router(pets_router)

if __name__ == "__main__":
    # database.Base.metadata.create_all(bind=database.engine)
    uvicorn.run('server:app', host="127.0.0.1", port=8000, reload=True)