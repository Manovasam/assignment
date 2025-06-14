from selenium.webdriver.common.by import By

class DiaryPage:
    def __init__(self, driver):
        self.driver = driver
        self.table_rows = (By.XPATH, "//table/tbody/tr")

    def get_dreams_data(self):
        rows = self.driver.find_elements(*self.table_rows)
        dream_entries = []
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            dream_entries.append({
                "name": cols[0].text.strip(),
                "days_ago": cols[1].text.strip(),
                "type": cols[2].text.strip()
            })
        return dream_entries
