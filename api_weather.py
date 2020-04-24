import requests
import sys
import json


'''weather_request = 'https://api.weather.yandex.ru/v1/forecast/'

headers = {'X-Yandex-API-Key': '6b963e22-5fa2-47e6-8a49-d67a12dd9793'}
w_params = {'lat': '37.490971',
            'lon': '55.829152',
            'lang': 'ru_RU'
}
response = requests.get(weather_request, headers=headers, params=w_params)
# response = requests.get(weather_request)'''


class Weather:
    def __init__(self, ask):
        question = ask

        weather_request = 'https://api.weather.yandex.ru/v1/forecast/'

        headers = {'X-Yandex-API-Key': '6b963e22-5fa2-47e6-8a49-d67a12dd9793'}
        w_params = {'lat': '37.490971',
                    'lon': '55.829152',
                    'lang': 'ru_RU'
                    }
        response = requests.get(weather_request, headers=headers,
                                params=w_params)

        if response:
            json_response = response.json()
            print(json_response['fact']['season'])
        else:
            print("Ошибка выполнения запроса:")
            print(weather_request)
            print("Http статус:", response.status_code, "(", response.reason,
                  ")")
            sys.exit(1)