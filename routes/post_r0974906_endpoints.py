from fastapi import APIRouter

app = APIRouter()

@app.post("/answer")
def create_answer(answer: r0974906_models.Answer):
    answer_query = queries.r0974906_queries.insert_answer_query
    success_answer_query = database.execute_sql_query(answer_query, (answer.email, answer.flavour, answer.reason,))
    if success_answer_query:
        return answer