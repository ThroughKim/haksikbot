import requests
from bs4 import BeautifulSoup
from urllib2 import urlopen
import datetime

def get_menu():
    html = urlopen('http://dgucoop.dongguk.edu/store/store.php?w=4&l=2&j=0')
    source = html.read()
    html.close()
    soup = BeautifulSoup(source)
    table_div = soup.find(id="sdetail")
    tables = table_div.find_all("table")
    menu_table = tables[1]
    trs = menu_table.find_all('tr')
    """
    cafeterias = dict(
        sang_bek = trs[8],
        sang_ill = trs[10],
        sang_yang = trs[12],
        sang_dduk = trs[14],
        sot_1 = trs[18],
        sot_2 = trs[19],
        sot_3 = trs[20],
        sot_4 = trs[21],
        sot_5 = trs[22],
        gru_a = trs[26],
        gru_b = trs[28],
        pan  = trs[30],
        noodle = trs[31],
        arisu = trs[33]
    )
    """
    cafeterias = [
        trs[8],
        trs[10],
        trs[12],
        trs[14],
        trs[18],
        trs[19],
        trs[20],
        trs[21],
        trs[22],
        trs[26],
        trs[28],
        trs[30],
        trs[31],
        trs[33]
    ]

    today_date = datetime.date.today()

    menu_list = []

    for cafeteria in cafeterias:
        tds = cafeteria.find_all('td')
        menu = tds[today_date.isoweekday() + 2].span.text
        menu_list.append(menu)

    message = menu_list

    return(message)