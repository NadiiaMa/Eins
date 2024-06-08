import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 58
    assert 'become-qa-auto' in r['items'][0]['name'] 


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0
    

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

@pytest.mark.api
def test_get_emojis(github_api):
    emojis = github_api.get_emojis()
    assert "smile" in emojis

@pytest.mark.api
def test_list_commits(github_api):
    commits = github_api.list_commits("octocat/Hello-World")
    assert len(commits) > 0
    assert "commit" in commits[0]

@pytest.mark.api
def test_list_commits_non_existing_repo(github_api):
    r = github_api.list_commits("octocat/non-existing-repo")
    assert 'message' in r
    assert r['message'] == 'Not Found'

@pytest.mark.api
def test_list_commits_specific_user_repo(github_api):
    commits = github_api.list_commits("torvalds/linux")
    assert len(commits) > 0
    assert "commit" in commits[0]

@pytest.mark.api
def test_emoji_monkey_exists(github_api):
    emojis = github_api.get_emojis()
    assert "monkey" in emojis

def test_emoji_total_count(github_api):
    emojis = github_api.get_emojis()
    assert len(emojis) > 1000
       