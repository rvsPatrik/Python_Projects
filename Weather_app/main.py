"""
    Created on 2024-12-04

    @author: rvsPatrik
"""

import tkinter as tk
import requests
import os
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("WEATHER_API")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

if not API_KEY:
    raise ValueError("Missing API key.")

def fetch_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
    
    params = {"q": city,"appid":API_KEY,"units":"metric"}

    try:
        response = requests.get(BASE_URL,params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        result_label.config(
            text = f"City: {city}\nTemperature: {temp}°C\nWeather: {weather}\nHumidity: {humidity}%"
        )
    except requests.exceptions.RequestException as e:
        result_label.config(text="Error Fetching weather data. Try again.")
    except KeyError:
        result_label.config(text="City not found. Check the name.")

root = tk.Tk()
root.geometry("250x200")
root.resizable(0,0)
root.title("Weather app")

tk.Label(root,text="Enter city:").pack(pady = 5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

fetch_button = tk.Button(root,text="Check Weather",command=fetch_weather)
fetch_button.pack(pady=10)

result_label = tk.Label(root,text="",wraplength=280)
result_label.pack(pady=10)

root.mainloop()