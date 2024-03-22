#Geert Vuurstaek

from fastapi import APIRouter

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

@app.post("/applicationForm")
def create_applicationForm(applicationForm: models.ApplicationForm):
    query = queries.insert_applications_query
    succes = database.execute_sql_query(query,(
        applicationForm.firstName,
        applicationForm.lastName,
        applicationForm.birthdate,
        applicationForm.gender,
        applicationForm.emailaddress
    ))
    if succes:
        return applicationForm

