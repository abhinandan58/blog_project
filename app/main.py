from fastapi import FastAPI,Body,HTTPException,Request
from fastapi.responses import JSONResponse,FileResponse,Response,HTMLResponse,StreamingResponse
from app.database_connection.connection import*
from app.models import *
from app.models.users import User
from app.models.images import Image
from app.models.blog_details import BlogDetails
from app.schemas.user_schemas import UserSchema
from app.api.users import router as user_router
from app.api.blog_details import router as blog_router
from app.api.images import router as image_router
from fastapi.encoders import jsonable_encoder


app=FastAPI()

@app.exception_handler(HTTPException)
async def validation_exception_handler(request: Request, e: HTTPException):
    return JSONResponse(
        status_code=e.status_code,
        content=jsonable_encoder({
            "success": False,
            "status_code":e.status_code,
            "error": f"{e.detail}"
        }),
    )

# Includes users api
app.include_router(user_router)
app.include_router(blog_router)
app.include_router(image_router)

















# def images(body:dict=Body(...)):
#     url=body.get("url")
#     caption=body.get("caption")
#     image=Image(url=url,caption=caption)
#     db.add(image)
#     db.commit()
#     return JSONResponse(content={image.info()},status_code=200)

# def blog_details(body:dict=Body(...)):
#     title=body.get("title")
#     description=body.get("description")
#     blog_detail=BlogDetails(title=title,description=description)
#     db.add(blog_detail)
#     db.commit()
#     return JSONResponse(content={blog_detail.info()},status_code=200)