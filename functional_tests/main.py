# django
import os, time
import unittest

# selenium
import selenium
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ServerStatusTest(unittest.TestCase):
    """
        This test if the server is able to start, and all endpoints are working
    """

    def setUp(self):
        self.BASE_URL = "http://localhost:8000"

        # run with hidden window
        options = Options()
        options.add_argument("--headless")

        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service, options=options)
        self.browser.implicitly_wait(5)
        # self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_app(self):
        self.browser.get(f"{self.BASE_URL}")

    def test_patients_app(self):
        self.browser.get(f"{self.BASE_URL}/")
        self.assertIn("MedSafe Health Management Information System", self.browser.title)

        # user clicks on a table record
        selected_row = self.browser.find_element(
            By.CSS_SELECTOR, f'table tr[data-row="1"]'
        )
        self.assertTrue(selected_row)
        patient_name = selected_row.find_element(
            By.CSS_SELECTOR, f'td[data-value="name"]'
        )
        print("patient_name:", patient_name)
        selected_row.click()

        # user sees prerview area
        preview_detail = self.browser.find_element(
            By.CSS_SELECTOR, f'#preview_detials'
        )
        self.assertTrue(preview_detail)

        # user sees selected record name in preview
        self.assertEqual(patient_name.text, self.browser.find_element(By.CSS_SELECTOR, '#preview_patient_name').text)


    def test_visits_app(self):
        self.browser.get(f"{self.BASE_URL}/visits/")
        self.assertIn("MedSafe Health Management Information System - Visits", self.browser.title)

if __name__ == "__main__":
    unittest.main()