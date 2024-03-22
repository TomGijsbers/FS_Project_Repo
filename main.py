from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import config
from routes import get_r0878924_endpoints, get_r0982632_endpoints, get_r0462116_endpoints, get_r0974906_endpoints, post_r0462116_endpoints, post_r0878924_endpoints, post_r0974906_endpoints, post_r0982632_endpoints


app = FastAPI()

app.include_router(router=get_r0462116_endpoints.app)
app.include_router(router=get_r0878924_endpoints.app)
app.include_router(router=get_r0982632_endpoints.app)
app.include_router(router=get_r0974906_endpoints.app)

app.include_router(router=post_r0462116_endpoints.app)
app.include_router(router=post_r0878924_endpoints.app)
app.include_router(router=post_r0974906_endpoints.app)
app.include_router(router=post_r0982632_endpoints.app)


origins = config.cors_origins.split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
