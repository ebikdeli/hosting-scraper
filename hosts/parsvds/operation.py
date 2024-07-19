from drivers.chrome import start_driver
from selenium.webdriver.common.by import By
from hosts.parse_url import extract_host_file_urls
import time



def start(wait:int=1) -> None:
    """Start scraping ParsVDS"""
    driver = start_driver(False)
    if driver is not None:
        # Look for specified urls in 'parsvds.txt' file
        urls = extract_host_file_urls('parsvds')
        for url in urls:
            driver.get(url)
            time.sleep(wait)
            prices = []
            prices_elem = driver.find_elements(By.CSS_SELECTOR, '.server-order-button')
            for pe in prices_elem:
                price = pe.text.replace(',', '')
                for p in price.split(' '):
                    if p.isdigit():
                        print(int(p))
        driver.close()
