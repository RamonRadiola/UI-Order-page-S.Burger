import allure
import pytest
from pages.home_page import HomePage
from data import Data

@allure.story("Кликает на плашку вопроса, проверяет текст выпадающего ответа")
class TestHomePage:
    @allure.title("Кликает на плашку вопроса, проверяет текст выпадающего ответа")
    @pytest.mark.parametrize("question_data", Data.QUESTION_DATA)
    def test_question_and_answer(self, home_page_start, question_data):
        home_page = HomePage(home_page_start.driver)
        home_page.click_question(question_data["question_locator"])
        answer_text = home_page.get_answer_text(question_data["answer_locator"])
        assert question_data["expected_text"] in answer_text