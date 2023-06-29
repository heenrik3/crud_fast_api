from fastapi import FastAPI
from routers.productRouter import router as ProductRouter
from controllers.errorController import exceptionHandler

app = FastAPI()

app.include_router(ProductRouter)

app.add_exception_handler(Exception, exceptionHandler)