#Daan Durt
from fastapi import APIRouter
import database
from queries import r0462116_queries as queries
from models import r0462116_models as models

app = APIRouter()

@app.post("/reservations")
def create_reservation(reservations: models.Reservation):
    query = queries.insert_reservation
    success = database.execute_sql_query(query, (
        reservations.first_name,
        reservations.last_name,
        reservations.email_address,
        reservations.date_tm,
        reservations.amount_of_people,
        reservations.remarks
    ))
    if success:
        return reservations