import requests
from bs4 import BeautifulSoup



response = requests.get('https://sports.ndtv.com/cricket/teams/105092-nepal-teamprofile/news')


html= BeautifulSoup(response.content,'html.parser')
traget_link = html.find('div',class_='img-gr')
print(traget_link.find_next('img').attrs['data-src'])
  