from time import sleep
from selenium import webdriver
import random

#You need Chrome browser and chromedriver
browser = webdriver.Chrome()

#redirect to URL
browser.get('https://www.instagram.com')
browser.implicitly_wait(5)

#wait for 2 seconds
sleep(2)

#find username and password textfields
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

#write your username and password to the textfields
username_input.send_keys("<insert username here>")
password_input.send_keys("<insert password here>")

#find and click login button
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

#wait for 2 seconds
sleep(2)

browser.get('<insert instagram post URL here>')

commentArray = ["Nice!", "Wow!", "Perfect!", "Gorgeous!"]

#Number of iterations (how many comments to post)
N = 1000

for i in range(0, N):
    #find comment textfield and click it
    commentArea = browser.find_element_by_class_name('Ypffh')
    commentArea.click()
    commentArea = browser.find_element_by_class_name('Ypffh')

    #pick one random comment of the commentArea
    randomNum = random.randint(0, len(commentArray) - 1)
    
    #write the comment
    commentArea.send_keys(commentArray[randomNum])
    
    #find the post button and click it
    postButton = browser.find_element_by_xpath("//button[@type='submit']")
    postButton.click()
    
    #wait for 20 seconds. NOTE: change this to a big number so that instagram doesn't block your comments.
    sleep(20)


#exit Browser and end process
browser.quit()
browser.close()
