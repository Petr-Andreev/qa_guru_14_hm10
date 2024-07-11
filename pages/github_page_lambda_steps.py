import allure
from selene import browser, have
from data.data_name import Data


class GitHubPage:

    def open_repo(self):
        with allure.step(f"Открываем репозиторий Petr-Andreev"):
            browser.open('/Petr-Andreev')

    def click_search(self):
        with allure.step("Кликаем на поисковую строку"):
            browser.element('[data-target="qbsearch-input.inputButtonText"]').click()

    def search_repo(self, name_repo):
        with allure.step(f"Вводим в поисковую строку {name_repo} и нажимаем press_enter"):
            browser.element('#query-builder-test').send_keys(f'repo:{name_repo}').press_enter()

    def search_text(self, text):
        with allure.step(f"Находим значение: {text} и кликаем по нему"):
            browser.all('[data-hovercard-type="issue"]').element_by(have.exact_text(text)).click()

    def should_have_text(self, text):
        with allure.step(f"Убеждаемся, что значение: {text} найдено"):
            browser.all('.markdown-title').first.should(have.text(text))

    def assert_name_issue(self, issue: Data):
        self.click_search()
        self.search_repo(issue.repo)
        self.search_text(issue.text_for_search)
        self.should_have_text(issue.text_for_should)
