# busco la url del resultado
class Results:
    def __init__(self, driver):
        self.driver = driver

    def google_results(self):
        return self.driver.current_url
