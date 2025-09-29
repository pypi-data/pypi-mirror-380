"""
unstar: Simple script to automate the removal of GitHub stars
"""

import sys
from time import sleep

from .exceptions import GitStarsException
from .stars import GitStars

__version__ = "0.1.0"

def main():
    """Main entry point for the CLI application."""
    if len(sys.argv) != 2:
        print("Usage: unstar <access_token>")
        print("Get your access token from: https://github.com/settings/tokens")
        sys.exit(1)

    access_token = sys.argv[1]
    my_stars = GitStars("https://api.github.com", access_token)

    try:
        reposes = my_stars.get_all_star_repos(2)

        for repo in reposes:
            if my_stars.delete_star(repo):
                print(f"{repo} is unstarred")
            else:
                print(f"{repo} not found")

            sleep(1)

    except GitStarsException as e:
        print('exception is - ' + e.__str__())
        sys.exit(1)


if __name__ == '__main__':
    main()
