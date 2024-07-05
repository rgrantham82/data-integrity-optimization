-- Insert data into the crime_reports table
COPY crime_reports FROM 'path_to_cleaned_csv_file.csv' CSV HEADER;

-- If using a direct API connection, you might need a Python script or similar to fetch and insert data.
-- Here's an example using Python's psycopg2 library:
"""
import requests
import psycopg2
import csv
from io import StringIO

url = 'https://data.austintexas.gov/resource/fdj4-gpfu.csv'
response = requests.get(url)

conn = psycopg2.connect("dbname=your_db user=your_user password=your_password")
cur = conn.cursor()

csv_file = StringIO(response.text)
csv_reader = csv.reader(csv_file)

header = next(csv_reader)
for row in csv_reader:
    cur.execute("INSERT INTO crime_reports VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326))", row)

conn.commit()
cur.close()
conn.close()
"""
