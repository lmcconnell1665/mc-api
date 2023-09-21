import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# if the env variable prod is set, use the ms sql server, else use the sqllite db
if os.getenv("prod"):
    SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:C0ffeeShop&@{os.getenv(prod)}/CoffeeShop"
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

else:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
    engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
