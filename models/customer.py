from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

    address = relationship("Address", back_populates="customer", uselist=False)
    orders = relationship("Order", back_populates="customer")
