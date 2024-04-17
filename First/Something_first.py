import Parcing_sites as ps
import Constants as cs
from bs4 import BeautifulSoup
import requests



#s = requests.session()
#tickets = ps.Virtualsite('', '', '')
#tickets1 = ps.Virtualsite('', '', '')
#tickets.request(st_useragent= cs.BRAUSERS[1], src=str(cs.SITES), page= cs.CITIES['Москва'] + '0304' + cs.CITIES['Ханой'] + '1')
#s.headers.update({'Referer': 'https://www.aviasales.ru', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36'})
#URL = 'https://www.aviasales.ru/search/UFA0104MOW1'
#data = s.get(URL)
#text = data.content
#soup = BeautifulSoup(text, "html.parser")
#print(str(soup))
#page = 1
#with open('./page_%d.html'% (page), 'w', encoding="utf-8") as output_file:
    #output_file.write(str(soup))
    #output_file.write(str(data.content))
#    output_file.write(str(data.text.encode('utf-8')))
#data = tickets.get_count('')
#page = 1
#with open('./page_%d.html'% (page), 'w') as output_file:
    #soup = BeautifulSoup()
tickets = ps.Virtualsite('', '', '')
daterange = ps.data_range('03/02/2023','07/02/2023')
date_list = list()
i = 0
for simple_date in daterange:
    i =+ 1
    str_simple_data = str(simple_date)
    date_list.append(str(simple_date))
print(date_list)
for date in date_list:
    tickets.dynamic_request(st_useragent= cs.BRAUSERS[2], src=str(cs.SITES), site=cs.CITIES['Москва'] + date +\
    cs.CITIES['Ханой'] + '1' + '?request_source=search_form', page=1)


