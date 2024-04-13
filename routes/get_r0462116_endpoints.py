from fastapi import APIRouter
import database
from queries import r0462116_queries as queries


app = APIRouter()


@app.get("/events")
def get_all_events():
    query = queries.events_query
    events = database.execute_sql_query(query)
    if isinstance(events, Exception):
        return events, 500
    events_to_return = []
    for event in events:
        event_dictionary = {"name": event[0],
                            "date":event[1],
                            "description": event[2],
                            "Participants": event[3],
                            "max_participants": event[4]
                            }
        events_to_return.append(event_dictionary)
    return({'events': events_to_return})


@app.get("/reservations")
def get_amount_for_date(email: str = ''):
    query = queries.reservations_query.reservations_query
    reservations = database.execute_sql_query(query, (
        email,))
    if isinstance(reservations, Exception):
        return reservations, 500
    reservations_to_return = []
    for reservation in reservations:
        reservation_dictionary = {"first name": reservation[0],
                                  "last name": reservation[1],
                                  "email": reservation[2],
                                  "date": reservation[3],
                                  "amount": reservation[4],
                                  "remarks": reservation[5]}
        reservations_to_return.append(reservation_dictionary)
    return({'reservations': reservations_to_return})
