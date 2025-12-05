from flask import Flask, jsonify, abort

app = Flask(__name__)

AIRPORT_DB = {
    "EFHK": {
        "ICAO": "EFHK",
        "Name": "Helsinki-Vantaa Airport",
        "Location": "Helsinki"
    },
    "ESSA": {
        "ICAO": "ESSA",
        "Name": "Stockholm Arlanda Airport",
        "Location": "Stockholm" }}

def is_prime(n):
    """Checks if a number n is a prime number."""
    if n is None or not isinstance(n, int) or n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    """
    Tells whether a number received as a parameter is a prime number or not.
    Response format: {"Number": 31, "isPrime": true}
    """
    result = is_prime(number)

    response_data = {
        "Number": number,
        "isPrime": result
    }

    return jsonify(response_data)


@app.route('/airport/<string:icao_code>', methods=['GET'])
def get_airport_info(icao_code):
    """
    Gets the ICAO code of an airport and returns the name and location in JSON format.
    Response format for EFHK: {"ICAO": "EFHK", "Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"}
    """

    icao_code_upper = icao_code.upper()

    airport_data = AIRPORT_DB.get(icao_code_upper)

    if airport_data is None:

        abort(404, description=f"Airport with ICAO code {icao_code_upper} not found.")


    return jsonify({
        "ICAO": airport_data["ICAO"],
        "Name": airport_data["Name"],
        "Location": airport_data["Location"]
    })



if __name__ == '__main__':
    app.run(debug=True)