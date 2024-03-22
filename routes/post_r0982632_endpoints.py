#Geert Vuurstaek
from fastapi import APIRouter

app = APIRouter()

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

