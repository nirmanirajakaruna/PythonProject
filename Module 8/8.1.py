import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="your password", database="airport")

cur = conn.cursor()

code = input("Enter ICAO code: ").upper()

cur.execute("SELECT name, municipality FROM airport  WHERE ident=%s", (code,))
row = cur.fetchone()

if row:
    print("Airport name:",row[0])
    print("Location:",row[1])
else:
    print("Airport not found.")

cur.close()
conn.close()