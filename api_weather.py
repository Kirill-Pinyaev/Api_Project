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
    def __init__(self, city, ask):
        self.city = city
        self.question = ask
        print(self.city, self.question)

        weather_request = 'https://api.weather.yandex.ru/v1/forecast/'
        if all(self.search(self.city)):
            lat, lon = self.search(self.city)
            print(lat, lon)
            headers = {'X-Yandex-API-Key': '6b963e22-5fa2-47e6-8a49-d67a12dd9793'}
            w_params = {'lat': '37.490971',
                        'lon': '55.829152',
                        'lang': 'ru_RU'
                        }
            response = requests.get(weather_request, headers=headers,
                                    params=w_params)

            if response:
                json_response = response.json()
            # print(json_response['now_dt'])
            else:
                print("Ошибка выполнения запроса:")
            print(weather_request)
            print("Http статус:", response.status_code, "(", response.reason,
                  ")")
            sys.exit(1)
        else:
            print(self.search(self.city))

    def search(self, toponym):
        if toponym:
            geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

            geocoder_params = {
                "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
                "geocode": toponym,
                "format": "json"}

            response = requests.get(geocoder_api_server, params=geocoder_params)

            json_response = response.json()
            # print(json_response)
            #
            # print(json_response["response"]["GeoObjectCollection"]
            #       ["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]['kind'])

            # print(json_response)
            print(json_response["response"]["GeoObjectCollection"]
                  ["featureMember"][0]["GeoObject"]["metaDataProperty"][
                      "GeocoderMetaData"]['Address']['Components'][-1]['kind'])
            print(json_response["response"]["GeoObjectCollection"]
                  ["featureMember"][0]["GeoObject"]["metaDataProperty"][
                      "GeocoderMetaData"]['Address']['Components'][-1]['name'])

            toponym = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]

            toponym_coodrinates = toponym["Point"]["pos"]
            toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

            return [toponym_longitude, toponym_lattitude]
        else:
            return [None, None]
            print()
            print(toponym + 'err')
            print()

Weather("Казань", "погода")
# Weather("россия", "погода")
# Weather("", "погода")
# Weather("apple", "погода")
# print()
# print(Weather('moscow', ''))