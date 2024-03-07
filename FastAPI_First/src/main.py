from fastapi import FastAPI
from apps.router import router as apps_router


app = FastAPI()
app.include_router(apps_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
