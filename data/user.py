from __init__ import connect
from model.user import User
from sqlalchemy import text

connect.execute(text(
    '''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(20) NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL
        )
    '''
))
connect.commit()

