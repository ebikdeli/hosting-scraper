from drivers.chrome import start_driver
from selenium.webdriver.common.by import By
import time



def start(wait:int=0) -> None:
    """Start scraping ParsVDS"""
    driver = start_driver(False)
    if driver is not None:
        driver.get('https://parsvds.com/virtual-server/iran-ssd/')
        # time.sleep(wait)
        prices = []
        prices_elem = driver.find_elements(By.CSS_SELECTOR, '.server-order-button')
        for pe in prices_elem:
            price = pe.text.replace(',', '')
            for p in price.split(' '):
                if p.isdigit():
                    print(int(p))
        driver.close()
