from database import Base, engine
from models.customer import Customer
from models.address import Address
from models.order import Order
from models.product import Product

Base.metadata.create_all(engine)
