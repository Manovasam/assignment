import pytest
from selenium import webdriver
from pages.home_page import HomePage
import allure

@allure.feature('Home Page Test')
class TestHomePage:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        yield
        self.driver.quit()

    @allure.story('Validate Home Page Elements and Navigation')
    def test_home_page_flow(self):
        with allure.step("Load Home Page"):
            self.home_page.load_page()

        with allure.step("Wait for loading animation to disappear"):
            self.home_page.wait_for_loading()

        with allure.step("Check main content visibility"):
            assert self.home_page.is_main_content_visible(), "Main content not visible"

        with allure.step("Click My Dreams Button and verify new tabs"):
            original_window = self.driver.current_window_handle
            self.home_page.click_my_dreams_button()
            WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
            assert len(self.driver.window_handles) == 3, "Expected 3 tabs/windows to be open"
