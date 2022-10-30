from typing import List
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.core.utils import read_version_from_cmd, PATTERN
from selenium.webdriver.chrome.options import Options

CONFIG_PATH = 'config.json'


class EnvBox:

    def __init__(self) -> None:
        self.PAGE =\
            "https://polki.pl/po-godzinach/z-zycia-wziete,.html"
                
        self.REJECT_COOKIES_XPATH =\
            "//button[@class='tcf277-button tcf277-button--slim accept-targeting-disclaimer-button']"
            
        self.POSITION_OF_LINKS =\
            "//div[@class='row list-box small-up-1 medium-up-3']"
            
        self.ONLY_ARTICLE_LINKS_CSS =\
            'div[class=text-box] a'


    def createChromiumDriaver(self, arguments: List = []):
        chrome_driver_manager = ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM,
            version=self.getChromiumVersion(),
        )
        
        chrome_options = Options()
        for arg in arguments:
            chrome_options.add_argument(arg)
    
        driver = webdriver.Chrome(chrome_driver_manager.install(), options=chrome_options)
        
        driver.get(self.PAGE)
    
        return driver

    # ta funkcja sprawdza która wersje chromoum masz zainstalowaną
    def getChromiumVersion(self, path='/usr/bin/chromium-browser') -> str | None:
        return read_version_from_cmd(f"{path} --version", PATTERN[ChromeType.CHROMIUM])
