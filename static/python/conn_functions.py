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
                (name, city, num_students))

    conn.commit()

    cur.execute("select id from schools where name = ?", (name,))
    school_id = cur.fetchone()

    conn.close()
    return school_id[0]


def get_schools():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('select * from schools')
    schools = cur.fetchall()

    conn.close()
    return schools


def create_school_account(email, username, password, city, num_students):
    school_id = create_school(username, city, num_students)

    conn = sqlite3.connect('database.db')

    cur = conn.cursor()

    cur.execute("insert into accounts (email, username, school_id, is_school, password) values (?, ?, ?, ?, ?)",
                (email, username, school_id, True, password))

    conn.commit()
    conn.close()


def create_account(email, username, forename, surname, school_id, password):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("insert into accounts (email, username, school_id, password, forename, surname) "
                "values (?, ?, ?, ?, ?, ?)",
                (email, username, school_id, password, forename, surname))

    conn.commit()
    conn.close()


def finds_user(username, password):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute("select id from accounts where username = ? and password = ?", (username, password))
    ret = cur.fetchall()
    conn.close()

    return ret
