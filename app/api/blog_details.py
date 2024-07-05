from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.blog_details import BlogDetails
from app.database_connection.connection import db
from app.schemas.blog_detail_schemas import Blogdetailschema

router = APIRouter(prefix="/api/v1/blog_details")
@router.post("")
def create_blog_detail(blog_detail:Blogdetailschema):
    try:
        blog_info=dict(blog_detail)
        save_blog=BlogDetails(**blog_info)
        db.add(save_blog)
        db.commit()
        return JSONResponse(content={"account cretated"},status_code=201)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)

@router.get("")
def create_blog_detail():
    try:
        blog_details=db.query(BlogDetails).all()
        all_blogs=[obj.info() for obj in blog_details]
        return JSONResponse(content={"message":"data fetched","data":all_blogs},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)


@router.put("/{id}")
def update_blog_status(id:int, updateblog:Blogdetailschema):
    try:
        blog = db.query(BlogDetails).get(id)
        BlogDetails.title= updateblog.title
        BlogDetails.description=updateblog.description
        BlogDetails.status=updateblog.status
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":blog},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)


@router.delete("/{id}")
def update_user_status(id:int):
   try:
       blog = db.query(BlogDetails).get(id)
       db.delete(blog)
       db.commit()
       return JSONResponse(content={"message":"data fetched","data":blog},status_code=200)
   except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)