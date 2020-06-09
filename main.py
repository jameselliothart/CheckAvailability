from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from contextlib import contextmanager
import time
import subprocess


URL = 'https://www.homedepot.com/p/Husky-36-in-W-x-72-in-H-x-24-in-D-Steel-Garage-Gear-Cabinet-G3624W-US/206497845'

@contextmanager
def open_driver(options=Options()):
    driver = webdriver.Chrome(chrome_options=options)
    yield driver
    driver.quit()

def check_availability(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    with open_driver(chrome_options) as driver:
        driver.get(URL)
        time.sleep(1)
        out_of_stock = driver.find_elements_by_class_name('oos-online')
        if not out_of_stock:
            return f'Available!\n{url}'
        return out_of_stock[0].text


if __name__ == "__main__":
    message = check_availability(URL)
    subprocess.Popen(['notify-send', message])
