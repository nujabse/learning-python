# -*- coding:utf-8 -*-
import urllib2
import re
import urllib


page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# 加上header 否则会出现请求错误
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    # 使用re 模块的compile 函数增加匹配模块的复用性
    pattern = re.compile('<div class="author clearfix">.*?href.*?<img src.*?title=.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?(.*?)</div>.*?<i class="number">(.*?)</i>',re.S)
    # 抓取 作者  内容 图片与否 点赞
    items = re.findall(pattern, content)
    # 去掉图片
    for item in items:
        haveImg = re.search("img", item[2])
        if not haveImg:
            print item[0], item[1], item[3]
   # print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
