from dataclasses import dataclass, field

import requests
from bs4 import BeautifulSoup


@dataclass
class Website:
    webs: list = field(default_factory=list)


web = Website()
url = 'https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites'
response = requests.get(url)
page = BeautifulSoup(response.text, 'lxml')
quotes = page.find('table')
trs = quotes.find_all('tr')
for tr in trs:
    B = []
    tds = tr.find_all('td')
    for td in tds:
        string = td.text.rstrip()
        while '[' in string:
            quote1 = string.find('[')
            quote2 = string.find(']')
            string = string[:quote1] + string[quote2+1:]
        B.append(string)
    if len(B) != 0:
        B[1] = B[1].replace(',', '')
        B[1] = B[1].replace('.', '')
        x = ''
        for el in B[1]:
            if el in '0123456789':
                x += el
            else:
                break
        B[1] = x
        web.webs.append(B)
parametrs = [10**7, 1.5 * 10**7, 5 * 10**7, 10**8, 5 * 10**8,
             10**9, 1.5 * 10**9]
for param in parametrs:
    for website in web.webs:
        if int(website[1]) < param:
            print(f'{website[0]} (Frontend:{website[2]}|Backend:', end='')
            print(f'{website[3]}) has {website[1]} unique visitors', end=' ')
            print(f'per month. (Expected more than {int(param)})')
            print()
