from fastapi import FastAPI
from src.products.router import router as productrouter

def register_route(app: FastAPI):
    app.include_router(productrouter)