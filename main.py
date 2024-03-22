from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database
import config
from routes import get_r0878924_endpoints

app = FastAPI()

app.include_router(router=get_r0878924_endpoints.app)
# app.include_router(router=post_r0878924_endpoints.app)

origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {'themeparks': 'test'}