from matplotlib.figure import Figure
import sqlite3


def create_figure(df):
    fig = Figure()
    data2 = df['School name']
    data = df['Total carbon emissions']

    chart = fig.add_subplot()

    chart.bar(data2, data)

    chart.set_ylim(0, data.max()+10)

    chart.invert_yaxis()

    return fig


def get_top_schools():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('select username, carbon_emission from accounts where is_school==true and carbon_emission>0')
    schools = cur.fetchall()
    schools.sort(key=lambda x: x[1], reverse=False)

    conn.close()
    return schools
