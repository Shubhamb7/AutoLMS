import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
url_list = []
subj_url_list = []
subj_ids = []

username = input('\n\nenter username : ')
passwd = input('enter password : ')

driver = webdriver.Chrome(options = options, executable_path=r"chromedriver.exe")
og_win = driver.window_handles[0]
driver.get("http://mydy.dypatil.edu/") 

user = driver.find_element_by_xpath('//*[@id="username"]')
user.click()
user.send_keys(username)
loginbtn = driver.find_element_by_xpath('//*[@id="loginbtn"]')
loginbtn.click()
passwdfld = driver.find_element_by_xpath('//*[@id="password"]')
passwdfld.click()
passwdfld.send_keys(passwd)
loginbtn2 = driver.find_element_by_xpath('//*[@id="loginbtn"]')
loginbtn2.click()

time.sleep(3)
links = driver.find_elements_by_tag_name('a')

for link in links:
    url = link.get_attribute('href')
    url_list.append(url)

num=33

for i in range(0,6):
    temp = url_list[num]
    templist = list(temp)
    finallist = templist[48:]
    subid = ''.join(finallist) 
    subj_ids.append(subid)
    num+=1

print('\n',subj_ids)
print('\n\nin progess...\n')

for i in range(0,6):
    driver.get("http://mydy.dypatil.edu/rait/course/customview.php?id="+subj_ids[i])
    time.sleep(2)
    subj_links = driver.find_elements_by_class_name('pending')
    
    for subj_link in subj_links:
        subj_url = subj_link.get_attribute('href')
        subj_url_list.append(subj_url)

    for i in subj_url_list:
        driver.execute_script('window.open("'+i+'","_blank")')
        time.sleep(1)

    for i in subj_url_list:
        new_win = driver.window_handles[1]
        driver.switch_to.window(new_win)
        driver.close()

    driver.switch_to.window(og_win)
    subj_url_list = []

setting = driver.find_element_by_class_name('usermenu')
setting.click()

links = driver.find_elements_by_tag_name('a')

for link in links:
    url = link.get_attribute('href')
    url_list.append(url)

driver.get(url_list[15])
driver.close()

print('Done!! Thankyou for waiting :)')
