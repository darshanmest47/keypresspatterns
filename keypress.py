
import pyautogui as P
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.facebook.com')

wt = WebDriverWait(driver,10)
wt.until(expected_conditions.title_contains('Facebook'))

name = driver.find_element(By.XPATH,"//input[@name='email']")
pwd = driver.find_element(By.XPATH,"//input[@type='password']")
btn = driver.find_element(By.NAME,"login")
name.click()
P.write("darshanmesta33@gmail.com")
P.sleep(5)
for i in range(25):
    P.press("backspace")
    P.sleep(1)


P.sleep(5)
P.write("darshanmesta33@gmail.com")
P.sleep(5)
P.hotkey("ctrl","a")
P.sleep(5)
P.hotkey("ctrl","c")
pwd.click()
P.hotkey("ctrl","v")
P.sleep(5)
for i in range(25):
    P.press("backspace")
    P.sleep(1)
P.write("DarshanKA47@")
P.sleep(2)
P.press("enter")
P.sleep(3)
driver.close()


