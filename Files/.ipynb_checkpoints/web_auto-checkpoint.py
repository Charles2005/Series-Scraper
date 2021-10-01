from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "../Selenium-Drivers/chromedriver.exe"


def entry(path=PATH):
    driver = webdriver.Chrome(path)
    driver.get("https://www.imdb.com/")
    driver.implicitly_wait(3)
    button = driver.find_element_by_class_name("ipc-icon--arrow-drop-down")
    button.click()
    advance_search = driver.find_element_by_link_text("Advanced Search")
    advance_search.click()
    while True:
        pass


# driver = webdriver.Chrome(PATH)
#
# driver.get("https://shopee.ph/")
# driver.implicitly_wait(3)
# pop_up_button = driver.find_element_by_class_name("shopee-popup__close-btn")
# pop_up_button.click()
#
# search_bar = driver.find_element_by_class_name("shopee-searchbar-input__input")
# search_bar.send_keys("GPU")
#
# submit_button = driver.find_element_by_class_name("btn-solid-primary")
# time.sleep(2)
# submit_button.click()



# WebDriverWait(driver, 30).until(
#     EC.text_to_be_present_in_element(
#         # Element Filtration
#         (By.CLASS_NAME, 'progress-label'),
#         # The expected text
#         'Complete!'
#     )
# )





