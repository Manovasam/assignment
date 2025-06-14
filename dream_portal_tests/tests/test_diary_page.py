import pytest
from selenium import webdriver
from pages.diary_page import DiaryPage
import allure

@allure.feature('Diary Page Test')
class TestDiaryPage:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://arjitnigam.github.io/myDreams/dreams-diary.html")
        self.diary_page = DiaryPage(self.driver)
        yield
        self.driver.quit()

    @allure.story('Validate Dream Table Data')
    def test_dreams_table(self):
        with allure.step("Extract dream table data"):
            dreams = self.diary_page.get_dreams_data()

        with allure.step("Check number of dreams"):
            assert len(dreams) == 10, "Dream count should be 10"

        with allure.step("Validate dream types and content"):
            for dream in dreams:
                assert dream["type"] in ["Good", "Bad"], f"Invalid dream type: {dream['type']}"
                assert dream["name"], "Dream name is empty"
                assert dream["days_ago"], "Days ago is empty"
