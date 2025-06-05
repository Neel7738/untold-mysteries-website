# climatrack.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
import turtle
import random

# --- WeatherRecord Class ---
class WeatherRecord:
    def __init__(self, date, temperature, rainfall, humidity, wind_speed):
        self.date = date
        self.temperature = temperature
        self.rainfall = rainfall
        self.humidity = humidity
        self.wind_speed = wind_speed

# --- WeatherDataset Class ---
class WeatherDataset:
    def __init__(self):
        self.records = []
        self.df = None

    def load_data(self, csv_file):
        self.df = pd.read_csv(csv_file, parse_dates=['date'])
        self.df.dropna(inplace=True)

        self.records = []
        for _, row in self.df.iterrows():
            record = WeatherRecord(
                row['date'],
                row['temperature'],
                row['rainfall'],
                row['humidity'],
                row['wind_speed']
            )
            self.records.append(record)

    def filter_by_month(self, month):
        return [r for r in self.records if r.date.month == month]

    def filter_by_year(self, year):
        return [r for r in self.records if r.date.year == year]

    def average_temperature(self):
        if not self.records:
            return 0
        return sum(r.temperature for r in self.records) / len(self.records)

    def max_temperature(self):
        if not self.records:
            return 0
        return max(r.temperature for r in self.records)

    def min_temperature(self):
        if not self.records:
            return 0
        return min(r.temperature for r in self.records)

    def total_rainfall(self):
        if not self.records:
            return 0
        return sum(r.rainfall for r in self.records)

    def most_humid_day(self):
        if not self.records:
            return None
        return max(self.records, key=lambda r: r.humidity)

    def windiest_day(self):
        if not self.records:
            return None
        return max(self.records, key=lambda r: r.wind_speed)

# --- ClimaTrackApp Class ---
class ClimaTrackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ClimaTrack – Weather Data Analyzer")
        self.dataset = WeatherDataset()

        # GUI Buttons
        tk.Button(root, text="Load Data", command=self.load_data, width=30).pack(pady=5)
        tk.Button(root, text="Show Statistics", command=self.show_statistics, width=30).pack(pady=5)
        tk.Button(root, text="Analyze Data (Plots)", command=self.analyze_data, width=30).pack(pady=5)
        tk.Button(root, text="Weather Animation", command=self.weather_animation, width=30).pack(pady=5)
        tk.Button(root, text="Predict Weather", command=self.predict_weather, width=30).pack(pady=5)
        tk.Button(root, text="Exit", command=root.destroy, width=30).pack(pady=5)

    # --- Load CSV Data ---
    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.dataset.load_data(file_path)
            messagebox.showinfo("Success", "Data loaded successfully!")

    # --- Show basic statistics ---
    def show_statistics(self):
        if not self.dataset.records:
            messagebox.showerror("Error", "Please load a dataset first.")
            return

        avg_temp = self.dataset.average_temperature()
        max_temp = self.dataset.max_temperature()
        min_temp = self.dataset.min_temperature()
        total_rain = self.dataset.total_rainfall()
        humid_day = self.dataset.most_humid_day()
        windy_day = self.dataset.windiest_day()

        stats = f"""
        Average Temperature: {avg_temp:.2f} °C
        Maximum Temperature: {max_temp:.2f} °C
        Minimum Temperature: {min_temp:.2f} °C
        Total Rainfall: {total_rain:.2f} mm
        Most Humid Day: {humid_day.date.date()} ({humid_day.humidity}%)
        Windiest Day: {windy_day.date.date()} ({windy_day.wind_speed} km/h)
        """

        messagebox.showinfo("Weather Statistics", stats)

    # --- Analyze Data (Graphs) ---
    def analyze_data(self):
        if self.dataset.df is None:
            messagebox.showerror("Error", "Load dataset first!")
            return

        df = self.dataset.df

        # 1. Temperature over time
        plt.figure(figsize=(10,5))
        sns.lineplot(x='date', y='temperature', data=df)
        plt.title('Temperature Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # 2. Rainfall distribution
        plt.figure(figsize=(8,5))
        sns.histplot(df['rainfall'], bins=30, kde=True)
        plt.title('Rainfall Distribution')
        plt.tight_layout()
        plt.show()

        # 3. Humidity trend
        plt.figure(figsize=(10,5))
        sns.lineplot(x='date', y='humidity', data=df)
        plt.title('Humidity Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # 4. Wind Speed variation
        plt.figure(figsize=(8,5))
        sns.boxplot(x='wind_speed', data=df)
        plt.title('Wind Speed Variation')
        plt.tight_layout()
        plt.show()

        # 5. Correlation Heatmap
        plt.figure(figsize=(8,5))
        sns.heatmap(df[['temperature', 'rainfall', 'humidity', 'wind_speed']].corr(), annot=True)
        plt.title('Correlation Between Variables')
        plt.tight_layout()
        plt.show()

    # --- Simple Weather Prediction ---
    def predict_weather(self):
        if self.dataset.df is None:
            messagebox.showerror("Error", "Load dataset first!")
            return

        today = self.dataset.df.iloc[-1]

        if today['humidity'] > 80:
            prediction = "High chance of rain tomorrow."
        elif today['temperature'] > 30:
            prediction = "Likely sunny and hot tomorrow."
        else:
            prediction = "Moderate weather expected."

        messagebox.showinfo("Weather Prediction", prediction)

    # --- Turtle Animation for Rain ---
    def weather_animation(self):
        screen = turtle.Screen()
        screen.title("Weather Animation - Rainy Day")
        screen.bgcolor("skyblue")
        screen.setup(width=800, height=600)

        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)

        for _ in range(100):
            t.penup()
            x = random.randint(-400, 400)
            y = random.randint(0, 300)
            t.goto(x, y)
            t.pendown()
            t.color("blue")
            t.forward(10)

        turtle.done()

# --- Main Driver Code ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ClimaTrackApp(root)
    root.geometry("400x400")
    root.mainloop()
