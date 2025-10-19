import sqlite3

def get_airports_by_country(area_code):
    conn = sqlite3.connect('airport_database.db')
    cursor = conn.cursor()

    query = """
    SELECT name, type 
    FROM airport
    WHERE iso_country = ?
    ORDER BY type;"""

    cursor.execute(query, (area_code,))
    airports = cursor.fetchall()

    if airports:
        print(f"Airports in country {area_code}:")
        for airport in airports:
            print(f"Name: {airport[0]}, Type: {airport[1]}")

    else:
        print(f"No airports found for country code {area_code}.")

     conn.close()

area_code = input("Enter the area code(e.g., FI): ").upper()
get_airports_by_country(area_code)