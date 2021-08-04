import requests
from bs4 import BeautifulSoup


def weather(city):

#    city = input("City : ")
    url = "https://www.google.com/search?q="+city+"+weather"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    a = soup.find_all("div", class_="BNeawe iBp4i AP7Wnd")[0].get_text()
    b = soup.find_all("div", class_="BNeawe tAd8D AP7Wnd")[0].get_text()
    c = soup.find_all("div", class_= "BNeawe vvjwJb AP7Wnd")[1].get_text().split(":")[0]


    return a, b, c
