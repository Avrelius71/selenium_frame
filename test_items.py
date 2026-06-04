from selenium.webdriver.common.by import By


class TestProductPage:
    def test_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

        assert button.is_displayed(), "Кнопки нет"