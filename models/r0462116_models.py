from pydantic import BaseModel
from datetime import datetime

class Resrvation(BaseModel):
    first_name: str
    last_name: str
    email_address: str
    date_tm: datetime
    amount_of_people: int
    remarks: str = None