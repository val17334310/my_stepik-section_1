import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    btn = browser.find_elements_by_css_selector(".btn-add-to-basket")
    assert btn, "button is missing"
    #Добавил time.sleep для проверки изменения языка
    time.sleep(10)