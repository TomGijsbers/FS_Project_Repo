from fastapi import APIRouter
import database
import queries.r0878924_queries
import models.r0878924_models as r0878924_models
import datetime


app = APIRouter()



@app.post("/contact")
def create_contact(contact: r0878924_models.contact):  # Zorg ervoor dat de import correct is
    query = queries.r0878924_queries.insert_contact_query
    succes = database.execute_sql_query(query, (
        contact.first_name_sender,
        contact.last_name_sender,
        contact.email_sender,
        contact.message,

    ))
    if succes:
        return {"status": "success"}  # Het is beter om een response object terug te sturen

