from time import sleep

import requests

"""
batch delete github repositories.

read this:
在 github 上 settings -> Developer settings -> Personal access tokens -> Generate new token
选择 delete_repo，记录该 token。
 
"""
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token !!!REPLACE THIS TOKEN HERE!!!",  # 此处的 xxx 代表前面申请的 token
    "X-OAuth-Scopes": "repo"
}

with open('repos.txt', 'r', encoding='utf-8') as f:  # 此处修改为 repos.txt 的地址
    repo_list = f.readlines()

url = "https://api.github.com/repos/{}/{}"
url_list = []
for repo in repo_list:
    name, repo = repo.strip().split("/")
    url_list.append(url.format(name, repo))

for url in url_list:
    requests.delete(url=url, headers=headers)
    sleep(2)
