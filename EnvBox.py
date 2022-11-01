from typing import List
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.core.utils import read_version_from_cmd, PATTERN
from selenium.webdriver.chrome.options import Options

CONFIG_PATH = 'config.json'

class EnvBox:

    def __init__(self) -> None:

        self.LAST_PAGE =\
                3

        self.PAGE =\
            "https://polki.pl/po-godzinach/z-zycia-wziete,1.html"
                
        self.REJECT_COOKIES_XPATH =\
            "//button[@class='tcf277-button tcf277-button--slim accept-targeting-disclaimer-button']"
            
        self.POSITION_OF_LINKS =\
            "//div[@class='row list-box small-up-1 medium-up-3']"
            
        self.ONLY_ARTICLE_LINKS_CSS =\
            'div[class=text-box] a'
        
        self.PATH_TO_CHROMIUM =\
            '/usr/bin/chromium-browser'
