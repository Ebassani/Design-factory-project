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

def get_school_accounts():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('select * from accounts where is_school = true')
    schools = cur.fetchall()

    conn.close()
    return schools


def update_carbon():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('update accounts set carbon_emission= carbon_emission_infra '
                '+ carbon_emission_food+carbon_emission_trans')

    conn.commit()
    conn.close()


def update_infra(school_id, value):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('update accounts set carbon_emission_infra = ' + str(value) + ' where school_id = '+str(school_id))

    conn.commit()
    conn.close()


def update_trans(school_id, value):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('update accounts set carbon_emission_trans = ' + str(value) + ' where school_id = '+str(school_id))

    conn.commit()
    conn.close()


def update_food(school_id, value):
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('update accounts set carbon_emission_food = ' + str(value) + ' where school_id = ' + str(school_id))

    conn.commit()
    conn.close()


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
