import requests

API_KEY = "cfa43beabff99902bd4ad04c8abad5a0"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter City Name:")

#building complete api url
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

# sending get request and saving the response as response object
response = requests.get(url)

# extracting data
if response.status_code == 200:
    data = response.json()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
#    wind = data["main"]["speed"]

    print(f"\n Weather in {city.capitalize()}:")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Weather: {weather.capitalize()}")
    print(f"Humidity: {humidity}%")
   # print(f"Wind Speed: {wind} m/s")
else:
    print("City not found or API request failed. Please check the city name and try again.")
    print(f"Error Code: {response.status_code}")
    print(f"Error Message: {response.text}")

