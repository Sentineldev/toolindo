from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def getScreenShot(url):


    service = Service(executable_path="./chromedriver")
    options = Options()
    options.add_argument('--start-maximized')
    with webdriver.Chrome(service=service,options=options) as driver:
        driver.get(url)

        element_1 = driver.find_element(By.ID,"cboxOverlay")   
        element_2 = driver.find_element(By.ID,"colorbox")
        driver.execute_script(
            """
            const element_1 = document.querySelector("#cboxOverlay")
            const element_2 = document.querySelector("#colorbox")
            element_1.parentNode.removeChild(element_1)
            element_2.parentNode.removeChild(element_2)
            document.body.style.zoom = "70%";

            window.scroll({
                top: 600,
                left: 100,
                behavior: "smooth",
            });

            """)       

        time.sleep(5)


        driver.save_screenshot("web.png")
getScreenShot("http://10.80.22.172:8085/producto/jueves-santo/")