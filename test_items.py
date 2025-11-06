from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_guest_should_see_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Проверяем наличие кнопки добавления в корзину
    try:
        add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        assert add_to_basket_button is not None, "Add to basket button not found"
    except NoSuchElementException:
        assert False, "Add to basket button not found"
