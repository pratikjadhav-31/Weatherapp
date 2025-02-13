import streamlit as st
import requests

# OpenWeatherMap API Key
API_KEY = 'bc6d3b0a96784d31021142f64d49cd00'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'

def get_weather(city_name):
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
    response = requests.get(complete_url)
    return response.json()

def main():
    st.title('Weather App')
    st.write('Enter the city name to get the weather information')

    city_name = st.text_input('City Name')

    if st.button('Get Weather'):
        if city_name:
            weather_data = get_weather(city_name)
            if weather_data['cod'] == 200:
                main = weather_data['main']
                wind = weather_data['wind']
                weather_desc = weather_data['weather'][0]['description']

                st.write(f"**Temperature:** {main['temp']} K")
                st.write(f"**Pressure:** {main['pressure']} hPa")
                st.write(f"**Humidity:** {main['humidity']} %")
                st.write(f"**Weather Description:** {weather_desc.capitalize()}")
                st.write(f"**Wind Speed:** {wind['speed']} m/s")
            else:
                st.error('City not found. Please enter a valid city name.')
        else:
            st.error('City name cannot be empty.')

if __name__ == '__main__':
    main()
