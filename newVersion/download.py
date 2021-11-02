import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
PATH="C:\edgeDriver\msedgedriver.exe"# Enter the path of the web driver
driver = webdriver.Edge(PATH)
driver.get('https://gogoanime.pe/login.html')
form=driver.find_element(By.CLASS_NAME,'form-login')
inp= driver.find_element(By.XPATH,"//input[@type='email']").send_keys('')# login credentials
pas = driver.find_element(By.XPATH,"//input[@type='password']").send_keys('')
but= driver.find_element(By.XPATH,"//button[@type='submit']").click()
#inp.2end_keys('prayash')
a=20 #first episode
b=27#last episode
b=b+1
counter=1
url='https://gogoanime.pe/k-on-2-episode-'
for i in range(a,b):
    x=str(i)
    driver.get(url+x)#Link of the anime
    time.sleep(5) 
    download_bar= driver.find_element(By.CLASS_NAME,'cf-download')
    download= download_bar.find_element(By.TAG_NAME,'a')
    download.click()
    time.sleep(5)
    
    if counter % 3 ==0 :
        time.sleep(300)
    counter += 1

#download = driver.find_element(By.CLASS_NAME,'dowload')
#link= download.find_element(By.TAG_NAME,'a').click() 
#print("praysh dudue"+ inp[1].text)



