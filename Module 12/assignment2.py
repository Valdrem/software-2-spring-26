import requests


city = input("Enter municipality: ")

api_key = "fd2cac36be4631ae03537b90e9494414"
request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(request_url)
    converted_response = response.json()

    if response.status_code == 200:
        print(f"Weather: {converted_response["weather"]["description"]}")
        print(f"Weather: {converted_response["main"]["temp"]}")
    else:
        print(f"Error: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")
