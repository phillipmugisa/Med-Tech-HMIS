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
from selenium.webdriver.common.action_chains import ActionChains

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
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()
        
    def test_patients_api(self):
        self.browser.get(f"{self.BASE_URL}/api/patients/")
        self.assertIn("Patient List", self.browser.title)

        self.browser.get(f"{self.BASE_URL}/api/patients/create/")
        self.assertIn("Patient Create", self.browser.title)
        

if __name__ == "__main__":
    unittest.main()