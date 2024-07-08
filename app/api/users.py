from fastapi import APIRouter,HTTPException
from app.schemas.user_schemas import UserSchema
from fastapi.responses import JSONResponse
from app.models.users import User
from app.database_connection.connection import db
from app.helper_fuctions.hashing import hashed_password

router = APIRouter(prefix="/api/v1/users",tags=["user API's"])

@router.post("")
def create_user(user:UserSchema):
    try:
        user_info = dict(user)
        user_info['password'] = hashed_password(user_info['password'])
        save_user = User(**user_info)
        db.add(save_user)
        db.commit()
        return JSONResponse(content={"message":"","data":[]},status_code=201)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)
    
@router.get("")
def get_user_details():
    try:
        users = db.query(User).all()
        all_users = [obj.info() for obj in users]
        return JSONResponse(content={"message":"data fetched","data":all_users},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)

@router.put("/{id}")
def update_user_status(id:int, updateUser:UserSchema):
    try:
        user = db.query(User).get(id)
        user.email = updateUser.email
        user.username=updateUser.username
        user.contact=updateUser.contact
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":[]},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)
                       

@router.delete("/{id}")
def update_user_status(id:int):
    try:
        user = db.query(User).get(id)
        db.delete(user)
        db.commit()
        return JSONResponse(content={"message":"data fetched","data":user},status_code=200)
    except Exception as e:
        print(e ,"##########")
        return JSONResponse(content={"message":"usr not found","data":[]}, status_code=404)























    """
    Create user by using user information
    Args:
        user (Userschema): IT create user by using userschema information

    Returns:
        It returns jsonreponse
    """