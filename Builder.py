from typing import List
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import read_version_from_cmd, PATTERN


class ChromeDriverBuilder:

    def createChromiumDriaver(page: str, path_to_chromium , arguments: List = []):
        chrome_driver_manager = ChromeDriverManager(
            chrome_type=ChromeType.CHROMIUM,
            version='106.0.5249.61'
        )

        chrome_options = Options()
        for arg in arguments:
            chrome_options.add_argument(arg)

        driver = webdriver.Chrome(
            chrome_driver_manager.install(), options=chrome_options)

        driver.get(page)

        return driver

    def getChromiumVersion(path) -> str | None:
        return read_version_from_cmd(f"{path} --version", PATTERN[ChromeType.CHROMIUM])
