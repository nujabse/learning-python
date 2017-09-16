import feedparser
import re
from string import Template
import smtplib
from email.mime.text import MIMEText
from datetime import date


# read from rss site
# rss = 'http://rss.cnki.net/kns/rss.aspx?Journal=SHSW&Virtual=knavi'
# feed = feedparser.parse(rss)
# d = dict()

# d['name'] = "李童庆"
# d['time'] = date.today().strftime("%d/%m/%y")
class RssToEmail():
    def __init__(self):
        self.feed = feedparser.parse('http://rss.cnki.net/kns/rss.aspx?Journal=SHSW&Virtual=knavi')
        self.text = ''
        self.limit = 10

    def read_template(self, filename):
        with open(filename, 'r') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)

    def send_message(self):
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login("h.p.zhumeng@outlook.com", "microsoft2015")
        s.sendmail("h.p.zhumeng@outlook.com", "962302959@qq.com", msg)

    def text_generator(self):
        for key in self.feed["entries"][:self.limit]:
            # print('*'*50+ "\n")
            # print("标题：" + key["title"] + "\n")
            self.text += "标题：" + key["title"] + "\n"
            # print("更新日期：" + key["updated"] + "\n")
            self.text += "更新日期：" + key["updated"] + "\n"
            # print("作者：" + key["author"] + "\n")
            self.text += "作者：" + key["author"] + "\n"
            regex = re.compile("作者：.*?<br/>摘要：")
            s = key["summary_detail"]['value']
            sub = ''
            result = re.sub(regex, sub, s, 0)
            self.text += "摘要：" + result + "\n"
        print(self.text)
        return self.text
        # print("摘要：" + result + "\n")
        # print('*'*50+ "\n")
        # text = text + read_template('message.txt').safe_substitute(d)


RssToEmail().text_generator()
# print(text)
