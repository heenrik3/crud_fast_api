from fastapi import Request
from fastapi.responses import JSONResponse

async def exceptionHandler(req: Request, err: Exception):
    return JSONResponse(
        # status_code=err.status_code,
        content={
            "message": str(err)
        }
    )