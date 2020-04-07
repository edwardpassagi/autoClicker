from selenium import webdriver
from secrets import username, password
from time import sleep

class ClickerBot():
    def __init__(self):
        self.driver = webdriver.Chrome("env/Scripts/chromedriver.exe")

    def login(self):
        # navigate to clickclick.com
        self.driver.get("https://clickclickclick.click/")
        sleep(3)

        # locate and spam button
        while True:
            sleep(0.5)
            click_btn = self.driver.find_element_by_xpath('/html/body/main/div/div[1]/a')
            click_btn.click()

bot = ClickerBot()
bot.login()





