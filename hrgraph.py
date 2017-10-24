#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

tempdata = []
dates = []
# Read the data from db
con = mdb.connectcon = ('DBHOST', 'DBUSER', 'DMPASS', 'DB');
cur = con.cursor()
cur.execute("SELECT datetime, temp  FROM readings ORDER BY `datetime` DESC limit 60")
for i in range(cur.rowcount):
    row = cur.fetchone()
    date = matplotlib.dates.date2num(row[0])
    dates.append(date)
    tempdata.append(row[1])
con.close()

fig, ax = plt.subplots(figsize=(6,5))
ax.plot_date(dates, tempdata,fmt='-')
ax.xaxis.set_major_formatter(DateFormatter('%H:%M'))

ax.set_ylabel('Temperature F')
for label in ax.get_xticklabels():
    label.set_rotation(60)
plt.tight_layout()

plt.savefig('/var/www/html/hrtemp.png')
