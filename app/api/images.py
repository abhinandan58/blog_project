from fastapi import APIRouter
from app.schemas.image_schemas import Imageschema
from fastapi.responses import JSONResponse
from app.models.images import Image
from app.database_connection.connection import db

router=APIRouter(prefix="/api/v1/images")
@router.post("")
def create_image(image:Imageschema):
    try:
        image_info=dict(image)
        save_image=Image(**image_info)
        db.add(save_image)
        db.commit()
        return JSONResponse(content={"account created"},status_code=201)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)


@router.get("")
def get_image_details():
    try:
        images=db.query(Image).all()
        print(images,"565656")
        all_images=[obj.info() for obj in images]
        return JSONResponse(content={"message":"data fetched","data":all_images},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)

@router.put("/{id}")
def update_image_status(id:int, updateimage:Imageschema):
    try:
        image = db.query(Image).get(id)
        image.url = updateimage.url
        image.caption=updateimage.caption
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":image},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)

@router.delete("/{id}")
def update_user_status(id:int):
    try:
        image = db.query(Image).get(id)
        image.url = Image.url
        image.caption=Image.caption
        db.delete(image)
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":image},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)



