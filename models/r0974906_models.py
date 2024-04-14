from pydantic import BaseModel
from datetime import date

class Reasons(BaseModel):
    email: str
    flavour: str
    reason: str

