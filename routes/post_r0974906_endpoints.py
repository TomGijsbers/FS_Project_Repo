from fastapi import APIRouter

app = APIRouter()

@app.post("/reasons")
def create_answer(reasons: r0974906_models.Answer):
    reasons_query = queries.r0974906_queries.insert_reasons_query
    success_answer_query = database.execute_sql_query(reasons_query, (reasons.email, reasons.flavour, reasons.reason,))
    if success_answer_query:
        return answer