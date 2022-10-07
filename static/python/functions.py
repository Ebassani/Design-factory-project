import pandas as pd
from matplotlib.figure import Figure
import sqlite3


def create_figure(df):
    fig = Figure()
    data2 = df['School name']
    data = df['Total carbon emissions']

    chart = fig.add_subplot()

    bars = chart.bar(data2, data.max()-data, bottom=data+10, color=['red', 'blue'])

    chart.set_ylim(0, data.max()+10)

    chart.invert_yaxis()

    for bar in bars:
        bar.sticky_edges.y[:] = [data.values.max()]

    return fig


def get_top_schools():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    cur.execute('select username, carbon_emission from accounts where is_school==true and carbon_emission>0')
    schools = cur.fetchall()

    df = pd.DataFrame(schools, columns=['School name', 'Total carbon emissions'])
    df = df.sort_values(by=['Total carbon emissions'])

    conn.close()
    return df
