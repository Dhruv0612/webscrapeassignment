from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import shutil

options = Options()
options.add_argument("--headless")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH,chrome_options=options)

t=input("enter number")
truth = True

try:

    os.mkdir(t)

except OSError:

    shutil.rmtree(t)
    os.mkdir(t)

z = 65

while truth:
    j=chr(z)
    driver.get("https://codeforces.com/problemset/problem/" + t + "/" + j)
    b = driver.current_url
        
    if b[-1] == j:

        os.mkdir(t + "/" + j)

        s= lambda X: driver.execute_script("return document.body.parentNode.scroll" + X)
        driver.set_window_size(s("Width"),s("Height"))

        a = driver.find_elements_by_tag_name("pre")
        number_of_inputs = len(a)/2

        driver.find_element_by_tag_name("body").screenshot(t + "/" + j + "/problem.png")

        for i in range(0,len(a),2):
            file = open(t+ "/" + j + "/input" + str((i/2)+1) + ".txt","w")
            file.write(a[i].text)

        for i in range(1,len(a),2):
            file = open(t + "/" + j + "/output" + str((i/2)+ 0.5) + ".txt","w")
            file.write(a[i].text)

        z+=1

    else:
        truth = False

    






