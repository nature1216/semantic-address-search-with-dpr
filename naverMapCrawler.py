from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

jeonju_restaurant_info = pd.DataFrame(columns=['상호명','도로명주소','지번주소','설명'])

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)

driver.get("https://map.naver.com/")

searchTextField = driver.find_element(By.CLASS_NAME, "input_search")
searchTextField.send_keys("전주 음식점" + Keys.ENTER)

time.sleep(2)

searchFrame = driver.find_element(By.CSS_SELECTOR, "iframe#searchIframe")
driver.switch_to.frame(searchFrame)

body = driver.find_element(By.CSS_SELECTOR, 'body')
body.click()
for i in range(50) :
    body.send_keys(Keys.PAGE_DOWN)

item_list = driver.find_elements(By.CSS_SELECTOR, 'span.place_bluelink.TYaxT')
print(len(item_list))

for i in item_list:
    time.sleep(1)
    i.click()
    title = i.text
    time.sleep(1)
    driver.switch_to.default_content()
    entryFrame = driver.find_element(By.CSS_SELECTOR, "iframe#entryIframe")
    driver.switch_to.frame(entryFrame)

    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[4]/div/div/div/div/a[1]").click()
    # driver.find_element(By.CSS_SELECTOR, "a.PkgBl").click()
    try:
        driver.find_element(By.CSS_SELECTOR, "a.PkgBl").click()
        juso = driver.find_elements(By.CSS_SELECTOR, 'div.nQ7Lh')
        print(juso[0].text)
        print(juso[1].text)
        doro_juso = juso[0].text
        jibeon_juso = juso[1].text
        driver.find_element(By.CSS_SELECTOR, "a.PkgBl").click()
    except:
        print("없음")
        doro_juso = None
        jibeon_juso = None

    try:
        driver.find_element(By.CSS_SELECTOR, "a.xHaT3").click()
    except:
        print("더보기없음")

    try:
        explain = driver.find_element(By.CSS_SELECTOR, "span.zPfVt").text
        print(explain)
    except:
        explain = None
        print("설명없음")
    driver.switch_to.default_content()
    driver.switch_to.frame(searchFrame)
    time.sleep(3)

    new_data = pd.DataFrame({'상호명': [title], '도로명주소': [doro_juso], '지번주소': [jibeon_juso], '설명': [explain]})
    jeonju_restaurant_info = pd.concat([jeonju_restaurant_info, new_data], ignore_index=True)

driver.quit()

print(jeonju_restaurant_info)