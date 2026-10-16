from pydantic import BaseModel
from datetime import datetime


class Dimensions(BaseModel):
    width: float
    height: float
    depth: float


class Review(BaseModel):
    rating: int
    comment: str
    date: datetime
    reviewerName: str
    reviewerEmail: str


class ProductMeta(BaseModel):
    createdAt: datetime
    updatedAt: datetime
    barcode: str
    qrCode: str


class ProductResponse(BaseModel):
    id: int
    title: str
    description: str
    category: str
    price: float
    discountPercentage: float
    rating: float
    stock: int
    tags: list[str]
    brand: str | None = None
    sku: str
    weight: float
    dimensions: Dimensions
    warrantyInformation: str
    shippingInformation: str
    availabilityStatus: str
    reviews: list[Review]
    returnPolicy: str
    minimumOrderQuantity: int
    meta: ProductMeta
    thumbnail: str
    images: list[str]

class ProductsResponse(BaseModel):
    products: list[ProductResponse]
    total: int 
    skip: int
    limit: int
    
class ProductCategory(BaseModel):
    category: str    