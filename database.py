from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()

# podmien na inne parametry, jesli potrzebujesz
# lub ustaw zmienne srodowiskowe
# DB_USER = "myuser"
# DB_PASSWORD = "mypassword"
# DB_HOST = "localhost"
# DB_PORT = "5435"
# DB_NAME = "shop"

DATABASE_URL = "postgresql+psycopg2://postgres:grosales@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
# echo=True - włącza logowanie zapytań SQL do konsoli
# engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
