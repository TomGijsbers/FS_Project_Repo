from pydantic import BaseModel
from datetime import date
class uploadPhoto(BaseModel):
    name: str
    description: str


class contact(BaseModel):
    contact_id: int
    first_name_sender: str
    last_name_sender: str
    email_sender: str
    message: str
    created_at: date