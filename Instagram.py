import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Instagram():
    def __init__(self, url="https://www.speedtest.net/"):
        load_dotenv()   
        self.url = url
        self.chrome_local_path = "C:\Development"
        self.driver = webdriver.Chrome(executable_path=self.chrome_local_path)
        self.driver.get(self.url)
        self.username = os.getenv("INSTAGRAM_USERNAME")
        self.password = os.getenv("PASSWORD")


    def sign_in(self):
        time.sleep(5.2)
        log_in = self.driver.find_elements(By.CLASS_NAME, '_aj1-')
        log_in[84].click()
        time.sleep(2.1)
        
        fill_username = self.driver.find_element(By.NAME, "username")
        fill_username.send_keys(self.username)
        
        fill_password = self.driver.find_element(By.NAME, "password")
        fill_password.send_keys(self.password)
        
        log_in_button = self.driver.find_elements(By.CLASS_NAME, "_acan")
        log_in_button[1].click()

        time.sleep(7.2)

        not_now_skip_button = self.driver.find_element(By.CLASS_NAME, '_ac8f')
        not_now_skip_button.click()
        time.sleep(5.2)
        
    
    def follow_the_followers_users(self):
        followers_users_button = self.driver.find_elements(By.CLASS_NAME, 'x2pgyrj')
        followers_users_button[1].click()
        time.sleep(4.2)
        # followers_div = self.driver.find_element(By.CSS_SELECTOR, "div > div._aano")
        popup_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(popup_window_handle)
        print(self.driver)

        # Scroll down the popup window by sending Page Down key multiple times
        for i in range(10):
            self.driver.find_element(By.CSS_SELECTOR, 'div._aano').send_keys(Keys.END)
            time.sleep(3.2)   # wait for 1 second for the page to load before scrolling again
            
            
            
    