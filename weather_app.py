import tkinter as tk
from tkinter import messagebox
import requests

API_KEY = "cfa43beabff99902bd4ad04c8abad5a0"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Function to get weather data
def get_weather():
    city = city_entry.get()
    if city == "":
        messagebox.showerror("Input Error", "Please enter a city name.")
        return

    # building complete api url
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    # sending get request and saving the response as response object
    try:
        response = requests.get(url)
        data = response.json()

        # extracting data
        if response.status_code == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            weather = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            # wind = data["wind"]["speed"]

            result = (
                f"Weather in {city.capitalize()}:\n"
                f"Temperature: {temp}°C\n"
                f"Feels Like: {feels_like}°C\n"
                f"Weather: {weather.capitalize()}\n"
                f"Humidity: {humidity}%"
                # f"Wind Speed: {wind} m/s"
            )
            result_label.config(text=result)
        else:
            messagebox.showerror("Error", f"City not found. Please check the {city} name and try again.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # print("City not found or API request failed. Please check the city name and try again.")
        # print(f"Error Code: {response.status_code}")
        # print(f"Error Message: {response.text}")

# ----- GUI Setup -----
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.configure(bg="#282c34")

# Title
title = tk.Label(root, text="🌤️ Weather App", font=("Helvetica", 20, "bold"), bg="#282c34", fg="white")
title.pack(pady=10)

# City Entry
city_entry = tk.Entry(root, font=("Helvetica", 16), justify="center")
city_entry.pack(pady=10)
city_entry.focus()

# Get Weather Button
get_btn = tk.Button(root, text="Get Weather", font=("Helvetica", 14), bg="#61dafb", fg="black", command=get_weather)
get_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, font=("Helvetica", 14), bg="#282c34", fg="white", justify="left", wraplength=350)
result_label.pack(pady=20)

# Run the App
root.mainloop()
