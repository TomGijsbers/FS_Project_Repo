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
def get_all_festivals():
    query = FS_Project_Repo.queries.r0878924_queries.review_name_query
    reviews = database.execute_sql_query(query)
    if isinstance(reviews, Exception):
        return reviews, 500
    coasters_to_return = []
    for coaster in reviews:
        coasters_to_return.append(coaster[0])
    return {'themeparks': coasters_to_return}