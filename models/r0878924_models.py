from pydantic import BaseModel
from datetime import date


class contact(BaseModel):
    first_name_sender: str
    last_name_sender: str
    email_sender: str
    message: str


class FaqItem(BaseModel):
    contact_id: int
    question: str
    answer: str