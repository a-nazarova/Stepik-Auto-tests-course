from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    #link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector("input:required.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("input:required.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("input:required.third")
    input3.send_keys("Smolensk@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
