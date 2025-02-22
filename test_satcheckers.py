# Generated by Selenium IDE
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

import smtplib

email = "zchen15@bostonk12.org"
location = "02132" #your zip code
distance = "100 miles" #whatever your want (has to be on the website as an option)
class TestSatchecker():
    def setup_method(self):
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.vars = {}
        self.actions = ActionChains(self.driver)

    def teardown_method(self):
        self.driver.quit()

    def test_satchecker(self):
        #self.driver = webdriver.Chrome(r"chromedriver")

        self.driver.get("https://satsuite.collegeboard.org/sat/test-center-search")

        #self.driver.set_window_size(1720, 1349)
        from selenium.webdriver.support.ui import Select

        # locate the dropdown element by id
        dropdown = Select(self.driver.find_element(By.ID, "apricot_select_4"))
        time.sleep(1)
        dropdown.select_by_visible_text("August 26, 2023 — Saturday") #change to match your wanted date
        #dropdown.select_by_value("2023-06-03")
        #self.driver.find_element(By.ID, "student").click()
        text_input = self.driver.find_element(By.ID, "apricot_input_5")
        text_input.send_keys(location)
        dropdown = Select(self.driver.find_element(By.ID, "apricot_select_6"))
        dropdown.select_by_visible_text(distance)
        button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Find a Test Center')]")
        button.click()
        time.sleep(1)
        # Find the element containing the desired text
        element = self.driver.find_element(By.XPATH, "//*[contains(text(),'Test centers with available seats')]")

        # Extract the text from the element
        text = element.text

        # Print the text
        print(text)
        import re
        try:
            number = int(re.findall(r'\d+', text)[0])
        except IndexError as e:
            self.test_satchecker()
        print(number)  # Output: 0



        # sending the mail
        if (number > 0):
            import smtplib

            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)

            # start TLS for security
            s.starttls()

            # Authentication
            s.login(email, "woyqfyvopjikowns")

            # message to be sent
            message = str(number) + "  Testing Centers Open"
            s.sendmail(email, email, message)

            # terminating the session
            s.quit()
        #time.sleep()



# send("completed the test for SAT")

checker = TestSatchecker()

checker.setup_method()
x = 0
while x < 2:
    checker.test_satchecker()
checker.teardown_method()
