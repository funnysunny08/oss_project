import requests
from info import dong, favorite

keyword = '{} {} 맛집'.format(dong, favorite)

client_id = "your_client_id"
client_secret = "your_client_secret"
headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}

url_base = "https://openapi.naver.com/v1/search/local.json?query="

url_middle = "&display=1&start=1&sort=comment"

url = url_base + keyword + url_middle

result = requests.get(url, headers=headers).json()

matjip = result['items'][0]['title']
