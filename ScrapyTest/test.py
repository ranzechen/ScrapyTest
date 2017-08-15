#!/bin/bash/python
from bs4 import BeautifulSoup
import urllib.request
def get_html(url):
    request = urllib.request.Request(url)
    request.add_header("User-Agent",
                       "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36")
    html = urllib.request.urlopen(request)
    return html.read()

def get_soup(url):
    soup = BeautifulSoup(get_html(url), "lxml")
    return soup
def img2port(img_url):
    """
    mimvp.com的端口号用图片来显示, 本函数将图片url转为端口, 目前的临时性方法并不准确
    """
    code = img_url.split("=")[-1]
    if code.find("AO0OO0O") > 0:
        return 80
    else:
        return None
if __name__ == '__main__':
    url = "http://www.httpdaili.com/mfdl/"
    soup = get_soup(url)
    table = soup.find("div", attrs={"kb-item-wrap11"}).table
    trs = table.find_all("tr")
    for i in range(1, len(trs)):
        tds = trs[i].find_all("td")
        if len(tds) != 0:
            ip = tds[0].text
            port = tds[1].text
            type = tds[2].text
            if type == u"匿名":
                print(ip, port)


