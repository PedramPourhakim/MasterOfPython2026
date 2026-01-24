from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
import requests

# Builder.load_file("main.kv")
# class CustomLabel(Label):
#     pass
Window.size = (400, 300)
class OpenMeteoProvider:

    base_url = "https://api.open-meteo.com/v1/forecast"


    def get_current_weather(self, lat, lon):

        params = {

            "latitude": lat,

            "longitude": lon,

            "current": "temperature_2m,relative_humidity_2m"

        }

        response = requests.get(self.base_url, params=params)

        normalize_data = {"temp": response.json()["current"]["temperature_2m"],

                          "humidity": response.json()["current"]["relative_humidity_2m"]}

        return normalize_data

class WeatherGUIApp(App):
    def build(self):
        # return CustomLabel()
        main_layout = BoxLayout(orientation='vertical', padding=10,spacing=10)
        self.lat_entry = TextInput(hint_text='Enter Latitude', padding=10,
                                   size_hint_y=None, height=50, multiline=False)
        self.lon_entry = TextInput(hint_text='Enter Longitude', padding=10,
                                   size_hint_y=None, height=50, multiline=False)
        fetch_btn = ToggleButton(text='Fetch weather data', size_hint_y=None, height=50)
        fetch_btn.bind(on_press=self.fetch_current_weather)
        self.result_layout = BoxLayout(orientation='vertical', padding=10,spacing=10)
        self.no_result = Label(text="no data yet")
        main_layout.add_widget(self.lat_entry)
        main_layout.add_widget(self.lon_entry)
        main_layout.add_widget(fetch_btn)
        main_layout.add_widget(self.result_layout)
        self.result_layout.add_widget(self.no_result)
        return main_layout

    def show_info(self,temp=27,humidity=50):
        self.result_layout.clear_widgets()
        temp_label = Label(text=f"Temperature: {temp}",size_hint_y=None, height=30)
        humidity_label = Label(text=f"Humidity : {humidity} %",size_hint_y=None, height=30)
        self.result_layout.add_widget(temp_label)
        self.result_layout.add_widget(humidity_label)

    def fetch_current_weather(self,instance):
        lat = self.lat_entry.text
        lon = self.lon_entry.text
        provider = OpenMeteoProvider()
        self.result_layout.clear_widgets()
        loading_label = Label(text = "Loading data...")
        self.result_layout.add_widget(loading_label)
        result = provider.get_current_weather(float(lat),float(lon))
        self.show_info(result.get("temp"),result.get("humidity"))


if __name__ == '__main__':
    WeatherGUIApp().run()
