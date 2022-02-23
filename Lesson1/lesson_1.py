import requests
import json


class GitRepos:
    def __init__(self, name):
        self.name = name
        self.url = f'https://api.github.com/users/{self.name}/repos'

    def repo_list_to_json(self, f_name):
        resp = requests.get(self.url)
        data = resp.json()
        repo_list = [repos.get('name') for repos in data]
        with open(f'{f_name}.json', 'w') as file:
            json.dump(repo_list, file)
        print('Done...')


def main():
    user = 'octocat'
    repos = GitRepos(user)
    repos.repo_list_to_json('repositories')


if __name__ == '__main__':
    main()
