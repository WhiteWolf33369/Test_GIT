# Импортируем модуль
import requests
from bs4 import BeautifulSoup
from lxml import html
import Constants as cs
from selenium import webdriver as wb
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import datetime
import pandas as pd
import time

# создаем класс виртуальных сайтов
class Virtualsite:
    # Стандартная функцция Init
    def __init__(self, name: object, headers: object, req: object) -> object:
        self.name = name
        self.headers = headers
        self.req = req
        self.session = requests.session()

    # создаем запрос на сайт, st_accept- желаемый формат получения данных, st_useragent - данные браузера,
    # с которого отправляется запрос. page- страница сайта(В нынешнем случае валюта)
    def request(self, st_accept="text/html",st_referer="", st_useragent="", src="", page=""):
        #self.headers = {"Accept": st_accept,
        #                "User-Agent": st_useragent}
        src1 = src + page
        print(src1)
        #self.req = requests.get(src1, self.headers)
        self.headers = {"Accept": st_accept,
            'Referer': st_referer,
                          'User-Agent': st_useragent}
        self.req = requests.get(src1)
        soup = BeautifulSoup(self.req.content, "html.parser")
        print(str(soup))
        page = 1
        with open('./page_%d.html' % (page), 'w', encoding="utf-8") as output_file:
            #output_file.write(str(self.req.text.encode('utf-8')))
            output_file.write(str(soup))
    def dynamic_request(self, st_accept="text/html",st_referer="", st_useragent="", src="", site='', page=1):
        #self.headers = {"Accept": st_accept,
        #                "User-Agent": st_useragent}
        src1 = src + site
        print(src1)
        #self.req = requests.get(src1, self.headers)
        self.headers = {"Accept": st_accept,
            'Referer': st_referer,
                          'User-Agent': st_useragent}
        #driver = wb.Chrome(service = ChromeService(executable_path = ChromeDriverManager().install))
        driver = wb.Chrome()
        driver.get(src1)
        #self.req = driver.get(src1)
        #time.sleep(20)
        #driver.implicitly_wait(20)
        #input('Press to print web page')
        self.req = driver.page_source
        time.sleep(20)
        soup = BeautifulSoup(str(self.req), "html.parser")
        #print(str(soup))
        #str_page = str(page)
        with open('./page_%d.html' % (page), 'w', encoding="utf-8") as output_file:
        # output_file.write(str(self.req.text.encode('utf-8')))
            output_file.write(str(soup))
        driver.close()
    # Получение значения нужных переменных
    def get_count(self, day = ""):
        soup = BeautifulSoup(str(self.req),'html.parser')
        #title = soup.find('span',{'class':'app_content'})
        items = soup.find_all('span',{'class':["s__FVoTcD1TH6rgNduZuYgA s__oXVxdY01BRdRDR1BPVh_ "
                                                "s__DhnUWRq_dnfbyy1pfoX2 s__sNYAKy6VBDAUbuW4TLqO", 'data-test-id']})
        list_of_times = []
        for item in items:
            #time = item.find('span', {'class': ["s__FVoTcD1TH6rgNduZuYgA s__oXVxdY01BRdRDR1BPVh_ "
            #                                    "s__DhnUWRq_dnfbyy1pfoX2 s__sNYAKy6VBDAUbuW4TLqO", 'data-test-id']})
            list_of_times.append(item.text)

        return list_of_times
        #tree = html.fromstring(str(self.req))
        #title_lxml = tree.xpath('//div[@class = "app_content"]')[0]

        #print(title[0])
        #print(title.string[0])
@staticmethod
def data_range(first_data = '' , final_data = ''):
    first_data1 = datetime.datetime.strptime(first_data, '%d/%m/%Y')
    final_data1 = datetime.datetime.strptime(final_data, '%d/%m/%Y')
#    first_data1 = datetime.datetime.strftime(first_data, '%d/%m/%Y')
#    final_data1 = datetime.datetime.strftime(final_data, '%d/%m/%Y')
    print(first_data1)
    print(final_data1)
    daterange = pd.date_range(first_data1, final_data1)
    #need_datarange = daterange.format(date_format='%d-%m-%Y %X')
    need_datarange = daterange.strftime(date_format='%d%m')
    return need_datarange





