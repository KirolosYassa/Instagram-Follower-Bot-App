import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import humanfriendly
import time
from parse_numbers import parse_number_with_k_suffix
from selenium.common.exceptions import NoSuchElementException

class Instagram():
    def __init__(self, profile_name="coding_dev_"):
        load_dotenv()   
        self.profile_name = profile_name
        print(profile_name)
        self.url = f"https://www.instagram.com/"
        self.chrome_local_path = "C:\Development"
        self.driver = webdriver.Chrome(executable_path=self.chrome_local_path)
        self.driver.get(self.url)
        self.username = os.getenv("INSTAGRAM_USERNAME")
        self.password = os.getenv("PASSWORD")
        print(self.username, self.password)


    def sign_in(self):
        time.sleep(5.2)
        # log_in = self.driver.find_elements(By.CLASS_NAME, '_aj1-')
        # log_in[84].click()
        # time.sleep(2.1)
        
        fill_username = self.driver.find_element(By.NAME, "username")
        fill_username.send_keys(self.username)
        
        fill_password = self.driver.find_element(By.NAME, "password")
        fill_password.send_keys(self.password)
        
        log_in_button = self.driver.find_elements(By.CLASS_NAME, "_acan")
        log_in_button[1].click()

        time.sleep(10.2)
        
    
    def find_followers(self):
        self.url = f"https://www.instagram.com/{self.profile_name}/followers"
        self.driver.get(self.url)
        time.sleep(5.2)
        
        pop_up_window = self.driver.find_element(By.CLASS_NAME, "_aano")
        
        # Scroll till Followers list is there
        followers_number = self.driver.find_elements(By.CSS_SELECTOR, "span._ac2a span")
        print(followers_number[1].text)
        followers_number = parse_number_with_k_suffix(followers_number[1].text)
                                                      
        # counter = 0
        # progress_bar = self.driver.find_element(By.CLASS_NAME, "x78zum5")
        while True:
            try:
                
                self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', 
                pop_up_window)
                loading_still = self.driver.find_element(By.CSS_SELECTOR, '.x78zum5.xl56j7k.xdt5ytf')
                print(loading_still)
                # time.sleep(0.5)
            except: 
                break

    def follow(self):
        users = self.driver.find_elements(By.CLASS_NAME, "_acan")
        for user in users:
            try:
                user.click()
            except:
                unfollow_button = self.driver.find_element(By.CLASS_NAME, "_a9-_")
                unfollow_button.click()
                
                # cancel_button = self.driver.find_element(By.CLASS_NAME, "_a9_1")
                # cancel_button.click()
            finally:
                time.sleep(0.5)
                continue
            

    # def unfollow(self):
    #     users = self.driver.find_elements(By.CLASS_NAME, "_acan")
    #     for user in users:
    #         try:
    #             user.click()
    #         except:
    #             unfollow_button = self.driver.find_element(By.CLASS_NAME, "_a9-_")
    #             unfollow_button.click()
                
    #             # cancel_button = self.driver.find_element(By.CLASS_NAME, "_a9_1")
    #             # cancel_button.click()
    #         finally:
    #             time.sleep(0.5)
    #             continue
            
    