from fastapi import Depends
from src.config import settings,Settings
from src.products.product_service import ProductService
from typing import Annotated




def get_product_service() -> ProductService:
    return ProductService(settings= settings)


productService = Annotated[ProductService,Depends(get_product_service)]

