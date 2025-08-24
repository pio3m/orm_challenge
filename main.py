from python_database.kuba_orm_challenge.database import SessionLocal

from models.customer import Customer
from models.address import Address
from models.order import Order
from models.product import Product

# przyklad wykorzystania kodu

session = SessionLocal()

# 1. Dodaj klienta i adres
customer = Customer(name="Jan Kowalski", email="jan@exampl3e2.com")
address = Address(street="Warszawska 10", city="Warszawa", customer=customer)


# 2. Dodaj produkty
product1 = Product(name="Laptop", price=3500)
product2 = Product(name="Myszka", price=100)


# 3. Utwórz zamówienie i przypisz produkty
order = Order(customer=customer)

order.products.extend([product1, product2])

session.add(customer)  # zapisujemy całość
session.commit()

# Odczyt — pokaż wszystkie zamówienia Jana
jan = session.query(Customer).filter_by(name="Jan Kowalski").first()

for order in jan.orders:
    print(f"Zamówienie #{order.id}: {[p.name for p in order.products]}")
