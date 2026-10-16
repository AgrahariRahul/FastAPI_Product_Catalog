from src.products.product_schema import ProductsResponse,ProductResponse,ProductCategory
from src.config import Settings
import httpx


class ProductRepository():
    
    def __init__(self, settings: Settings):
        self._settings = settings
    
    
    async def get_products(self) -> ProductsResponse:
        """ fetch all product"""
        async with httpx.AsyncClient() as client:
           url = f"{self._settings.product_base_api_url}/products"
           response = await client.get(url)
           return response.json()
    
    
   
    async def get_product_by_id(self,product_id:int) -> ProductResponse:
        """ fetch product by id"""
        async with httpx.AsyncClient() as client:
            url = f"{self._settings.product_base_api_url}/products/{product_id}"
            response = await client.get(url)
            return response.json()


    async def get_product_categories(self) -> list[ProductCategory]:
        """fetch all product categories"""
        async with httpx.AsyncClient() as client:
                    url = f"{self._settings.product_base_api_url}/products/category-list"
                    response = await client.get(url)
                    categories = response.json()
                    return [
                        ProductCategory(category= category) for category in categories
                    ]
    