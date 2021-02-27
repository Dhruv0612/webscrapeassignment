from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/login/index.php")

a = driver.find_element_by_id("username")

b = driver.find_element_by_id("password")

c = driver.find_element_by_id("valuepkg3")

d = driver.find_element_by_id("login")

e=d.text

l=e.split("\n")

captcha = l[3]

f=input("ENTER USERNAME")
g=input("ENTER PASSWORD")

a.send_keys(f)
b.send_keys(g)
h=""
useful=captcha.split()

if "first" in useful:
    i=useful.index(",")
    h+=useful[i-1]

elif "second" in useful:
    i=useful.index(",")
    h+=useful[i+1]

elif "add" in useful:
    i=useful.index("+")
    h+=str(int(useful[i+1])+int(useful[i-1]))

elif "subtract" in useful:
    i=useful.index("-")
    h+=str(int(useful[i-1])-int(useful[i+1]))

c.send_keys(h)

c.send_keys(Keys.RETURN)











