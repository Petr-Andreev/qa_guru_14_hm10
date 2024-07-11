import allure
from selene import browser, have
from data.data_name import issue


class GitHubPage:

    def decorator_steps(self):
        self.click_search()
        self.search_repo(issue.repo)
        self.search_text(issue.text_for_search)
        self.should_have_text(issue.text_for_should)

    @allure.step(f"Открываем репозиторий Petr-Andreev")
    def open_main_page(self):
        browser.open('/Petr-Andreev')

    @allure.step('Кликаем на поисковую строку')
    def click_search(self):
        browser.element('[data-target="qbsearch-input.inputButtonText"]').click()

    @allure.step("Вводим в поисковую строку {name_repo} и нажимаем press_enter")
    def search_repo(self, name_repo):
        browser.element('#query-builder-test').send_keys(f'repo:{name_repo}').press_enter()

    @allure.step('Находим значение: {text} и кликаем по нему')
    def search_text(self, text):
        browser.all('[data-hovercard-type="issue"]').element_by(have.exact_text(text)).click()

    @allure.step('Убеждаемся, что значение: {text} найдено')
    def should_have_text(self, text):
        browser.all('.markdown-title').first.should(have.text(text))
