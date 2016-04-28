#!/root/.pyenv/versions/py3.4.1/bin/python3.4

import facebook
import datetime
from selenium import webdriver
from pyvirtualdisplay import Display


def write_post():

    today_date = datetime.date.today().strftime('%m월 %d일')
    post_token = 'CAAIIAeqKJNgBAKoZCCoLCh3kuQl6HNmrIL0jZBTfCJHjZBqhkZAyNTUPNipqG5TtAXVPFoBd7Jb19x996EorcQSLIELZCy8z6ZASFZAFQHWVg3PQTZAyUS9mLHJ2BEEr3IpsMXEMZBZBS2uD5aZBOeT1o6YRHqCCuQVA9gryRE7vz1rJhCgyoZBU71j6'
    graph = facebook.GraphAPI(post_token)
    #graph.put_object("1681679528749683", "feed", message=get_menu())
    get_screenshot()
    photo = open("screenshot.png", "rb")
    graph.put_photo(message=today_date + "의 점심 식단표입니다~ \r\n식단표는 매일 오전 11시에 게시됩니다. \r\n도움이 되셨다면 좋아요 눌러주세요~~!!", image=photo.read())
    photo.close()

def get_screenshot():
    display = Display(visible=0, size=(1024, 860))
    display.start()
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000')
    browser.save_screenshot('screenshot.png')
    browser.quit()
    display.stop()

write_post()
