from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from EnvBox import EnvBox
from Utils import WebUtils
from Builder import ChromeDriverBuilder



def delete_cookies():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, env.REJECT_COOKIES_XPATH)))
    driver.find_element(By.XPATH, env.REJECT_COOKIES_XPATH).click()


def get_links():
    div_list_with_links = driver.find_elements(By.XPATH, env.POSITION_OF_LINKS)
    links = []

    for div in div_list_with_links:
        links.extend(div.find_elements(By.CSS_SELECTOR, env.ONLY_ARTICLE_LINKS_CSS))

    res = []
    for link in links:
        res.append(link.get_attribute('href'))
    return res


def get_article(links):
    pass


options = []
# options.append('--headless')

env = EnvBox()
driver = ChromeDriverBuilder.createChromiumDriaver(env.PAGE, env.PATH_TO_CHROMIUM, options)
webUtils = WebUtils(driver)
    
delete_cookies()
article_links = get_links()

for link in article_links:
    print(link)