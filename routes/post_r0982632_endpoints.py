#Geert Vuurstaek
from fastapi import APIRouter
import database
from models import r0982632_models
from queries import r0982632_queries as queries

app = APIRouter()

@app.post("/applicationForm")
def create_applicationForm(applicationForm: r0982632_models.ApplicationForm):
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

@app.post("/subscribe")
def create_subscribe(subscription: r0982632_models.Subscribers):
    query = queries.insert_subscriptions_query
    success = database.execute_sql_query(query, (
        subscription.email,
    ))
    if success:
        return subscription
