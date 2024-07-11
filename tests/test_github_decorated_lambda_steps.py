
from data import data_name
from pages.github_page_lambda_steps import GitHubPage

github_form = GitHubPage()
issue = data_name.issue
def test_open():
    github_form.open_repo()
    github_form.assert_name_issue(issue)