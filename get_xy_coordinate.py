__author__ = 'wyb'
# coding:utf-8
#
import xlrd
import xlwt
import requests
import urllib
import math
import re

pattern_x = re.compile(r'"x":(".+?")')
pattern_y = re.compile(r'"y":(".+?")')


def mercator2wgs84(mercator):
    point_x = mercator[0]
    point_y = mercator[1]
    x = point_x/20037508.3427892*180
    y = point_y/20037508.3427892*180
    y = 180/math.pi*(2*math.atan(math.exp(y*math.pi/180))-math.pi/2)
    return x, y


def get_mercator(addr):
    quote_addre = urllib.quote(addr.encode('utf-8'))
    city = urllib.quote(u'齐齐哈尔市'.encode('utf-8'))
    province = urllib.quote(u'黑龙江省'.encode('utf-8'))
    if quote_addre.startswith(city) or quote_addre.startswith(province):
        pass
    else:
        quote_addre = city+quote_addre
    s = urllib.quote(u'北京市'.encode('utf-8'))
    api_addre = "http://api.map.baidu.com/?qt=gc&wd=%s&cn=%s&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._ \
               cbk62300" % (quote_addre, s)
    req = requests.get(api_addre)
    content = req.content
    x = re.findall(pattern_x, content)
    y = re.findall(pattern_y, content)
    if x:
        x = x[0]
        y = y[0]
        x = x[1:-1]
        y = y[1:-1]
        x = float(x)
        y = float(y)
        location = (x, y)
    else:
        location = ()
    return location


def run():
    data = xlrd.open_workbook(r'H:\PyCharm\data\Book2.xls')
    rtable = data.sheets()[0]
    nrows = rtable.nrows
    values = rtable.col_values(0)

    workbook = xlwt.Workbook()
    wtable = workbook.add_sheet('data', cell_overwrite_ok=True)
    row = 0
    for value in values:
        mercator = get_mercator(value)
        if mercator:
           wgs = mercator2wgs84(mercator)
        else:
            wgs = ('NotFound', 'NotFound')
        print "%s,%s,%s" % (value, wgs[0], wgs[1])
        wtable.write(row, 0, value)
        wtable.write(row, 1, wgs[0])
        wtable.write(row, 2, wgs[1])
        row += 1

    workbook.save(r'H:\PyCharm\data\data.xls')

if __name__ == '__main__':
    run()
