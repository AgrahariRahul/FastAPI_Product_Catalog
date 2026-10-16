from fastapi import FastAPI
from .. import config
import httpx
from src.config import Settings
from src.products.product_repository import ProductRepository
from src.products.product_schema import ProductsResponse,ProductResponse,ProductCategory


class ProductService():
    
    def __init__(self,settings:Settings):
        self._settings = settings
        self._repository = ProductRepository(self._settings)
        
    async def get_products(self) -> ProductsResponse:
            response = await self._repository.get_products()
            return response   
        
    async def get_product(self,product_id:str) -> ProductResponse:
        response = await self._repository.get_product_by_id(product_id)
        return response
    
    async def get_product_category(self) -> list[ProductCategory]:
            response = await self._repository.get_product_categories()
            return response              

    
    