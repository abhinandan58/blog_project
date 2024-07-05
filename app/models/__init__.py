from app.models import images, users, blog_details
from app.database_connection.connection import Base,engine
Base.metadata.create_all(bind=engine)