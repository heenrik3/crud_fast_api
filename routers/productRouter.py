from fastapi import APIRouter
import controllers.productController as productController

router = APIRouter()

@router.get('/products')
async def get_products():
    return await productController.getProducts()

@router.get('/products/{id}')
async def get_product(id: int):
    return await productController.getProduct(id)