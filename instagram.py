
from time import sleep

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)

class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')

    def go_to_login_page(self):
      #  self.browser.find_element_by_xpath("//a[text()='Entrar']").click()
        sleep(2)
        return LoginPage(self.browser)


import time 
import sys
import random
from selenium import webdriver


user = "USER"
password = "PASSWORD"
profile = "PROFILE_TO_FOLLOW_FOLLOWERS"
total = 150
shouldExit = False

browser = webdriver.Chrome()
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login(user, password)

browser.implicitly_wait(5)

browser.get("https://www.instagram.com/"+profile)

time.sleep(2)
followers = browser.find_element_by_xpath('//a[@href="/'+profile+'/followers/"]')
followers.click()

time.sleep(5)

fBody  = browser.find_element_by_xpath('//div[@role="dialog"]//ul')
overflow  = fBody.find_element_by_xpath('..')
scroll = 0

time.sleep(5)
counter = 0
while True:
    #browser.execute_script('arguments[0].scrollTop = 1000000;', overflow)
    buttons = fBody.find_elements_by_xpath("//*[contains(text(), 'Seguir')]")
    counterFor = 0

    if(len(buttons) > 5):
        time.sleep(random.randint(50, 100))
        
    for btn in buttons:
        browser.execute_script('arguments[0].scrollTop = arguments[1].scrollTop + arguments[1].offsetHeight;', overflow, btn)
        btn.click()
        time.sleep(2)
        # if(btn.text == "Seguir"):
        #     shouldExit = True
        #     break

        #name  = btn.find_element_by_xpath('../..').find_element_by_class_name('notranslate').text
        sys.stdout.write('\nFollowed ['+str(counter+1)+'/'+str(total)+']')
        sys.stdout.flush()

        time.sleep(random.randint(15, 40))
        counterFor += 1
        counter += 1
        if(counter >= total):
            break

    if(len(buttons) == counterFor):
        browser.execute_script('arguments[0].scrollTop = 10000000000;', overflow)
        sleep(3)


        
    
    if(counter >= total) or (shouldExit == True):
        break

browser.close()

