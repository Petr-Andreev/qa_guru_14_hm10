from selene import browser, have
from data.users import User


class GitHubPage:

    def open(self):
        browser.open('/Petr-Andreev')

    def click_search(self):
        browser.element('[data-target="qbsearch-input.inputButtonText"]').click()

    def search_repo(self, name_repo):
        browser.element('#query-builder-test').send_keys(f'repo:{name_repo}').press_enter()

    def search_text(self, text):
        browser.all('[data-hovercard-type="issue"]').element_by(have.exact_text(text)).click()

    def should_have_text(self, text):
        browser.all('.markdown-title').first.should(have.text(text))

    def assert_name_issue(self, admin: User):
        self.click_search()
        self.search_repo(admin.repo)
        self.search_text(admin.text_for_search)
        self.should_have_text(admin.text_for_should)
