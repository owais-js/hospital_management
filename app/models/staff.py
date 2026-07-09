from sqlalchemy import Column,Integer,String

from app.core.database import Base

class Staff(Base):
    __tablename__ = "staff"

    id = Column(Integer,primary_key=True,index=True)

    name = Column(String(100),nullable=False)

    gender = Column (String(20), nullable=False)

    designation  = Column (String(100),nullable=False)

    department = Column(String(100),nullable=False)

    phone = Column(String(20),nullable=False)

    salary = Column(Integer,nullable=False)
