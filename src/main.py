from fastapi import FastAPI
from .api import register_route

app = FastAPI()


register_route(app=app)
