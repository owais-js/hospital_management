from sqlalchemy import Column,Integer,String

from app.core.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String(100),nullable=False)

    gender = Column(String(20),nullable=False)

    specialization = Column(String(100), nullable=False)

    qualification = Column(String(100), nullable=False)

    phone = Column(String(20), nullable=False)

    experience = Column(String(100),nullable=False)