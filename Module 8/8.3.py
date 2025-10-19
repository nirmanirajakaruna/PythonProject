import sqlite3
from geopy.distance import geodesic

def get_coordinates(icao_code):
    conn = sqlite3.connect('airports_database.db')
    cursor = conn.cursor()

    query = """
    SELECT latitude_deg, longitude_deg FROM airport WHERE ident = ?;"""

    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    conn.close()

    if result:
        return (result[0], result[1])
    else:
        return None

def calculate_distance(icao1, icao2):
    coord1 = get_coordinates(icao1)
    coord2 = get_coordinates(icao2)

    if coord1 and coord2:
        distance = geodesic(coord1, coord2).kilometers
        print(f"Distance between {icao1} and {icao2} is {distance:.2f} kilometers.")
    else:
        print("One or bothICAO codes not found in the database.")

icao_code1 = input("Enter ICAO code of the first airport: ").upper()
icao_code2 = input("Enter ICAO code of the second airport: ").upper()
calculate_distance(icao_code1, icao_code2)
