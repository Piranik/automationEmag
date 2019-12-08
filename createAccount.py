from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random


class AccountCreation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(height=1920, width=1080)
        self.driver.maximize_window()
        self.mail = 'testeautomate@mail.com'
        self.parola = 'Dan1231231'
        self.wait = WebDriverWait(self.driver, 10)
        self.url = ('https://www.emag.ro/homepage')
        abc = ["abcdefghijklmnopqrstuvwxyz1234567890"]
        for i in abc:
            self.mail = random.choice(i) + random.choice(i) + random.choice(i) + random.choice(i) + "@gmail.com"
        self.prenume = "Dany"
        self.nume = "Moceanu"
        self.parola = "D@31231"
        self.telefon = "+40721121456"
        self.action = ActionChains(self.driver)

    def testCreateAccount(self):
        self.driver.get(self.url)
        self.assertIn("eMAG.ro - Libertate în fiecare zi", self.driver.title, "Am ajuns pe homepage")

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/nav[1]/div/div/div[3]/div/div[2]/a/span"))).click()

        # Login / Create account page
        self.assertIn("https://www.emag.ro/user/login", self.driver.current_url, "Am ajuns pe pagina de login/create account")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='email']"))).send_keys(self.mail)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/form/div[4]/div/button"))).click()
        self.assertIn("https://www.emag.ro/user/register/", self.driver.current_url, "Register account")

        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='r_name']"))).send_keys(self.prenume + ' ' + self.nume)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="r_password"]'))).send_keys(self.parola)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="r_password_confirmation"]'))).send_keys(self.parola)
        # terms = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[5]/div/label')))
        # print(terms)
        time.sleep(1)
        term = self.driver.find_element_by_xpath('//*[@id="agree_terms"]')
        self.action.move_by_offset(xoffset=609, yoffset=545).click().perform()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[7]/div/button'))).click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    AccountCreation()