import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
PATH="C:\edgeDriver\msedgedriver.exe"
driver = webdriver.Edge(PATH)
driver.get('https://gogoanime.pe/login.html')
form=driver.find_element(By.CLASS_NAME,'form-login')
inp= driver.find_element(By.XPATH,"//input[@type='email']").send_keys('prayashthapa15@yahoo.com')
pas = driver.find_element(By.XPATH,"//input[@type='password']").send_keys('party@me')
but= driver.find_element(By.XPATH,"//button[@type='submit']").click()
#inp.send_keys('prayash')


driver.get('https://gogoanime.pe/toushinki-gs-frame-episode-3')
driver.implicitly_wait(5)
#download = driver.find_element(By.CLASS_NAME,'dowload')
#link= download.find_element(By.TAG_NAME,'a').click() 
#print("praysh dudue"+ inp[1].text)



