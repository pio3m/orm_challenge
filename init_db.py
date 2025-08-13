from database import engine, Base
from sqlalchemy.orm import declarative_base

from models.customer import Customer
from models.address import Address   
from models.order import Order
from models.product import Product


Base.metadata.create_all(engine)
