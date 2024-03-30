from fastapi import APIRouter
import database
import queries.r0878924_queries

app = APIRouter()


@app.get("/photos")
def get_photos():
    query = queries.r0878924_queries.photo_query
    result = database.execute_sql_query(query)
    if isinstance(result, Exception):
        return result, 500
    photo_list = []
    for photo_details in result:
        photo_list.append({
            "id": photo_details[0],
            "name": photo_details[1],
            "path": photo_details[2],
            "description": photo_details[3],
            "upload_date": photo_details[4]
        })
    return {"photos": photo_list}
