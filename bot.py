from selenium import webdriver
from secrets import username, password
from time import sleep

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome("env/Scripts/chromedriver.exe")

    def login(self):
        # navigate to tinder.com
        self.driver.get("https://tinder.com/")
        sleep(5)

        # locate facebook login button
        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        # fb login phase
        base_window = self.driver.window_handles[0]
        fb_login = self.driver.window_handles[1]
        self.driver.switch_to_window(fb_login)

        # insert credentials
        fb_user = self.driver.find_element_by_xpath('//*[@id="email"]')
        fb_user.send_keys(username)

        fb_pass = self.driver.find_element_by_xpath('//*[@id="pass"]')  
        fb_pass.send_keys(password)

        fb_login_button = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        fb_login_button.click()  

        # going back to tinder
        self.switch_to_base()
        self.close_loc()
        self.close_notif()
        self.close_passport()


    def switch_to_base(self):
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(base_window)
        
    def like(self):
        like_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
        
        
        
    
    def dislike(self):
        dislike_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        dislike_button.click()
        
    def auto_swipe(self):
        self.switch_to_base()

        while True:
            sleep(0.5)
            try:
                self.like()
            except Exception:
                self.close_popup()

            
    def close_popup(self):
        close_popup_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        close_popup_button.click()

    def close_loc(self):
        allow_loc_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_loc_button.click()

    def close_notif(self):    
        enable_notification_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        enable_notification_button.click()

    def close_passport(self):
        passport_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        passport_button.click()


bot = TinderBot()
bot.login()
bot.auto_swipe()





