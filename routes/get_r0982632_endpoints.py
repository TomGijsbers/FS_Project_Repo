#Geert Vuurstaek
from fastapi import APIRouter
import database
from queries import r0982632_queries as queries

app = APIRouter()

@app.get("/reviews")
def get_all_reviews():
    query = queries.scoopheaven_reviews
    reviews = database.execute_sql_query(query)
    if isinstance(reviews, Exception):
        return reviews, 500
    reviews_to_return = []
    for review in reviews:
        reviews_dictionary = { "name": review[0],
                               "avatar": review[1],
                               "review": review[2],
                               "rating": review[3],
                               "Time": review[4]

        }
        reviews_to_return.append(reviews_dictionary)
    return {'total_reviews': reviews_to_return}

@app.get("/personel")
def get_personel_by_job(job: str=None):
    query = queries.scoopheaven_personel
    jobtitel = database.execute_sql_query(query,(job,))
    if isinstance(jobtitel, Exception):
        return jobtitel, 500
    jobs_to_return = []
    for jobs in jobtitel:
        jobs_dictionary = {"name": jobs[0],
                              "job": jobs[1],
                              "avatar": jobs[2],
                              "quote": jobs[3]
                              }
        jobs_to_return.append(jobs_dictionary)
    return {'job': jobs_to_return}