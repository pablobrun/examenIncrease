#Importo las librerias necesarias
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class googleIndex:
    def __init__(self, driver):
        self.driver = driver
        # busco los webelements necesarios en el index y realizo las busquedas
        self.query_input = (By.NAME, 'q')
        self.search_button = (By.NAME, 'btnK')
        self.google_sugestions = (By.CLASS_NAME, 'erkvQe')
        self.firs_sugestion = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul/li[1]')

    #Hago la busqueda haciendo click en el boton
    def google_search(self, search_text):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.query_input)).send_keys(search_text)

    def google_search_click(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.search_button)).click()

    #Hago la busqueda haciendo click en la sugerencia
    def google_dropdowm_sugestion(self):
        if WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.google_sugestions)):
            return True

    def google_sugestion(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.firs_sugestion)).click()

