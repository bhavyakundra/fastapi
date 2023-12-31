from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func
from sqlalchemy.orm import relationship
from .database import Base
from sql_app import models
from sql_app.database import engine

models.Base.metadata.create_all(bind=engine)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime, default=func.now())
    # One-to-one relationship with UserToken model
    user_token = relationship("UserToken", back_populates="user", uselist=False)
    # One-to-many relationship with Post model
    posts = relationship("Post", back_populates="user")

class UserToken(Base):
    __tablename__ = "user_token"

    id = Column(Integer, primary_key=True, index=True)
    access_token = Column(String, index=True)
    
    # One-to-one relationship with User model
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    user = relationship("User", back_populates="user_token", uselist=False)
    
class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="posts")
    

    