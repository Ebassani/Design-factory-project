import sqlite3


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = sqlite3.connect('database.db')

    with open('schema.sql') as f:
        conn.executescript(f.read())

    conn.close()


def create_school(name, city, num_students):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("insert into schools (name, city, num_students) values (?, ?, ?)",
                (name, city, num_students)
                )

    conn.commit()
    conn.close()
