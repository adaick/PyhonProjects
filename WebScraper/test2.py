import requests
from bs4 import BeautifulSoup
# print('helllo')
# response = requests.get('https://www.google.com')
# print(response)
response = requests.get('https://api.covid19api.com/summary')
response_json = response.json()
print(response_json)