import requests
from bs4 import BeautifulSoup

kuids = str(input('Insert kuids: '))
url = 'https://kuid.trainz-mp.ru/search.php'

data = {'query': kuids, 'type': '2'}
session = requests.Session()
response = session.post(url, data=data)

soup = BeautifulSoup(response.text, 'lxml')
table = soup.find('h1')
kuid_count = soup.find('b')
href = table.find('a').get('href')

num = ''

for c in kuid_count:
    if c.isdigit():
        num = num + c

num = (int(num)/50)
url_of_kuids = 'https://kuid.trainz-mp.ru/' + href

response = session.get(url_of_kuids)
soup = BeautifulSoup(response.text, 'lxml')
page_count = soup.find_all('a')

kuid_list = []
i = 0

while i <= num:
    i = i + 1
    kuid_url = ('https://kuid.trainz-mp.ru/' + href + '/?p=' + str(i))
    response = session.get(kuid_url)
    soups = BeautifulSoup(response.text, 'lxml')
    body = soups.find('body')
    table = body.find('table', class_='items-table')
    td = table.find('tbody', class_='')
    kuid_url = table.find_all('tr', class_='')
    for kuid in kuid_url:
        kuid_link = kuid.find('a').get('href')
        kuid_list.append(kuid_link)

number = 0

for element in kuid_list:
    if 'kuid/' in element:
        kuid_url = 'https://kuid.trainz-mp.ru/' + element
        response = session.get(kuid_url).text
        soup = BeautifulSoup(response, 'lxml')
        search_h2 = soup.find('h2')
        download_url = search_h2.find('a').get('href')
        url_of_kuid = ('https://kuid.trainz-mp.ru/' + download_url)
        url_content = session.get(url_of_kuid).content
        number = number + 1
        with open(f'D:/dfolder/{number}.cdp', 'wb') as file:
            file.write(url_content)
