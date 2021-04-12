# Importo las librerias necesarias
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# voy a la pagina de resultados de google y hago click en el primer resultado
class GoogleResults:
    def __init__(self, driver):
        self.driver = driver
        self.first_result = (By.LINK_TEXT, 'The Name of the Wind - Patrick Rothfuss')

    def google_results(self):
        return self.driver.current_url

    def google_first_results(self):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.first_result)).text

    def google_first_results_click(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.first_result)).click()
