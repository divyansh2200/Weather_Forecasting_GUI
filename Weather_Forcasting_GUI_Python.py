# f'http://api.weatherapi.com/v1/forecast.json?key=b5e01861b575475ca2f34339211003&q={location}&days=7'
import requests
import tkinter as tk
from PIL import Image, ImageTk

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Weather App')
        self.root.geometry('800x400')
        self.root.maxsize(800, 600)
        self.root.minsize(800, 400)
        self.root.configure(bg='#87ceeb')

        self.create_widgets()

    def create_widgets(self):
        self.create_labels()
        self.create_entry()
        self.create_weather_image()
        self.create_current_weather_frame()

    def create_labels(self):
        self.weather_app_label = tk.Label(self.root, text="WEATHER APP", font=("Consolas", "24", "bold italic"), bg='#000fff000', pady=5)
        self.weather_app_label.pack()

    def create_entry(self):
        self.location_text = tk.Entry(self.root, font=("Arial", "20"), width=30, borderwidth=2)
        self.location_text.bind('<Return>', self.weather_information)
        self.location_text.place(x=160, y=50)

    def create_weather_image(self):
        # ffd343
        self.weather_condition_image = tk.Label(self.root, bg='#87ceeb')  
        self.weather_condition_image.place(x=340, y=100)

    def create_current_weather_frame(self):
        self.current_weather_frame = tk.Frame(self.root)
        self.current_weather_frame.place(x=240, y=180)

        self.location_label = tk.Label(self.current_weather_frame, text="", font=("Times new roman", "20", "bold italic"))
        self.location_label.grid(row=0, column=0)

        self.temperature_label = tk.Label(self.current_weather_frame, text="", font=("Times new roman", "20", "bold italic"))
        self.temperature_label.grid(row=1, column=0)

        self.condition_label = tk.Label(self.current_weather_frame, text="", font=("Consolas", "14", "bold italic"))
        self.condition_label.grid(row=2, column=0)

    def get_image(self, url_img, image_name):
        url = requests.get(f'http:{url_img}')
        with open(image_name, 'wb') as f:
            f.write(url.content)
        self.weather_img = ImageTk.PhotoImage(Image.open(image_name))
        return self.weather_img

    def weather_request(self, location):
        api_key = "YOUR_API_KEY"  # Replace with your actual API key
        url = f'http://api.weatherapi.com/v1/forecast.json?key=b5e01861b575475ca2f34339211003&q={location}&days=7'
        data = requests.get(url).json()
        return data

    def weather_information(self, event):
        location = self.location_text.get()
        data = self.weather_request(location)

        name = data['location']['name']
        region = data['location']['region']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        today_weather_img = data['current']['condition']['icon']

        # Update current weather labels and image
        self.location_label.config(text=f'{name}, {region}')
        self.temperature_label.config(text=f'Temperature: {int(temp_c)}°C')
        self.condition_label.config(text=f'Condition: {condition}')
        self.weather_condition_image.config(image=self.get_image(today_weather_img, 'weather.png'))

        self.location_text.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
