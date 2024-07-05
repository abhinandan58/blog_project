from pydantic import BaseModel,validator

class Blogdetailschema(BaseModel):
    id: int
    title:str
    description:str
    status:str
    
    # @validator("id")
    # def validate_id(v):
    #     if not v:
    #         raise ValueError("id cannot be empty")
    #     return v
    @validator("title")
    def validate_title(v):
        if not v:
            raise ValueError("title is compalsory")
        if len(v)>50:
            raise ValueError("title should not exceed 50")
        return v
    @validator("description")
    def validate_description(v):
        if not v:
            raise ValueError("there should be description")
        return v