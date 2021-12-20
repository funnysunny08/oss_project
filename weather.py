import requests
from bs4 import BeautifulSoup
from urllib import parse
from info import gu, dong

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

gu_url = parse.quote(gu)
dong_url = parse.quote(dong)
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={}+{}+%EB%82%A0%EC%94%A8'.format(
    gu_url, dong_url)

data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

weather = soup.select_one(
    '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div.temperature_info > p > span.weather.before_slash').text
gion = soup.select_one(
    '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div.weather_graphic > div.temperature_text > strong').text
