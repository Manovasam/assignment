import pytest
from selenium import webdriver
from pages.summary_page import SummaryPage
import allure

@allure.feature('Summary Page Test')
class TestSummaryPage:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://arjitnigam.github.io/myDreams/dreams-total.html")
        self.summary_page = SummaryPage(self.driver)
        yield
        self.driver.quit()

    @allure.story('Validate Summary Statistics')
    def test_summary_statistics(self):
        with allure.step("Verify Good Dreams count"):
            assert self.summary_page.get_stat("Good Dreams") == 6

        with allure.step("Verify Bad Dreams count"):
            assert self.summary_page.get_stat("Bad Dreams") == 4

        with allure.step("Verify Total Dreams count"):
            assert self.summary_page.get_stat("Total Dreams") == 10

        with allure.step("Verify Recurring Dreams count"):
            assert self.summary_page.get_stat("Recurring Dreams") == 2
