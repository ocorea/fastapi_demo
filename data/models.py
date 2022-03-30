from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer)
    factorial = Column(Integer)
   