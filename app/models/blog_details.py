from app.database_connection.connection import Base
from app.models.users import User
from sqlalchemy import Boolean, Column,Text ,DateTime, Integer, String, func,ForeignKey

class BlogDetails(Base):
    __tablename__ = "blog_details"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id=Column(Integer, nullable=False,autoincrement=True)
    # user=ForeignKey("users",backref="blog_details")
    title=Column(String(250))
    description=Column(Text)
    status=Column(String(250))
    created_at=Column(DateTime,default=func.now(),nullable=False)
    updated_at=Column(DateTime,default=func.now(),onupdate=func.now(),nullable=False)
def info(self):
        return({
            "id":self.id,
            "user_id":self.user_id,
            "title":self.title,
            "description":self.description,
        })

