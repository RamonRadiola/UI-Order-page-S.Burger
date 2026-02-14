from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = Constants.URL
        self.original_window = self.get_current_window_handle()

    @allure.step("базовый метод с переходом на главную старницу сайта")
    def go_to_site(self, driver):
        self.driver.get(self.url)
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.LOGO_WORD_SCOOTER))

    @allure.step("базовый метод определения кликабельности элемента")
    def find_element_for_click(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator), message=f'Not find element {locator}')

    @allure.step("базовый метод для определения появления элемента'")
    def find_element_for_visio(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not find element {locator}')

    @allure.step("Метод прокрутки страницы до нужного элемента")
    def scroll_to_element_base(self, locator):
        element = self.find_element_for_visio(locator)
        self.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("базовый метод для определения появления элемента'")
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step("Возвращает список handles всех открытых вкладок'")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключается на указанную вкладку'")
    def switch_to_window(self, window_handle):
         self.driver.switch_to.window(window_handle)

    @allure.step("Ожидает, пока количество открытых вкладок станет равным указанному'")
    def wait_for_number_of_windows_to_be(self, number, timeout=10):
         WebDriverWait(self.driver, timeout).until(EC.number_of_windows_to_be(number))

    @allure.step("Ожидает, пока URL страницы станет равным указанному")
    def wait_for_url_to_be(self, url, timeout=10):
         WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    @allure.step("Закрывает текущую вкладку")
    def close_current_window(self):
        self.driver.close()

    @allure.step("Выполняет JavaScript на странице")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Возвращает текущий url")
    def check_current_url(self):
        return self.driver.current_url

    @allure.step("Переключается на новую вкладку")
    def switch_new_window(self):
        windows = self.get_window_handles()
        for window in windows:
            if window != self.original_window:
                self.switch_to_window(window)
                break