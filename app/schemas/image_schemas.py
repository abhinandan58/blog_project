from pydantic import BaseModel,validator

class Imageschema(BaseModel):
    id: int
    blog_detail_id:int
    url:str
    caption:str
    # @validator("id")
    # def validate_id(v):
    #     if not v:
    #         raise ValueError("id cannot be empty")
    #     return v
    # @validator("blog_detail_id")
    # def validator_blog_detail_id(v):
    #     if not v:
    #         raise ValueError("blog id is important") 
    #     return v
    @validator("url")
    def validator_url(v):
        if not v:
            raise ValueError("url is important")
        if ' ' in v:
            raise ValueError("there is no space in url")
        return v
    @validator("caption")
    def validator_description(v):
        if not v:
            raise ValueError("compolsary to write caption")
        return v
   