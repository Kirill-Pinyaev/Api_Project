import requests

response = requests.get("https://api.weather.yandex.ru/v1/forecast/")

headers = {'X-Yandex-API-Key': '6b963e22-5fa2-47e6-8a49-d67a12dd9793'}


print(response, type(response))