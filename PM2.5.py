# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
    target = 'http://www.pm25.com/shanghai.html'
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('div', class_='bi_location_content_active hide')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    for each in a:
        g = each.get('mon')
        g = g.replace('选择监测点', '上海')
        g = g.replace('十五厂', '闵行')
        g = g.replace('徐汇上师大', '徐汇')
        g = g.replace('杨浦四漂', '杨浦')
        g = g.replace('青浦淀山湖', '青浦')
        g = g.replace('静安监测站', '静安')
        g = g.replace('浦东川沙', '川沙')
        g = g.replace('浦东新区监测站', '浦东')
        g = g.replace('浦东张江', '张江')
        print(g, 'aqi==', each.get('aqi'), 'pm25==', each.get('pm25'), 'qua==', each.get('qua'))
    div1 = div_bf.find_all('div', class_='bi_aqiarea_bottom')
    print(div1[0])
