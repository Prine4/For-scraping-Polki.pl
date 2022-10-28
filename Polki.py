import requests
import selenium
import time 
	
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options  
from selenium import webdriver
from bs4 import BeautifulSoup


chrome_options = Options()
chrome_options.add_argument("--headless") 
driver = webdriver.Chrome(chrome_options=chrome_options)

page = 'https://polki.pl/po-godzinach/z-zycia-wziete,.html'
rejectCookiesXPATH = "//button[@class='tcf277-button tcf277-button--slim accept-targeting-disclaimer-button']"
positionOfLinks = "//div[@class='row list-box small-up-1 medium-up-3']"

def delete_cookies():

	driver.get(page)
	
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, rejectCookiesXPATH)))
	driver.find_element(By.XPATH, rejectCookiesXPATH).click()	
	
def get_links():
	
	
	el = driver.find_element(By.XPATH, positionOfLinks)
	if el:
		url = el.get_attribute('href')
		if url is not None:
			for i in url:
				print(url)

		else:
			print('dupa')

delete_cookies()

get_links()
