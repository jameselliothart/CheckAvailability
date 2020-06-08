from selenium import webdriver
from contextlib import contextmanager
import time


URL = 'https://www.homedepot.com/p/Husky-36-in-W-x-72-in-H-x-24-in-D-Steel-Garage-Gear-Cabinet-G3624W-US/206497845'

@contextmanager
def open_driver(options=webdriver.ChromeOptions()):
    driver = webdriver.Chrome(chrome_options=options)
    yield driver
    driver.quit()

def check_availability(url):
    with open_driver() as driver:
        driver.get(URL)
        time.sleep(1)
        out_of_stock = driver.find_elements_by_class_name('oos-online')
        if not out_of_stock:
            return f'Available!\n{url}'
        return out_of_stock[0].text


if __name__ == "__main__":
    print(check_availability(URL))
