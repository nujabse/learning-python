import feedparser
import re 
from string import Template
import smtplib
import time

# read from rss site
rss = 'http://rss.cnki.net/kns/rss.aspx?Journal=SHSW&Virtual=knavi'
feed = feedparser.parse(rss)

def read_template(filename):
    with open(filename, 'r') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def sendMessage():
"""
Send messages using SMTP server
"""
    s =smtplib.SMTP(host = 'smtp-mail.outlook.com', port = 587)
    s.starttls()
    s.login("h.p.zhumeng@outlook.com", "microsoft2015")
    s.sendmail("h.p.zhumeng@outlook.com", "962302959@qq.com", msg)


for key in feed["entries"]:
    print('*'*50+ "\n")
    print("标题：" + key["title"] + "\n")
    print("更新日期：" + key["updated"] + "\n")
    print("作者：" + key["author"] + "\n")
    regex = re.compile("作者：.*?<br/>摘要：")
    s = key["summary_detail"]['value']
    sub = ''
    result = re.sub(regex, sub, s, 0)
    print("摘要：" + result + "\n") 
    print('*'*50+ "\n")
