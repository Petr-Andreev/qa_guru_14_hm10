from data import data_name
from pages.github_page_with_decorated_steps import GitHubPage

github_form = GitHubPage()
issue = data_name.issue


def test_open():
    github_form.open_main_page()
    github_form.decorator_steps()
