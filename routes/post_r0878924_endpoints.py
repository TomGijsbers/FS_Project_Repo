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



@app.post("/uploadPhoto")
async def create_uploadPhoto(
        name: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...)
):
    # Hier zou je de logica plaatsen om de bestandsnaam te valideren/opschonen
    filename = f"assets/student2/{file.filename}"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "wb") as buffer:
        shutil.copyfileobj(await file.read(), buffer)

    upload_date = datetime.now().isoformat()  # Huidige tijd in ISO formaat
    # Gebruik een aangepaste query of pas je bestaande query aan om de pad te gebruiken
    # en de upload_date die je net hebt gegenereerd
    query = queries.r0878924_queries.insert_photo_query
    succes = database.execute_sql_query(query, (
        name,
        filename,
        description,
        upload_date  # Merk op dat dit de huidige tijd is, niet uit het model
    ))

    if succes:
        return {"message": "Photo uploaded successfully", "name": name, "description": description, "path": filename}
    else:
        return {"error": "Failed to upload photo"}


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

