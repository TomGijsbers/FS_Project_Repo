from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database
import config
from routes import get_r0878924_endpoints
from queries import r0878924_queries

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


# @app.get("/")
# def root():
#     return {'themeparks': 'test'}

@app.get("/test")
def get_all_festivals():
    query = r0878924_queries.contact_name_query
    coasters = database.execute_sql_query(query)
    if isinstance(coasters, Exception):
        return coasters, 500
    coasters_to_return = []
    for coaster in coasters:
        coasters_to_return.append(coaster[0])
    return {'themeparks': coasters_to_return}