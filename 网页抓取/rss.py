import feedparser
import re 

rss = 'http://rss.cnki.net/kns/rss.aspx?Journal=SHSW&Virtual=knavi'
feed = feedparser.parse(rss)
for key in feed["entries"]:
    print('*'*50+ "\n")
    print("标题：" + key["title"] + "\n")
    print("更新日期：" + key["updated"] + "\n")
    print("作者：" + key["author"] + "\n")
    regex = re.compile("作者：.*?<br/>摘要：")
    s = key["summary_detail"]['value']
    sub = ''
    result = re.sub(regex, sub, s, 0)
    print("摘要：" + result) 
    print('*'*50+ "\n")
