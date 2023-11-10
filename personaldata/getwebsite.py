from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


WAIT_FOR_PAGE = 1  # wait 1 second for website to load


class GetWebsiteMixin:
    def get_website_html(self, url):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        # executable_path=driver_path)
        driver = webdriver.Chrome(options=chrome_options)
        # Go to the website
        driver.get(url)
        # Get the content of the website
        time.sleep(WAIT_FOR_PAGE)
        return driver.page_source
