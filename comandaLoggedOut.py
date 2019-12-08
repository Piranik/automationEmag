from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random


class FlowComandaLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(height=1920, width=1080)
        self.driver.maximize_window()
        self.mail = "dantest@gmail.com"
        self.parola = 'Dan1231231'
        self.wait = WebDriverWait(self.driver, 10)
        self.url = ('https://www.emag.ro/homepage')
        self.action = ActionChains(self.driver)

    def testFlow(self):
        self.driver.get(self.url)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/ul/li[3]/a'))).click()
        time.sleep(2)
        # self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/div[3]/div[2]/ul/li[1]/div[1]/a[1]').click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div[3]/div[2]/ul/li[1]/div[1]/a[1]'))).click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/section[1]/div/div[2]/div/div[3]/div[2]/div[5]/div[1]/div[2]/div/div[1]/div[1]/a/div/img'))).click()
        self.driver.execute_script("scroll(0, 550);")

        #Cumpara in rate
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="trigger-ecredit-modal"]'))).click()
        self.assertIn('Cumpara in Rate', self.driver.page_source)
        time.sleep(1)
        self.action.move_by_offset(xoffset=1099, yoffset=369).click().perform()
        time.sleep(2)
        self.assertIn('Produsul a fost adaugat in cos', self.driver.page_source)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[19]/div/div/div[2]/div/div[3]/a'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[3]/a'))).click()
        time.sleep(1)

        #Login
        self.assertIn("https://www.emag.ro/user/login", self.driver.current_url)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="email"]'))).send_keys(self.mail)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[4]/div/button'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(self.parola)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[4]/div/button'))).click()
        time.sleep(2)

        #Checkout
        self.assertIn('https://www.emag.ro/cart/checkout', self.driver.current_url)
        time.sleep(1)
        self.driver.execute_script("scroll(0, 1000);")
        self.driver.execute_script("scroll(0, 1000);")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/form/div/div[1]/div[7]/div/div[3]/button'))).click()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/form/div/div[1]/div[3]/div/div/div[4]/div/ul/li[1]/div[2]/div[4]/div[2]/div[2]/div[2]/div[2]/label'))).click()
        time.sleep(2)
        self.driver.execute_script("scroll(0, 2000);")
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/form/div/div[1]/div[7]/div/div[3]/button'))).click()
        time.sleep(2)
        self.assertIn('https://www.emag.ro/cart/summary', self.driver.current_url)

        # TRimite comanda
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div[3]/button').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    FlowComandaLogout()