import requests
api_key="0bfac58f31ce2c98dedcca6e7c0a24a8"
user_input=input("Enter city:")

weather_data=requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
print(weather_data.json())
weather=weather_data.json()['weather'][0]['main']
temp=round(weather_data.json()['main']['temp'])
humidity=round(weather_data.json()['main']['humidity'])
print(f"The weather in {user_input} is:{weather}")
print(f"The temperature in {user_input} is:{temp}°F")
print(f"The humidity in {user_input} is:{humidity}")


