#Geert Vuurstaek

from pydantic import BaseModel
from datetime import date

class ApplicationForm(BaseModel):
    firstName: str
    lastName: str
    birthdate: date
    gender: str
    emailaddress : str

class Subscribers(BaseModel):
    email: str
