import requests


api_key = "157238fcc58d1eefce0bcdeb404a32c2"

user_input = input("Enter the city: ")
url = f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}'
weather_data = requests.get(url)

if weather_data.json()["cod"] == 404:
    print("No city found")
else: 
    weather = weather_data.json()["weather"][0]["main"]
    temp = round(weather_data.json()["main"]["temp"])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp} F")
