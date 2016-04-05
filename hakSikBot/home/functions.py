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
    menu_dict = {}
    today_date = datetime.date.today()
    today_span_num = today_date.isoweekday() + 2
    
    sang_bek_tds = trs[8].find_all('td')
    sang_bek_today_spans = sang_bek_tds[today_span_num].find_all('span')
    sang_bek_today_menu = sang_bek_today_spans[0].text.replace("\r\n", "<br>")
    sang_bek_today_price = sang_bek_today_spans[1].text
    
    sang_ill_tds = trs[10].find_all('td')
    sang_ill_today_spans = sang_ill_tds[today_span_num].find_all('span')
    sang_ill_today_menu = sang_ill_today_spans[0].text.replace("\r\n", "<br>")
    sang_ill_today_price = sang_ill_today_spans[1].text

    sang_yang_tds = trs[12].find_all('td')
    sang_yang_today_spans = sang_yang_tds[today_span_num].find_all('span')
    sang_yang_today_menu = sang_yang_today_spans[0].text.replace("\r\n", "<br>")
    sang_yang_today_price = sang_yang_today_spans[1].text
    
    sang_dduk_tds = trs[14].find_all('td')
    sang_dduk_today_spans = sang_dduk_tds[today_span_num].find_all('span')
    sang_dduk_today_menu = sang_dduk_today_spans[0].text.replace("\r\n", "<br>")
    sang_dduk_today_price = sang_dduk_today_spans[1].text

    sangrok_dict = dict(
        sang_bek_today_menu=sang_bek_today_menu,
        sang_bek_today_price=sang_bek_today_price,
        sang_ill_today_menu=sang_ill_today_menu,
        sang_ill_today_price=sang_ill_today_price,
        sang_yang_today_menu=sang_yang_today_menu,
        sang_yang_today_price=sang_yang_today_price,
        sang_dduk_today_menu=sang_dduk_today_menu,
        sang_dduk_today_price=sang_dduk_today_price
    )
    menu_dict.update(sangrok_dict)

    sot_1_tds = trs[18].find_all('td')
    sot_1_today_spans = sot_1_tds[today_span_num].find_all('span')
    sot_1_menu = sot_1_today_spans[0].text.replace("\r\n", "<br>")
    sot_1_price = sot_1_today_spans[1].text

    sot_2_tds = trs[19].find_all('td')
    sot_2_today_spans = sot_2_tds[today_span_num].find_all('span')
    sot_2_menu = sot_2_today_spans[0].text.replace("\r\n", "<br>")
    sot_2_price = sot_2_today_spans[1].text

    sot_3_tds = trs[20].find_all('td')
    sot_3_today_spans = sot_3_tds[today_span_num].find_all('span')
    sot_3_menu = sot_3_today_spans[0].text.replace("\r\n", "<br>")
    sot_3_price = sot_3_today_spans[1].text

    sot_4_tds = trs[21].find_all('td')
    sot_4_today_spans = sot_4_tds[today_span_num].find_all('span')
    sot_4_menu = sot_4_today_spans[0].text.replace("\r\n", "<br>")
    sot_4_price = sot_4_today_spans[1].text

    sot_5_tds = trs[22].find_all('td')
    sot_5_today_spans = sot_5_tds[today_span_num].find_all('span')
    sot_5_menu = sot_5_today_spans[0].text.replace("\r\n", "<br>")
    sot_5_price = sot_5_today_spans[1].text

    sot_dict = dict(
        sot_1_menu=sot_1_menu,
        sot_1_price=sot_1_price,
        sot_2_menu=sot_2_menu,
        sot_2_price=sot_2_price,
        sot_3_menu=sot_3_menu,
        sot_3_price=sot_3_price,
        sot_4_menu=sot_4_menu,
        sot_4_price=sot_4_price,
        sot_5_menu=sot_5_menu,
        sot_5_price=sot_5_price
    )
    menu_dict.update(sot_dict)

    gru_a_tds = trs[26].find_all('td')
    gru_a_today_spans = gru_a_tds[today_span_num].find_all('span')
    gru_a_menu = gru_a_today_spans[0].text.replace("\r\n", "<br>")
    gru_a_price = gru_a_today_spans[1].text

    gru_b_tds = trs[28].find_all('td')
    gru_b_today_spans = gru_b_tds[today_span_num].find_all('span')
    gru_b_menu = gru_b_today_spans[0].text.replace("\r\n", "<br>")
    gru_b_price = gru_b_today_spans[1].text

    gru_dict = dict(
        gru_a_menu=gru_a_menu,
        gru_a_price=gru_a_price,
        gru_b_menu=gru_b_menu,
        gru_b_price=gru_b_price
    )
    menu_dict.update(gru_dict)

    pan_pan_tds = trs[30].find_all('td')
    pan_pan_menu = pan_pan_tds[today_span_num].text.replace("\r\n", "<br>")

    pan_noodle_tds = trs[31].find_all('td')
    pan_noodle_menu = pan_noodle_tds[today_span_num].text.replace("\r\n", "<br>")

    pan_dict = dict(
        pan_pan_menu=pan_pan_menu,
        pan_noodle_menu=pan_noodle_menu
    )
    menu_dict.update(pan_dict)

    arisu_menu = trs[33].find_all('td')[today_span_num].span.text.replace("\r\n", "<br>")
    arisu_dict = dict(arisu_menu=arisu_menu)
    menu_dict.update(arisu_dict)


    return(menu_dict)

