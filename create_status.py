import os
import requests
from pprint import pprint
access_token = os.environ['GITHUB_ACCESS_TOKEN']


# TODO: needs tests
def create_status(access_token, repo_name, pull_request_sha, state):
    """
    Create a new status associated with a Github pull requests
    Full API documentation https://developer.github.com/v3/repos/statuses/
    """
    # TODO: validation for state in ('pending',  'success', 'failure')
    base_url = 'https://api.github.com'
    headers = {'Authorization': 'token {}'.format(access_token)}
    url = '{}/repos/{}/statuses/{}'.format(
        base_url, repo_name, pull_request_sha)
    # TODO: pass better info about what's happened
    return requests.post(url, headers=headers, json={'state': state})


response = create_status(
    access_token=access_token,
    repo_name='pxg/Spoon-Knife',
    pull_request_sha='6ce3b87cf95900f71a3cb7742a8de25719b5de10',
    state='success')
pprint(response.status_code)
pprint(response.json())
