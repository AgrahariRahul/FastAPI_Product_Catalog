from fastapi import FastAPI,HTTPException,Depends
from fastapi import APIRouter
import requests
from src.products.product_schema import ProductResponse, ProductsResponse,ProductCategory
from typing import List
from src.products.product_dependencies import productService
from src.products.product_service import ProductService
from src.config import settings

router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.get("",response_model=ProductsResponse)
async def get_all_products(service: productService):
    response = await service.get_products()
    return response

@router.get("/categories",response_model= list[ProductCategory])
async def get_product_categories(service: productService): 
    response = await service.get_product_category()
    return response 

@router.get("/{product_id}",response_model= ProductResponse)
async def get_product_by_id(product_id:int,service: productService): 
    response = await service.get_product(product_id)
    return response 


