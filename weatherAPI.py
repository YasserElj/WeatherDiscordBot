import requests

#OpenWeatherMap API key
key = 'key'

def weatherAPI(city):

    URL = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+key

    response = requests.get(URL)

    name = response.json()['name']

    temp = int(response.json()['main']['temp'] - 273.15)

    status = response.json()['weather'][0]['description']

    humidity = response.json()['main']['humidity']
    

    return temp, status, humidity,name