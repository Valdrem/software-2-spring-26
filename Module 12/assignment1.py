import requests

request = "https://api.chucknorris.io/jokes/random"

try:

    response = requests.get(request)
    converted_response = response.json()

    if response.status_code == 200:
        print(converted_response["value"])
    else:
        print(f"Error: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")


