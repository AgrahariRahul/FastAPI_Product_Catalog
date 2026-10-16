import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    app_name:str = "RA-Product-Fast-Api"
    debug:bool = False
    
    @property
    def db_url(self) -> str:
        return os.getenv("DATABASE_URL")
    
    @property
    def product_base_api_url(self) -> str:
        return "https://dummyjson.com"
    
        
settings = Settings()    