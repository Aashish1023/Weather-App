# weather_app.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import requests

API_KEY = "cfa43beabff99902bd4ad04c8abad5a0"

class WeatherApp(App):
    def build(self):
        self.box = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.city_input = TextInput(hint_text="Enter city", multiline=False)
        self.result_label = Label(text="Weather info will appear here.")
        self.button = Button(text="Get Weather", on_press=self.get_weather)

        self.box.add_widget(self.city_input)
        self.box.add_widget(self.button)
        self.box.add_widget(self.result_label)

        return self.box

    def get_weather(self, instance):
        city = self.city_input.text.strip()
        if not city:
            self.result_label.text = "Please enter a city name."
            return

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        try:
            res = requests.get(url).json()
            temp = res['main']['temp']
            desc = res['weather'][0]['description']
            self.result_label.text = f"{city.title()}: {temp}°C, {desc.title()}"
        except:
            self.result_label.text = "Could not get weather."

WeatherApp().run()
