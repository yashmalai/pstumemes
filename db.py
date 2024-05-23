from connection import connection
import mariadb
import sys

def main():
    conn = connection()
    cur = conn.cursor()
    cur.execute("SELECT surname, firstname FROM user")

    #for row in cur:
    #    print(row)
    for surname, firstname in cur:
        print(f"Surname: {surname}, Firstname: {firstname}")
    
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()