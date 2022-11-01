import requests
from bs4 import BeautifulSoup
from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from EnvBox import EnvBox
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



options = []
options.append('--headless')

env = EnvBox()

for PAGE_OF_POLKI in range(1,env.LAST_PAGE):
    page = "https://polki.pl/po-godzinach/z-zycia-wziete,"+str(PAGE_OF_POLKI)+".html"
    driver = ChromeDriverBuilder.createChromiumDriaver(page, env.PATH_TO_CHROMIUM, options)
        
    delete_cookies()
    article_links = get_links()

    for PAGE_SCRAPED, link in enumerate(article_links):
        print(link)

        REQUEST_PAGE = requests.get(link)
        soup = BeautifulSoup(REQUEST_PAGE.content, 'html.parser')
        FIND_DIV = soup.find('div', class_=('off-canvas-content'))
        FIND_ARTICLE = FIND_DIV.find('article', class_=('article'))
        lines = content = FIND_ARTICLE.find_all('p')

        file = open('/home/krzysztof/Desktop/Milion dolarów/Historie z Polki.pl/Historia:'+str(PAGE_OF_POLKI)+','+str(PAGE_SCRAPED), 'w')

        for line in lines:
            file.write(line.text)
        file.close()
