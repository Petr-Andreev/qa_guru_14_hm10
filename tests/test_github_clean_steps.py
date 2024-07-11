from data import data_name
from pages.github_page import GitHubPage

github_form = GitHubPage()

def test_open():
    issue = data_name.issue
    github_form.open()
    github_form.assert_name_issue(issue)
