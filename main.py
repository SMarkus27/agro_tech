import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infrastructure.api.fastapi.routes.base import BaseAPIRouter


app = FastAPI()

app.include_router(BaseAPIRouter.get_instance())

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    api_port = 8000
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=api_port,
    )