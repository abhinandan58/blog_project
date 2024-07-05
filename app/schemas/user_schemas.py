from pydantic import BaseModel,validator,EmailStr

class UserSchema(BaseModel):
    # id: int
    username:str
    email: EmailStr
    password: str
    contact:int

    # @validator("id")
    # def validate_id(v):
    #     if not v:
    #         raise ValueError("Id cannot be empty")
    #     return v                 

    @validator("username")
    def validate_username(v):
        if not v:
            
            raise ValueError("Username cannot be empty")
        return v
    @validator("email")
    def validate_email(v):
        if not v:
            raise ValueError("Email cannot be empty")
        return v

    @validator("password")
    def validate_password(v):
        if not v:
            raise ValueError("Password cannot be empty")
        if ' ' in v:
                raise ValueError("Password cannot contain spaces.")
        return v

    @validator("contact")
    def validate_contact(v):
        if not v:
            raise ValueError("Phone Number cannot be empty")
        # if ' ' in v:
        #         raise ValueError("Phone number cannot contain spaces.")
        if len(str(v)) > 10:
                raise ValueError("Phone Number cannot have more than 10 digits")
        return v