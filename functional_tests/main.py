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
        self.browser.implicitly_wait(10)
        self.browser.maximize_window()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_app(self):
        self.browser.get(f"{self.BASE_URL}")

    def test_create_patient(self):
        self.browser.get(f"{self.BASE_URL}/")
        self.assertIn("MedSafe Health Management Information System", self.browser.title)
    
        # user see no patient record, and decides to create one
        # user click the "Create Patient button and sees an open modal"
        action = ActionChains(self.browser)
        create_activator = self.browser.find_element(
            By.CSS_SELECTOR, f'#create_patient_modal_activator'
        )
        action.click(create_activator)
        action.perform()

        patient_modal = self.browser.find_element(
            By.CSS_SELECTOR, "#create_patient_modal.inview"
        )
        self.assertTrue(patient_modal)

        # user fills in form to create patient
        firstName = self.browser.find_element(By.CSS_SELECTOR, "#firstName")
        action.click(firstName)
        action.send_keys("Phillip")

        middleName = self.browser.find_element(By.CSS_SELECTOR, "#middleName")
        action.click(middleName)
        action.send_keys("Paul")

        lastName = self.browser.find_element(By.CSS_SELECTOR, "#lastName")
        action.click(lastName)
        action.send_keys("Mugisa")

        NIN = self.browser.find_element(By.CSS_SELECTOR, "#NIN")
        action.click(NIN)
        action.send_keys("CME14234249VNEK")

        age = self.browser.find_element(By.CSS_SELECTOR, "#age")
        action.click(age)
        action.send_keys("22")

        gender = self.browser.find_element(By.CSS_SELECTOR, "#gender")
        action.click(gender)
        action.send_keys("Male")

        phoneNumber = self.browser.find_element(By.CSS_SELECTOR, "#phoneNumber")
        action.click(phoneNumber)
        action.send_keys("0783245726")

        email = self.browser.find_element(By.CSS_SELECTOR, "#email")
        action.click(email)
        action.send_keys("paulphillip@medsafe.com")

        address = self.browser.find_element(By.CSS_SELECTOR, "#address")
        action.click(address)
        action.send_keys("Kampala")

        NOK_firstName = self.browser.find_element(By.CSS_SELECTOR, "#NOK_firstName")
        action.click(NOK_firstName)
        action.send_keys("Alex")

        NOK_lastName = self.browser.find_element(By.CSS_SELECTOR, "#NOK_lastName")
        action.click(NOK_lastName)
        action.send_keys("Peter")
        
        NOK_nin = self.browser.find_element(By.CSS_SELECTOR, "#NOK_nin")
        action.click(NOK_nin)
        action.send_keys("BWEUB238237")

        NOK_relationship = self.browser.find_element(By.CSS_SELECTOR, "#NOK_relationship")
        action.click(NOK_relationship)
        action.send_keys("Brother")

        NOK_phoneNumber = self.browser.find_element(By.CSS_SELECTOR, "#NOK_phoneNumber")
        action.click(NOK_phoneNumber)
        action.send_keys("0756382631")

        NOK_Gender = self.browser.find_element(By.CSS_SELECTOR, "#NOK_Gender")
        action.click(NOK_Gender)
        action.send_keys("Male")

        NOK_address = self.browser.find_element(By.CSS_SELECTOR, "#NOK_address")
        action.click(NOK_address)
        action.send_keys("Mukono")

        action.perform()
        
        # user clicks save button
        save_cta = self.browser.find_element(By.CSS_SELECTOR, "#create_patient_modal.inview .modal-footer .save")
        action.move_to_element(save_cta)
        action.click(save_cta)
        action.perform()

        # modal is closed
        # self.assertFalse(self.browser.find_element(By.CSS_SELECTOR, "#create_patient_modal.inview"))

        # user sees the new patient record in table
        new_record = self.browser.find_element(
            By.CSS_SELECTOR, f'table tr[data-row="0"] td[data-value="fullname"]'
        )
        self.assertTrue(new_record)
        self.assertEqual(new_record.text, "Phillip Paul Mugisa")

    def test_patients_app(self):
        self.browser.get(f"{self.BASE_URL}/")
        self.assertIn("MedSafe Health Management Information System", self.browser.title)

        # user clicks on a table record
        selected_row = self.browser.find_element(
            By.CSS_SELECTOR, f'table tr[data-row="0"]'
        )

        self.assertTrue(selected_row)
        patient_name = selected_row.find_element(
            By.CSS_SELECTOR, f'td[data-value="fullname"]'
        )
        selected_row.click()

        # user sees prerview area
        preview_detail = self.browser.find_element(
            By.CSS_SELECTOR, f'#preview_detials'
        )
        self.assertTrue(preview_detail)

        # user sees selected record name in preview
        self.assertEqual(patient_name.text, self.browser.find_element(By.CSS_SELECTOR, '#preview_patient_name').text)

    def test_patient_edit(self):
        self.browser.get(f"{self.BASE_URL}/")
        self.assertIn("MedSafe Health Management Information System", self.browser.title)

        # user clicks on a table record
        selected_row = self.browser.find_element(
            By.CSS_SELECTOR, f'table tr[data-row="0"]'
        )
        selected_row.click()
        
        # user sees prerview area
        self.assertTrue(self.browser.find_element(
            By.CSS_SELECTOR, f'#preview_detials'
        ))

        # user clicks edit btn
        self.browser.find_element(
            By.CSS_SELECTOR, f'#editPatientDetails'
        ).click()

        # user see edit modal


    def test_visits_app(self):
        self.browser.get(f"{self.BASE_URL}/visits/")
        self.assertIn("MedSafe Health Management Information System - Visits", self.browser.title)
        

if __name__ == "__main__":
    unittest.main()