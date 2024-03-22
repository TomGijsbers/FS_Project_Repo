from fastapi import APIRouter
import database
from models import models
from queries import festival_queries as queries

app = APIRouter()