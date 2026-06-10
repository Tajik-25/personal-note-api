from sqlalchemy import Integer,String,ForeignKey,DateTime,Column
from datetime import datetime
from sqlalchemy.orm import relationship
from database import Base
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
    notes = relationship("Notes",back_populates="user")
class Notes(Base):
    __tablename__ = "notes"
    id = Column(Integer,primary_key=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime,default=datetime.utcnow())
    owner_id = Column(Integer,ForeignKey("users.id"))
    user = relationship("Users",back_populates="notes")
