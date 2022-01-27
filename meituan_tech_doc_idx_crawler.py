from time import sleep

import requests
from bs4 import BeautifulSoup

"""
第一版 后续改进
"""
url_template = "https://tech.meituan.com//page/{}.html"
base_url = "https://tech.meituan.com/"

start_page_num = 1
end_page_num = 26


class Info(object):
    def __init__(self, info_name, info_date, tags, url_link, short_desc):
        self.name = info_name
        self.date = info_date
        self.tags = tags
        self.link = url_link
        self.short_desc = short_desc

    def __str__(self):
        return self.name + self.date + self.link + self.short_desc


class Tag(object):
    def __init__(self, tag_name, tag_link):
        self.name = tag_name
        self.link = tag_link


def parse_one_page(page_num):
    sleep(1)
    url = url_template.format(page_num)
    if page_num == 1:
        url = base_url
    resp_text = requests.get(url).content.decode('utf-8')
    parse_result = BeautifulSoup(resp_text, 'html.parser')
    html_obj = parse_result.findAll("div", {"class": "post-container"})
    return html_obj


if __name__ == '__main__':
    total_list = []
    for i in range(start_page_num, end_page_num):
        result = parse_one_page(i)
        for child in result:
            if start_page_num == i and child.text == "浏览更多文章":
                continue
            zero = child.contents[0]
            name = zero.text
            link = zero.contents[0].attrs['href']
            date = child.contents[1].next.contents[1]
            desc = child.contents[2].text
            tag_list = []
            for c in child.contents[3].contents[0].contents:
                if len(c.text) > 2:
                    t = Tag(c.text, c.attrs['href'])
                    tag_list.append(t)
            total_list.append(Info(name, date, tag_list, link, desc))

    # for i in range(len(total_list)):
    #     print(len(total_list))
