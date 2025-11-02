import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    print(data['value'])  # Print only the joke text

get_chuck_norris_joke()