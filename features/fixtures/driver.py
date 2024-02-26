import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


# def get_remote_driver(context, executor):
#     os.environ['DISPLAY'] = ':0'
#     if context.used_browser.lower() == "chrome":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--window-size=1920,1080")
#         options.add_argument('--no-sandbox')
#         options.add_argument('--disable-dev-shm-usage')
#         driver = webdriver.Remote(command_executor=executor, options=options)
#     else:
#         raise ValueError("Invalid used_browser")
#     return driver


def get_local_driver(context):
    if context.used_browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if context.debug:
            options.add_experimental_option("detach", True)
        if context.headless:
            options.add_argument('--headless')
        # optional - using Webdriver Manager (now surpassed by Selenium's own Selenium Manager)
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError("Invalid used_browser")
    return driver
