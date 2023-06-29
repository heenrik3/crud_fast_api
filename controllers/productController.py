from models.productModel import products
from utils import response

async def getProducts():
    return response('success', None, products)

async def getProduct(id):
    return response('success', None, products[id])

