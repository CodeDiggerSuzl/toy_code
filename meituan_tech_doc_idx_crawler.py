import requests
from bs4 import BeautifulSoup

"""
第一版 后续改进
"""
url = "https://tech.meituan.com//page/2.html"
start_url = "https://tech.meituan.com/"
resp = requests.get(start_url)

html_raw_doc = resp.content.decode('utf-8')

soup = BeautifulSoup(html_raw_doc, 'html.parser')


class Info(object):
    def __init__(self, name, date, tags, url_link, short_desc):
        self.name = name
        self.date = date
        self.tags = tags
        self.link = url_link
        self.short_desc = short_desc

    def __str__(self):
        return self.name + self.date + self.link + self.short_desc


class Tag(object):
    def __init__(self, name, link):
        self.name = name
        self.link = link


if __name__ == '__main__':
    total_list = []
    result = soup.findAll("div", {"class": "post-container"})
    for child in result:
        print(child.text)
        if child.text == "浏览更多文章":
            continue
        zero = child.contents[0]
        name = zero.text
        # print(name)
        link = zero.contents[0].attrs['href']
        # print(link)
        date = child.contents[1].next.contents[1]
        # print(date)
        desc = child.contents[2].text
        # print(desc)
        tag_list = []
        for c in child.contents[3].contents[0].contents:
            if len(c.text) > 2:
                t = Tag(c.text, c.attrs['href'])
                tag_list.append(t)
        print(tag_list)
        total_list.append(Info(name, date, tag_list, link, desc))

    for i in range(len(total_list)):
        print(total_list[i].link)
        # print("序号：%s   值：%s" % (i + 1, total_list[i]))
