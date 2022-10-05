import pandas as pd
from matplotlib.figure import Figure
import sqlite3


def create_figure():
    fig = Figure()
    data2 = range(10)
    data = (1, 9, 3, 4, 5, 6, 7, 8, 9, 10)

    chart = fig.add_subplot()
    chart.plot(data2, data)

    return fig


def getTopSchools():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('select username, carbon_emission from accounts where is_school==true and carbon_emission>0')
    schools = cur.fetchall()

    df = pd.DataFrame(schools, columns=['School name', 'Total carbon emissions'])
    df = pd.crosstab(df['Total carbon emissions'], df['School name'])
    print(df)

    conn.close()
    return schools
