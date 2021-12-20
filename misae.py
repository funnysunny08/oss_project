import requests
from info import gu

response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')

city_air = response_data.json()

gus = city_air['RealtimeCityAir']['row']

PM = 0
danger = False

for place in gus:
    if place['MSRSTE_NM'] == gu:
        PM = place['PM10']
        if PM > 70:
            danger = True
