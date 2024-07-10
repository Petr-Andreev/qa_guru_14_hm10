from data import users
from pages.github_page import GitHubPage


def test_open():
    github_form = GitHubPage()
    admin = users.admin
    github_form.open()
    github_form.assert_name_issue(admin)
