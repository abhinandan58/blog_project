from app.database_connection.connection import Base
from app.models.users import User
from app.models.blog_details import BlogDetails
from sqlalchemy import Boolean, Column,Text ,DateTime, Integer, String, func,ForeignKey

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, autoincrement=True)
    blog_detail_id=Column(Integer, nullable=False,autoincrement=True)
    blog=ForeignKey("blog_details",backref="image")
    url=Column(String(250))
    caption=Column(String(250))
    created_at=Column(DateTime,default=func.now(),nullable=False)
    updated_at=Column(DateTime,default=func.now(),onupdate=func.now(),nullable=False)
def info(self):
        return({
            "id":self.id,
            "blog_detail_id":self.blog_detail_id,
            "url":self.url,
            "caption":self.caption,
        })

