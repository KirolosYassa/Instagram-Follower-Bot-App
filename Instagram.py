import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
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

        
        
    def getSpeedReadings(self):
        self.start_internet_test()
        self.get_internet_test_speed_data()
        return self.readings_of_internet_test_speed
        
                
    def sign_in(self):
        time.sleep(3.2)
        log_in = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_Ma"]/div/div/div[1]/div/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[3]/div/div/div[2]/div[1]/a/button')
        log_in.click()
        time.sleep(2.1)
        
        fill_username = self.driver.find_element(By.NAME, "username")
        fill_username.send_keys(self.username)
        
        fill_password = self.driver.find_element(By.NAME, "password")
        fill_password.send_keys(self.password)

        time.sleep(5.2)

        not_now_skip_button = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_Pp"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        not_now_skip_button.click()
        time.sleep(5.2)
        
    
    def follow_the_followers_users(self):
        followers_users_button = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_9X"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers_users_button.click()
        
    