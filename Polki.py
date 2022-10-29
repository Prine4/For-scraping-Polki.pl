from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

page = 'https://polki.pl/po-godzinach/z-zycia-wziete,.html'
rejectCookiesXPATH = "//button[@class='tcf277-button tcf277-button--slim accept-targeting-disclaimer-button']"
positionOfLinks = "//div[@class='row list-box small-up-1 medium-up-3']"
webdriver_path = 'chromedriver_linux64/chromedriver'

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)
driver.get(page)


def delete_cookies():
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, rejectCookiesXPATH)))
    driver.find_element(By.XPATH, rejectCookiesXPATH).click()


def get_links():
    div_list_with_links = driver.find_elements(By.XPATH, positionOfLinks)
    links = []

    for div in div_list_with_links:
        links.extend(div.find_elements(By.CSS_SELECTOR, 'div[class=text-box] a'))

    res = []
    for link in links:
        res.append(link.get_attribute('href'))
    return res

def get_article(links):
    pass

delete_cookies()
article_links = get_links()
get_article(article_links)
