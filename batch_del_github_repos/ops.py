from time import sleep
import requests

"""
read this:
在 github 上 settings -> Developer settings -> Personal access tokens -> Generate new token
选择 delete_repo，记录该 token。
 
"""
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token !!!REPLACE THIS TOKEN HERE!!!", # 此处的 xxx 代表前面申请的 token
    "X-OAuth-Scopes": "repo"
}

with open('repos.txt', 'r', encoding='utf-8') as f: # 此处修改为 repos.txt 的地址
    data = f.readlines()

url = "https://api.github.com/repos/{}/{}"
urls = []
for line in data:
    name, repo = line.strip().split("/")
    urls.append(url.format(name, repo))

for l in urls:
    requests.delete(url=l, headers=headers)
    sleep(2)