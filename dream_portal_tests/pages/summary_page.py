from selenium.webdriver.common.by import By

class SummaryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_stat(self, label):
        stat = self.driver.find_element(By.XPATH, f"//li[contains(text(), '{label}')]")
        return int(stat.text.split(":")[-1].strip())
