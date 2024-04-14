from pydantic import BaseModel
from datetime import date

class Answer(BaseModel):
    email: str
    flavour: str
    reason: str