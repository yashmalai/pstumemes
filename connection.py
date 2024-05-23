import mariadb as db
import sys

def connection():
    try:
        conn = db.connect(
        user="root",
        password="root",
        host="127.0.0.1",
        port=3306,
        database="testingserv"
    )
        return conn
    except db.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

