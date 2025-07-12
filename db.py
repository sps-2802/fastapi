# db.py
import psycopg2

def getConnection():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="Ayrus"
    )
    
    try:
        yield conn
    finally:
        conn.close()
        