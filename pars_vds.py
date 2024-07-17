from drivers.chrome import start_driver
import time



def start(wait:int=0) -> None:
    """Start scraping ParsVDS"""
    driver = start_driver()
    if driver is not None:
        driver.get('https://www.zoomg.ir/cinema-articles/369521-presumed-innocent-tv-show-introduction/')
        time.sleep(wait)
        driver.close()
