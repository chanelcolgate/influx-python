import pandas as pd
from influxdb import InfluxDBClient

vix_db = pd.read_csv('InfluxDB/vix-daily_csv.csv', parse_dates=[0])

points = []
for index, row in vix_db.iterrows():
    point = {
            "measurement": "financial-analysis",
            "tags": {
                "type": "vix-daily"
                },
            "fields": {
                "open": row[1],
                "high": row[2],
                "low": row[3],
                "close": row[4]
                },
            "date": row[0]
            }
    #points.append(point)

points.append(point)
print(point)
client = InfluxDBClient('localhost', 8086, 'root', 'root', 'Example')
client.create_database('Example')
client.write_points(points)
