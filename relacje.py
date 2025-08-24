from python_database.kuba_orm_challenge.database import SessionLocal
from models.customer import Customer
from models.address import Address
from models.order import Order
from models.product import Product

session = SessionLocal()


customer_1 = session.query(Customer).filter_by(name="Jan Kowalski").all()

# Najprostszy LIKE z filter()
results = session.query(Customer).filter(Customer.name.like("%Jan%")).all()
for customer in results:
    print(customer.id, customer.name)
