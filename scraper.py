import sys,time,credentials
sys.stdout.reconfigure(encoding='utf-8')
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.facebook.com/')

email = driver.find_element(By.ID,"email")
password = driver.find_element(By.ID,"pass")

email.send_keys(credentials.email)
password.send_keys(credentials.password)
password.submit()

time.sleep(10)

