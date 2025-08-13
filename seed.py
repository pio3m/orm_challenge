# Generuje duży zbiór danych, aby LIKE było zauważalnie wolne.
# Uruchom:  python seed.py

from faker import Faker
from database import engine, SessionLocal

from models.customer import Customer
from models.address import Address
from models.order import Order
from models.product import Product

from database import SessionLocal
from sqlalchemy.exc import IntegrityError

# Ile rekordów stworzyć (zmień swobodnie)
N = int(2e5)  # 200 000
BATCH = 1000  # Rozmiar partii do batch insertów

def seed_products(session):
    """Dodaj kilka przykładowych produktów (przyda się do późniejszych przykładów relacji)."""
    base_products = [
        Product(name="Laptop", price=3500),
        Product(name="Myszka", price=100),
        Product(name="Klawiatura", price=250),
        Product(name="Monitor", price=1200),
    ]
    session.add_all(base_products)
    session.commit()

def seed_customers(session):
    """Wstaw dużą liczbę klientów; co kilkadziesiąt rekordów wymuś 'Jan ...' dla testów LIKE."""
    fake = Faker()
    inserted = 0
    batch = []

    for i in range(N):
        # co 37. rekord twórz wzorzec "Jan <Nazwisko>", żeby LIKE miał co znaleźć
        if i % 37 == 0:
            name = f"Jan {fake.last_name()}"
        else:
            name = fake.name()

        email = f"user{i}@example.com"  # unikalny
        batch.append(Customer(name=name, email=email))

        if len(batch) >= BATCH:
            session.add_all(batch)
            try:
                session.commit()
            except IntegrityError:
                session.rollback()
            inserted += len(batch)
            print(f"Wstawiono {inserted}/{N}")
            batch.clear()

    if batch:
        session.add_all(batch)
        try:
            session.commit()
        except IntegrityError:
            session.rollback()
        inserted += len(batch)
        print(f"Wstawiono {inserted}/{N}")

def main():
    with SessionLocal() as session:

        print("Dodawanie produktów (opcjonalne przykłady relacji)...")
        seed_products(session)

        print(f"Generowanie klientów (N={N})...")
        seed_customers(session)

    print("Seed zakończony.")

if __name__ == "__main__":
    main()