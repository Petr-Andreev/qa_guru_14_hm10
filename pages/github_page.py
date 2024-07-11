from selene import browser, have
from data.data_name import Data


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

    def assert_name_issue(self, issue: Data):
        self.click_search()
        self.search_repo(issue.repo)
        self.search_text(issue.text_for_search)
        self.should_have_text(issue.text_for_should)
