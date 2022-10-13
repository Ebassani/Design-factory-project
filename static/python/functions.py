import numpy as np
import pandas as pd
import sqlite3


def get_top_schools():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('select username, carbon_emission from accounts where is_school==true and carbon_emission>0')
    schools = cur.fetchall()
    schools.sort(key=lambda x: x[1], reverse=False)

    conn.close()
    return schools


def avg(schools):
    df = pd.DataFrame(schools, columns=['carbon'])
    df = df.replace(0, np.NaN)
    return df['carbon'].mean()


def avg_carbon_schools():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('select carbon_emission from accounts where is_school==true and carbon_emission>0')
    schools = cur.fetchall()

    return avg(schools)


def avg_carbon_schools_infra():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('select carbon_emission_infra from accounts where is_school==true and carbon_emission_infra>0')
    schools = cur.fetchall()

    return avg(schools)


def avg_carbon_schools_food():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('select carbon_emission_food from accounts where is_school==true and carbon_emission_food>0')
    schools = cur.fetchall()

    return avg(schools)


def avg_carbon_schools_trans():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('select carbon_emission_food from accounts where is_school==true and carbon_emission_trans>0')
    schools = cur.fetchall()

    return avg(schools)
