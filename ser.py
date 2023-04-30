import constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Ser(webdriver.Chrome):
    def __init__(self, driver_path= "E:\Chrome driver" , teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Ser, self).__init__()

    def land_first_page(self):
        self.get(const.Base_URL)

    def login(self, email="hamza1996780@gmail.com", passw="Hamza123"):
        emai = self.find_element(by=By.ID, value="username")
        emai.clear()
        ps = self.find_element(by=By.ID, value="password")
        ps.clear()
        sub = self.find_element(by=By.CLASS_NAME, value="sbutton")
        time.sleep(3)
        emai.send_keys(email)
        ps.send_keys(passw)
        sub.click()

        self.implicitly_wait(5)
        time.sleep(3)
        sur = self.find_element(by=By.CLASS_NAME, value="fa.fahack.fahack_surveys")
        sur.click()

        cl = self.find_element(by=By.ID, value="addAddressFormClose1Cta")
        cl.click()

    def dailyserve(self):
        while(True):
            for x in range(10):
                chooseyouranswer = self.find_element(by=By.ID, value="profileAnswerDisplay")
                chooseyouranswer.click()
                time.sleep(2)
                profession = self.find_element(by=By.CLASS_NAME, value="surveyProfile-post__optionsItem--qa6Fz")
                profession.click()
                sub=self.find_element(by=By.ID, value="profileSubmitCta")
                sub.click()
                time.sleep(5)
            cont = self.find_element(by=By.ID, value="continueProfileCta")
            cont.click()
