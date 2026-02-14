from pages.base_page import BasePage
from locators import Locators
import allure



class HomePage(BasePage):
    @allure.step("Клик по вопросу")
    def click_question(self, question_locator):
        self.find_element_for_click(locator=question_locator).click()

    @allure.step("Получение текста ответа")
    def get_answer_text(self, answer_locator):
        return self.find_element_for_visio(locator=answer_locator).text

    @allure.step("Метод прокрутки страницы до нужного элемента на странице")
    def scroll_to_element(self, locator):
        return self.scroll_to_element_base(locator)

    @allure.step("Клик по кнопке заказа сверху")
    def click_button_order_up(self):
        self.find_element_for_click(locator=Locators.BUTTON_ORDER_UP).click()

    @allure.step("Клик по кнопке заказа снизу")
    def click_button_order_down(self):
        self.find_element_for_click(locator=Locators.BUTTON_ORDER_DOWN).click()

    @allure.step("Клик по кнопке согласия на сбор куки")
    def click_button_cookie(self):
        self.find_element_for_click(locator=Locators.BUTTON_COOKIE).click()

    @allure.step("Клик по голотип-слову'cамокат'")
    def click_logo_scooter(self):
        self.find_element_for_click(locator=Locators.LOGO_WORD_SCOOTER).click()

    @allure.step("Клик по голотип-слову'яндекс'")
    def click_logo_ya(self):
        self.find_element_for_click(locator=Locators.LOGO_WORD_YANDEX).click()

    @allure.step("Проверка успешного оформления заказа")
    def is_order_successful(self):
        return 'Заказ оформлен' in self.find_element_for_visio(Locators.SIGNAL_ORDER_IS_READY).text