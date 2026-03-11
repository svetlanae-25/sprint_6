#Проверка раздела «Вопросы о важном» (выпадающий список)
import allure
import pytest

import data
from pages.main_page import MainPage

class TestFAQAnswers:
    @allure.title("Тест ответов на вопросы")
    @pytest.mark.parametrize('question_id, expected_answer', data.FAQData.faq_answers)
    def test_faq_answers(self, driver, question_id, expected_answer):
        # Arrange
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_faq_question(question_id)
        # Act
        actual_answer = main_page.get_faq_answer_text(question_id)
        # Assert
        assert actual_answer == expected_answer