import requests
import json
import win32com.client as wincom

city = input("Enter you city name: ")

url = f"https://api.weatherapi.com/v1/current.json?key=6e24d58e8c674040ae583901250609&q={city}"

r =  requests.get(url)
weather = json.loads(r.text)

degrees = weather["current"]["temp_c"]
cond = weather["current"]["condition"]["text"]

speak = wincom.Dispatch("SAPI.SpVoice")

text = f"Weather in {city} city is {degrees} degree celcius and today is {cond}"
speak.Speak(text)