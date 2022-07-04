import requests
from datetime import datetime

key = '52c457badebc350feaaae7d514fa8248'

now = datetime.now()

def weatherAPI(city):

    URL = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+key

    response = requests.get(URL)

    name = response.json()['name']

    temp = int(response.json()['main']['temp'] - 273.15)

    status = response.json()['weather'][0]['description']

    humidity = response.json()['main']['humidity']

    date = now.strftime("%d/%m/%Y %H:%M")
    

    return temp, status, humidity, date,name

