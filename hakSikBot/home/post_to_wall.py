import facebook
import requests
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen


def write_post():
    post_token = 'CAAIIAeqKJNgBAKoZCCoLCh3kuQl6HNmrIL0jZBTfCJHjZBqhkZAyNTUPNipqG5TtAXVPFoBd7Jb19x996EorcQSLIELZCy8z6ZASFZAFQHWVg3PQTZAyUS9mLHJ2BEEr3IpsMXEMZBZBS2uD5aZBOeT1o6YRHqCCuQVA9gryRE7vz1rJhCgyoZBU71j6'
    graph = facebook.GraphAPI(post_token)
    graph.put_object("1681679528749683", "feed", message=get_menu())


def get_fb_token(app_id, app_secret):
    redirect_uri = 'http://througkim.github.io'
    payload = {'grant_type': 'publish_stream', 'redirect_uri': redirect_uri, 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params=payload)
    result = file.text

    print(result)
    return result


def get_menu():
    html = urlopen('http://dgucoop.dongguk.edu/store/store.php?w=4&l=2&j=0')
    source = html.read()
    html.close()
    soup = BeautifulSoup(source, "lxml")
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

    message = "상록원-백반\r\n" + menu_list[0] + \
              "\r\n\r\n상록원-일품\r\n" + menu_list[1] + \
              "\r\n\r\n상록원-양식\r\n" + menu_list[2] + \
              "\r\n\r\n상록원-뚝배기\r\n" + menu_list[3] + \
              "\r\n\r\n솥앤누들-1\r\n" + menu_list[4] + \
              "\r\n\r\n솥앤누들-2\r\n" + menu_list[5] + \
              "\r\n\r\n솥앤누들-3\r\n" + menu_list[6] + \
              "\r\n\r\n솥앤누들-4\r\n" + menu_list[7] + \
              "\r\n\r\n솥앤누들-5\r\n" + menu_list[8] + \
              "\r\n\r\n그루터기-A\r\n" + menu_list[9] + \
              "\r\n\r\n그루터기-B\r\n" + menu_list[10] + \
              "\r\n\r\n팬앤누들-팬\r\n" + menu_list[11] + \
              "\r\n\r\n팬앤누들-누들\r\n" + menu_list[12] + \
              "\r\n\r\n아리수\r\n" + menu_list[13]

    return(message)

write_post()