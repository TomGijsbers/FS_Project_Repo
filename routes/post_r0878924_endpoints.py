from fastapi import APIRouter,File, UploadFile, Form
import database
import queries.r0878924_queries
import models.r0878924_models as r0878924_models
import datetime
import os
import shutil

app = APIRouter()


# @app.post("/uploadPhoto")
# def create_uploadPhoto(uploadPhoto: r0878924_models.uploadPhoto):
#     query = queries.r0878924_queries.insert_photo_query
#     succes = database.execute_sql_query(query,(
#         uploadPhoto.id,
#         uploadPhoto.name,
#         uploadPhoto.path,
#         uploadPhoto.description,
#         uploadPhoto.upload_date.isoformat() #convert date to string
#     ))
#     if succes:
#         return uploadPhoto




@app.post("/contact")
def create_contact(contact: r0878924_models.contact):  # Zorg ervoor dat de import correct is
    query = queries.r0878924_queries.insert_contact_query
    succes = database.execute_sql_query(query, (
        contact.first_name_sender,
        contact.last_name_sender,
        contact.email_sender,
        contact.message,
        datetime.now(),  # Dit zal de huidige tijd/datum toevoegen
    ))
    if succes:
        return {"status": "success"}  # Het is beter om een response object terug te sturen

