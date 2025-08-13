from database import Base, engine, SessionLocal
from models.customer import Customer
from models.address import Address
from models.order import Order
from models.product import Product

session = SessionLocal()


piotr = session.query(Customer).filter_by(name="piotr").all()
# print(piotr[0].name)

print(piotr[0].address.street)

# customer = Customer(name="Pawel", email="pawel@example.com")
# order_1 = Order(customer=customer)

# session.add(customer)
# session.commit()    

pawel = session.query(Customer).filter_by(name="Pawel").first()
for order in pawel.orders:
    print(f"Zamówienie #{order.id}: {[p.name for p in order.products]}")

