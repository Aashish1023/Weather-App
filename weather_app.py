import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

API_KEY = "cfa43beabff99902bd4ad04c8abad5a0"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
ICON_URL = "http://openweathermap.org/img/wn/{}@2x.png"

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
            wind = data["wind"]["speed"]
            icon_code = data["weather"][0]["icon"]

            # Weather icon next to tet in GUP app
            icon_url = ICON_URL.format(icon_code)
            icon_response = requests.get(icon_url)
            icon_data = icon_response.content
            icon_image = Image.open(BytesIO(icon_data)).resize((100, 100), Image.Resampling.LANCZOS)
            icon = ImageTk.PhotoImage(icon_image)

            icon_label.config(image=icon)
            icon_label.image = icon
            
            result = (
                f"📍Weather in {city.capitalize()}:\n"
                f"🌡️Temperature: {temp}°C\n"
                f"Feels Like: {feels_like}°C\n"
                f"🌦️Weather: {weather.capitalize()}\n"
                f"💧Humidity: {humidity}%"\
                f"🍃Wind Speed: {wind} m/s"
                
            )
            result_label.config(text=result)
        else:
            messagebox.showerror("Error", f"City not found. Please check the {city} name and try again.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

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

# 🧠 This MUST exist before config
icon_label = tk.Label(root, bg="#282c34")
icon_label.pack(pady=5)

# Result Label
result_label = tk.Label(root, font=("Helvetica", 14), bg="#282c34", fg="white", justify="left", wraplength=350)
result_label.pack(pady=20)

# Run the App
root.mainloop()
