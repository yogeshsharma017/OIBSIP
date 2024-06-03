import tkinter as tk
from tkinter import ttk
import requests

def get_location():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        return data.get('city')
    except Exception as e:
        print("Error getting location:", e)
        return ""

def fetch_weather():
    try:
        api_key = "d51e314aafb7f52ec819888d1de6360c"
        city = city_entry.get() or get_location()
        units = units_var.get()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            # Determine temperature unit symbol based on selected metric
            if units == "metric":
                unit_symbol = "°C"
            else:
                unit_symbol = "°F"
                
            temperature_label.config(text=f"Temperature: {data['main']['temp']}{unit_symbol}")
            weather_label.config(text=f"Weather: {data['weather'][0]['description']}")
            # Display weather icon
            icon_url = f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}.png"
            icon_data = requests.get(icon_url).content
            with open("weather_icon.png", "wb") as f:
                f.write(icon_data)
            weather_icon = tk.PhotoImage(file="weather_icon.png")
            icon_label.config(image=weather_icon)
            icon_label.image = weather_icon
        else:
            temperature_label.config(text=f"No location named {city} found!")
            weather_label.config(text="")
            icon_label.config(image="")
    except Exception as e:
        temperature_label.config(text="An error occurred")
        weather_label.config(text="")
        icon_label.config(image="")
        print("Error fetching weather:", e)


app = tk.Tk()
app.title("WeatherOMeter By Yogesh Sharma")
app.geometry("400x400")
app.configure(bg="#e0e0e0")

# Styling
style = ttk.Style()
style.configure("TButton", foreground="#333333", background="#4CAF50", font=("Arial", 12))
style.map("TButton", background=[("active", "#45a049")])

bg_color = "#e0e0e0"
fg_color = "#333333"

city_label = ttk.Label(app, text="Input Location:", background=bg_color, foreground=fg_color, font=("Arial", 12))
city_label.pack(pady=(10, 0))

city_entry = ttk.Entry(app, font=("Arial", 12))
city_entry.pack(pady=(0, 10))

units_var = tk.StringVar(value="metric")  # Default to metric units
units_frame = ttk.Frame(app)
units_frame.pack()
units_frame.config(style="Background.TFrame")
metric_button = ttk.Radiobutton(units_frame, text="Metric (°C)", variable=units_var, value="metric", style="TButton")
imperial_button = ttk.Radiobutton(units_frame, text="Imperial (°F)", variable=units_var, value="imperial", style="TButton")
metric_button.grid(row=0, column=0, padx=(0, 5))
imperial_button.grid(row=0, column=1, padx=(5, 0))

fetch_button = ttk.Button(app, text="Search 🔍", command=fetch_weather)
fetch_button.pack()

temperature_label = ttk.Label(app, text="", background=bg_color, foreground=fg_color, font=("Arial", 14))
temperature_label.pack()

weather_label = ttk.Label(app, text="", background=bg_color, foreground=fg_color, font=("Arial", 14))
weather_label.pack()

icon_label = ttk.Label(app, background=bg_color)
icon_label.pack()

app.mainloop()
