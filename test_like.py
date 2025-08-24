import time
from python_database.kuba_orm_challenge.database import SessionLocal
import models
from models.customer import Customer

session = SessionLocal()

# Fraza do wyszukania
term_contains = "Jan%"  # wiodący %, często wolniejsze


def run_query(pattern):
    return session.query(Customer).filter(Customer.name.like(pattern)).all()


# Pomiar czasu dla "%Jan%"
t0 = time.perf_counter()
results_contains = run_query(term_contains)
t1 = time.perf_counter()
print(f"LIKE '{term_contains}' — znaleziono {len(results_contains)} rekordów w {t1 - t0:.4f} s")

session.close()
