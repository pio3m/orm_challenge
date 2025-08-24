from .customer import Customer
from .address import Address
from .order import Order
from .product import Product

# __all__ = ["Customer", "Address", "Order", "Product"]

from database import engine, Base
from sqlalchemy.orm import declarative_base

# from .models.customer import Customer
# from .models.address import Address
# from .models.order import Order
# from .models.product import Product


Base.metadata.create_all(engine)
