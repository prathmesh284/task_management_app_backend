import psycopg
from psycopg.rows import dict_row
from app.core.config import DATABASE_URL

def get_db():
    conn = psycopg.connect(
        DATABASE_URL,
        row_factory=dict_row
    )
    try:
        yield conn
    finally:
        conn.close()
