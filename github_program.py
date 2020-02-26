import requests
import json
from operator import itemgetter

def get_user(username, debug=False):

    response = requests.get(f"https://api.github.com/users/{username}/repos")
    
    # if response.status_code != 200:
    #     raise TimeoutError

    summary = []
    repos = response.json()
    print(repos)

    for rep in repos:
        commits = requests.get(f"https://api.github.com/repos/{username}/{rep['name']}/commits").json()
        summary.append([rep['name'], len(commits)])

    if debug:
        # return [repo[0] for repo in summary]
        return response, repos

    return sorted(summary, key=itemgetter(1))

def get_input(prompt):
    username = input(prompt)
    return username

def main():
    username = get_input("Enter your username: \n")
    try:
        result = get_user(username)
        return username, result

    except TimeoutError as t:
        return "Request Timed Out", t

    except Exception as e:
        return "Invalid Input", e

if __name__ == "__main__":
    x, y = main()
    print(x, y)