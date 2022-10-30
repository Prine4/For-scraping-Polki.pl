from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Utils to po angilsku narzędzia
class WebUtils:
    
    def __init__(self, driver, time_out = 10,) -> None:
        self.driver = driver
        self.time_out = time_out
    
    def wait_until_clickable(self, by: By, value):
        WebDriverWait(self.driver, self.time_out).until(EC.element_to_be_clickable((by, value)))