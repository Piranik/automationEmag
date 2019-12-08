from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random


class FlowComandaLogin(unittest.TestCase):
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
        self.assertIn("eMAG.ro - Libertate în fiecare zi", self.driver.title, "Am ajuns pe homepage")
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "/html/body/div[3]/nav[1]/div/div/div[3]/div/div[2]/a/span"))).click()

        # Login / Create account page
        self.assertIn("https://www.emag.ro/user/login", self.driver.current_url,
                      "Am ajuns pe pagina de login/create account")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='email']"))).send_keys(self.mail)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/form/div[4]/div/button"))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(self.parola)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/form/div[4]/div/button'))).click()


        #Homepage
        time.sleep(2)
        self.assertIn('https://www.emag.ro/homepage', self.driver.current_url)

        #Navigate through cateogories
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/ul/li[1]/a/span'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/aside/ul/li[1]/a'))).click()
        self.driver.execute_script("scroll(0, 250);")
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/div/div[3]/div/section[1]/div/figure[1]/a'))).click()
        self.driver.execute_script("scroll(0, 550);")

        #Adauga in cos
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div/section[1]/div/div[2]/div/div[3]/div[2]/div[5]/div[1]/div[2]/div/div[3]/div[3]/form/button'))).click()
        time.sleep(2)
        self.assertIn('Produsul a fost adaugat in cos', self.driver.page_source)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[14]/div/div/div[5]/div/div/div/div[1]/div[3]/div[2]/a'))).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/section[1]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/form/div[3]/button[1]'))).click()
        time.sleep(2)
        self.assertIn("Produsul a fost adaugat in cos", self.driver.page_source)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[12]/div/div/div[1]/button'))).click()
        time.sleep(2)
        #Adauga la favorite
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/section[1]/div/div[2]/div/div[2]/div[2]/div/div/div[2]/form/div[3]/button[2]'))).click()

        #mergi in cos
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="my_cart"]'))).click()

        #sterge item
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/form/div/div[3]/div[1]/div[1]/div/div[2]/div[1]/div[3]/a[1]'))).click()
        time.sleep(2)

        #Update quantity
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/form/div/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div/span[1]/span[1]/span'))).click()
        time.sleep(1)
        self.action.move_by_offset(xoffset=756, yoffset=395).click().perform()

        #Continua la urmatorul pas de checkout
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[1]/div/div[3]/a'))).click()
        time.sleep(2)

        #Selecteaza livrare prin curier
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="courierTab"]'))).click()
        self.driver.execute_script("scroll(0, 1000);")
        time.sleep(1)

        #Metode de plata
        lista_metode = {"Card Online": '/html/body/div[1]/div/form/div/div[1]/div[5]/div[4]/ul/li[1]/div[1]',
                        "Ramburs": '/html/body/div[1]/div/form/div/div[1]/div[5]/div[4]/ul/li[2]/div[1]',
                        "Ordin de plata": '/html/body/div[1]/div/form/div/div[1]/div[5]/div[4]/ul/li[3]/div[1]',
                        "Mastercard": '/html/body/div[1]/div/form/div/div[1]/div[5]/div[4]/ul/li[4]/div[1]'}
        key_plata = random.choice(list(lista_metode.keys()))
        value_plata = lista_metode[key_plata]
        self.wait.until(EC.visibility_of_element_located((By.XPATH, value_plata))).click()
        time.sleep(1)
        self.driver.execute_script("scroll(0,650);")
        time.sleep(1)



        #Pasul urmator
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/form/div/div[1]/div[7]/div/div[3]/button'))).click()

        #TRimite comanda
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div[3]/button').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    FlowComandaLogin()