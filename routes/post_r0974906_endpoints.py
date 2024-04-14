
import database
import queries.r0974906_queries
from models import r0974906_models
from fastapi import APIRouter

app = APIRouter()






@app.post("/reasons")
def create_reasons(reasons: r0974906_models.Reasons):
    reasons_query = queries.r0974906_queries.insert_reasons_query
    success_answer_query = database.execute_sql_query(reasons_query, (reasons.email, reasons.flavour, reasons.reason,))
    if success_answer_query:
        return reasons
