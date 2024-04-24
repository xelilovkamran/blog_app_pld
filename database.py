from sqlalchemy import create_engine, text
import os

host = os.environ.get("DB_HOST")
user = os.environ.get("DB_USER")
password = os.environ.get("DB_PASSWORD")
db_name = os.environ.get("DB_NAME")

engine = create_engine(
    f"mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8mb4",
    connect_args={
        "ssl": {
            "ssl_ca": "/var/lib/mysql/ca.pem",
        }
    })
