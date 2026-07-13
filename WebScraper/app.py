from bs4 import BeautifulSoup
import requests

url= 'https://soti.net/mc/help/javascriptapi/en/index.html'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())
    print(soup.title.string)
else:
    print("Error: Unable to retrieve the webpage")


for link in soup.find_all('a'):
    print(link.get('href'))



