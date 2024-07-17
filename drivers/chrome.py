from selenium import webdriver


def start_driver(headless:bool=True, ignore_image:bool=True, silent_mode:bool=True, disable_css:bool=True, timeout:int=20, implicit_wait:float=5) -> object:
    """Start chrome selenium driver with needed options. If successful returns Chrome Driver object otherwise return None"""
    # Add chrome options to enhance performance
    try:
        driver = None
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('headless')
        if ignore_image:
            options.add_argument('--blink-settings=imagesEnabled=false')
        # Selenium silent mode
        if silent_mode:
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # Following 'prefs' dictionary used for disable css (supposly) and optimize the code
        # Pass the argument 1 to allow and 2 to block (We need javascript to be loaded so we set it to 1)
        if disable_css:
            prefs = {'profile.default_content_setting_values': {'cookies': 2, 'images': 2, 'javascript': 2,
                                'plugins': 2, 'popups': 2, 'geolocation': 2,
                                'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2,
                                'mouselock': 2, 'mixed_script': 2, 'media_stream': 2,
                                'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2,
                                'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2,
                                'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2,
                                'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2,
                                'durable_storage': 2}}
            options.add_experimental_option(
                "prefs", prefs
            )
        else:
            # Atleast disable notifications
            options.add_experimental_option(
                "prefs", {"profile.default_content_setting_values.notifications": 2}
            )
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        # options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        options.add_argument('--disable-gpu')
        # Following 4 options are used to test if performance can get better
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-features=NetworkService")
        options.add_argument("--disable-features=VizDisplayCompositor")
        # Add options to chrome driver
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(timeout)
        driver.implicitly_wait(implicit_wait)
        driver.set_window_size(800, 600)
    except Exception as e:
        print(f'ERROR HAPPENED: {e.__str__()}')
    return driver
