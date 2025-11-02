import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(municipality):
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("City not found or API error.")
        return

    weather_desc = data['weather'][0]['description']
    temp_kelvin = data['main']['temp']
    temp_celsius = kelvin_to_celsius(temp_kelvin)

    print(f"Weather in {municipality}: {weather_desc}, Temperature: {temp_celsius:.2f}°C")

city = input("Enter the name of a municipality: ")
get_weather(city)