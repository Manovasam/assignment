from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.loading_icon = (By.ID, "loading")
        self.main_content = (By.ID, "mainContent")
        self.my_dreams_button = (By.LINK_TEXT, "My Dreams")

    def load_page(self):
        self.driver.get("https://arjitnigam.github.io/myDreams/")

    def wait_for_loading(self):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(self.loading_icon))

    def is_main_content_visible(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.main_content))

    def click_my_dreams_button(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.my_dreams_button)).click()
