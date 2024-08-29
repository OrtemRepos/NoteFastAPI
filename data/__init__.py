import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine

connect = None
load_dotenv()

def get_db(reset: bool = False):
    global connect
    if reset and connect is not None:
        connect.close()
    user = os.getenv("PG_USER")
    password = os.getenv("PG_PASSWORD")
    db_name = os.getenv("PG_DATABASE")
    host = os.getenv("PG_HOST")
    port = os.getenv("PG_PORT")
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}")
    connect = engine.connect() 


get_db()
