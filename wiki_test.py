import requests
from bs4 import BeautifulSoup
url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find('table')
trs = quotes.find_all('tr')
A = []
for tr in trs:
    B = []
    tds = tr.find_all('td')
    for td in tds:
        B.append(td.text.rstrip())
    if len(B) != 0:
        B[1] = B[1].replace(',','')
        B[1] = B[1].replace('.','')
        x = ''
        for el in B[1]:
            if el in '0123456789':
                x += el
            else:
                break
        B[1] = x
        A.append(B)
for el in A:
    print(el)
    print('*******************************')
