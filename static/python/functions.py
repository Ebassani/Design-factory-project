import pandas as pd
from matplotlib.figure import Figure
import sqlite3


def create_figure(df):
    fig = Figure()
    data2 = df['School name']
    data = df['Total carbon emissions']

    chart = fig.add_subplot()
    chart.bar(data2, data)

    return fig


def getTopSchools():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('select username, carbon_emission from accounts where is_school==true and carbon_emission>0')
    schools = cur.fetchall()

    df = pd.DataFrame(schools, columns=['School name', 'Total carbon emissions'])
    df = df.sort_values(by=['Total carbon emissions'])

    conn.close()
    return df
