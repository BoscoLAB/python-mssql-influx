#!/usr/bin/python
#

import pymssql
from pymssql import _mssql
import time
import datetime

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=40)

from datetime import datetime, timedelta

current_time = datetime.utcnow().strftime("%Y-%m-%d")
#print(current_time)

global contents 


# MS SQL Verbindung aufbauen
conn = pymssql.connect("1.1.1.1","user","user","Datenbank")
cursor = conn.cursor(as_dict=True)
#Select ausführen
cursor.execute("SELECT ...))
for row in cursor:
#    print(row['ROW'])
    contents  = (row['ROW'])
conn.close()

# gelesene Daten in die Influx Datenbank schreiben
from datetime import datetime, timedelta

current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")

json_body = [

 {

        "measurement": "Name",

        "time": current_time,

        "fields": {'contents': contents}

 }

 ]

 #print (json_body)
# Verbindung zur Influx Datenbank aufbauen
from influxdb import InfluxDBClient

client = InfluxDBClient('1.1.1.1', '8086', 'user', 'user', 'Datenbank')

client.write_points(json_body)

