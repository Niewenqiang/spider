from bs4 import BeautifulSoup
import requests


def findall_in_page(page, startpart, endpart):
    all_strings = []
    end = 0
    while page.find(startpart, end) != -1:
        start = page.find(startpart, end) + len(startpart)
        end = page.find(endpart, start)
        string = page[start:end]
        all_strings.append(string)
    return all_strings


def t_title(x, page):
    target = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
    target = target.format(x, page)
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html, "lxml")
    div = div_bf.find_all('a', class_='j_th_tit')
    div = str(div)
    ti = findall_in_page(div, 'title="', '"')
    minti = findall_in_page(div, 'href="', '"')
    return ti, minti


def t_content(y, subpage):
    target = 'https://tieba.baidu.com{}?pn={}'
    target = target.format(y, subpage)
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html, "lxml")
    div = div_bf.find_all('div', class_="d_post_content j_d_post_content ")
    div_bf = str(div)
    m = findall_in_page(div_bf, '   ', '<')
    c = []
    for x in m:
        x = x.lstrip()
        c.append(x)
    #print(c)
    return c


def get_page_num(ii):
    target = 'https://tieba.baidu.com{}'
    target = target.format(ii)
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html, "lxml")
    div = div_bf.find_all('li', class_="l_pager pager_theme_4 pb_list_pager")
    div_bf = str(div)
    if ii in div_bf:
        m = findall_in_page(div_bf, '下一页', '">尾页')
        m = str(m)
        m = findall_in_page(m, '?pn=', '">尾页')
        m = str(m)
        m = int(m[2:-3])
    else:
        m = 1
    return m


if __name__ == '__main__':
    for k in range(0, 500, 50):
        a, b = t_title('全民冠军足球', k)
        p = []
        for i in b:
            m = get_page_num(i)
            q = []
            for st in range(1, m+1, 1):
                z = t_content(i, st)
                q.append(z)
            p.append(q)
        for j in range(len(a)):
            print("标题：", a[j])
            print("内容：", p[j])

