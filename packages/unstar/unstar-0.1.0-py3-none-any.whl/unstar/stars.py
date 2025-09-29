from time import sleep

import requests

from .exceptions import GitStarsException


class GitStars:
    def __init__(self, instance, token):
        self.__instance = instance
        self.__token = token

    def get_all_star_repos(self, sleep_time):
        repos = []
        page = 1

        while True:
            request = requests.get(
                f"{self.__instance}/user/starred",
                params={'page': page, 'per_page': 100},
                headers={
                    'Authorization': f'token {self.__token}',
                    'X-GitHub-Api-Version': '2022-11-28'
                }
            )

            data = request.json()

            if request.status_code == 200:
                if len(data) == 0:
                    return repos
                else:
                    repos.extend(name['full_name'] for name in data)
            else:
                raise GitStarsException(request.status_code, data['message'])

            page = page + 1
            sleep(sleep_time)

    def delete_star(self, repo_name):
        request = requests.delete(
            f"{self.__instance}/user/starred/{repo_name}",
            headers={
                'Authorization': f'token {self.__token}',
                'X-GitHub-Api-Version': '2022-11-28'
            }
        )

        if request.status_code == 204:
            return True
        elif request.status_code == 404:
            return False
        else:
            raise GitStarsException(request.status_code, request.json()['message'])

    def set_star(self, repo_name):
        request = requests.put(
            f"{self.__instance}/user/starred/{repo_name}",
            headers={
                'Authorization': f'token {self.__token}',
                'X-GitHub-Api-Version': '2022-11-28'
            }
        )

        if request.status_code == 204:
            return True
        elif request.status_code == 404:
            return False
        else:
            raise GitStarsException(request.status_code, request.json()['message'])
