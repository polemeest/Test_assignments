from fastapi import FastAPI
from apps.router import router as apps_router
from utils.database import engine
from apps.lovers.models import Base

app = FastAPI()
app.include_router(apps_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}
