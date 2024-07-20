from drivers import chrome
from selenium.webdriver.common.by import By
from hosts.parse_url import extract_host_file_urls
import time



def start(connection:object, wait:int=1) -> None:
    """Start scraping iranserver"""
    driver = chrome.start_driver(False)
    if driver is not None:
        # Look for specified urls in 'parsvds.txt' file
        urls = extract_host_file_urls('iranserver')
        for url in urls:
            driver.get(url)
            time.sleep(wait)
            prices = []
            products_elem = driver.find_elements(By.CSS_SELECTOR, '#iran .owl-item')
            for pe in products_elem:
                price = pe.text.replace(',', '')
                for p in price.split(' '):
                    if p.isdigit():
                        print(int(p))
        driver.close()
