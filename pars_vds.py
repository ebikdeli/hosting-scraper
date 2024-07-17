from drivers.chrome import start_driver
from selenium import webdriver
import time

# Add options to chrome driver
driver = start_driver()
if driver is not None:
    driver.get('https://www.zoomg.ir/cinema-articles/369521-presumed-innocent-tv-show-introduction/')
    time.sleep(3)
    driver.close()