from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://localhost:8000')
browser.save_screenshot('screenshot.png')
browser.quit()