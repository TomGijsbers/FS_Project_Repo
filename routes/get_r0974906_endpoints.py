from fastapi import APIRouter
from queries import r0974906_queries
import database
app = APIRouter()

@app.get("/flavours")
def get_flavours_table():
    flavours_query = r0974906_queries.flavours_query
    response_flavours_query = database.execute_sql_query(flavours_query)
    if isinstance(response_flavours_query, Exception):
        return response_flavours_query, 500
    flavours_query_list = []
    for details in response_flavours_query:
        flavours_query_list.append(
            {"FlavourID": details[0], "FlavourName": details[1], "Price": details[2], "Availability": details[3],
             "Vegan": details[4], "SugarFree": details[5]})
    return {"Flavours": flavours_query_list}

@app.get("/holders")
def get_holders_table():
    holders_query = r0974906_queries.holders_query
    response_holders_query = database.execute_sql_query(holders_query)
    if isinstance(response_holders_query, Exception):
        return response_holders_query, 500
    flavours_query_list = []
    for details in response_holders_query:
        flavours_query_list.append(
            {"HolderID": details[0], "Type": details[1], "Price": details[2], "Availability": details[3],
             "Vegan": details[4], "SugarFree": details[5]})
    return {"Holders": flavours_query_list}

@app.get("/toppings")
def get_toppings_table():
    toppings_query = r0974906_queries.toppings_query
    response_toppings_query = database.execute_sql_query(toppings_query)
    if isinstance(response_toppings_query, Exception):
        return response_toppings_query, 500
    flavours_query_list = []
    for details in response_toppings_query:
        flavours_query_list.append(
            {"ToppingID": details[0], "Type": details[1], "Price": details[2], "Availability": details[3],
             "Vegan": details[4], "SugarFree": details[5]})
    return {"Toppings": flavours_query_list}