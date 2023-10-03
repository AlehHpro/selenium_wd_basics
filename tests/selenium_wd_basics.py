import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSelenium(unittest.TestCase):
    __EMAIL = "valid.email@kaseya.com"
    __PASSWORD = "ValidPassword"

    def setUp(self) -> None:
        # setup
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_login(self):
        # test
        self.driver.get(url="https://dev.darkwebid.io/user/login?destination=resellers")
        self.driver.find_element(By.XPATH, "//*[@id='edit-name']").click()
        self.driver.find_element(By.ID, "edit-name").send_keys("sfsg")
        self.driver.find_element(By.ID, "edit-submit").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//a[@data-dismiss='alert']/.."))

        self.driver.find_element(By.XPATH, "//*[@id='edit-name']").clear()
        self.driver.find_element(By.XPATH, "//*[@id='edit-name']").click()
        self.driver.find_element(By.ID, "edit-name").send_keys(self.__EMAIL)
        self.driver.find_element(By.ID, "edit-submit").click()
        self.driver.find_element(By.ID, "edit-pass").send_keys("valid.email@kaseya.com")
        self.driver.find_element(By.ID, "edit-submit").click()
        self.assertTrue(self.driver.find_element(By.XPATH, "//a[@data-dismiss='alert']/.."))
        self.driver.find_element(By.ID, "edit-pass").clear()
        self.driver.find_element(By.ID, "edit-pass").send_keys(self.__PASSWORD)
        self.driver.find_element(By.ID, "edit-submit").click()

        self.assertTrue(self.driver.find_element(By.XPATH, "//div/h1[contains(text(),'Authentication')]"))

        self.driver.find_element(By.XPATH, "//*[@id='edit-actions']/a").click()

    def test_forgot_password(self):
        self.driver.get(url="https://dev.darkwebid.io/user/login?destination=resellers")
        self.driver.find_element(By.XPATH, "//*[@id='edit-name']").click()
        self.driver.find_element(By.ID, "edit-name").send_keys(self.__EMAIL)
        self.driver.find_element(By.ID, "edit-submit").click()
        self.driver.find_element(By.XPATH, "//*[@id='edit-forgot']/a").click()
        self.driver.find_element(By.ID, "edit-name").send_keys("asd@kaseya.com")
        self.driver.find_element(By.ID, "edit-submit").click()
        self.driver.find_element(By.XPATH, "//*[@id='block-system-main']/a").click()

    def test_kaseya_helpdesk_display(self):
        self.driver.get(url="https://dev.darkwebid.io/user/login?destination=resellers")
        self.driver.find_element(By.XPATH, "//a[text()='Learn More about KaseyaOne']").click()
        time.sleep(5)
        # Get current window handle (parent window)
        parent_window = self.driver.window_handles[0]

        # Switch to the new window/tab
        for window_handle in self.driver.window_handles:
            if window_handle != parent_window:
                self.driver.switch_to.window(window_handle)
                break  # Remove this line to switch to the last child window/tab(if you have only two)

        self.assertTrue(self.driver.title == "KaseyaOne")

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
