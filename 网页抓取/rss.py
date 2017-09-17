import feedparser
import re
from string import Template
import smtplib
from email.mime.text import MIMEText
from email.header import Header 
from email.utils import parseaddr, formataddr
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
        self.text = '<html><body><h1 style="font-size:24px; color:#202121">生物物理学周报</h1>'
        self.limit = 10
        self.from_addr = "h.p.zhumeng@outlook.com"
        self.to_addr = "962302959@qq.com"

    def read_template(self, filename):
        with open(filename, 'r') as template_file:
            template_file_content = template_file.read()
        return Template(template_file_content)

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    
    # def mail_mime(self):
    #     msg = MIMEText('Hello messge sent via python!\n' + self.text, 'plain', 'utf-8')
    #     msg['From'] = self._format_addr("蒙哥<%s>" % self.from_addr)
    #     msg['To'] = self._format_addr("谷歌<%s>" % self.to_addr)
    #     msg['Subject'] = Header('生物物理RSS','utf-8').encode()
    #     return msg
    #

    def send_message(self):
        # from_addr = "h.p.zhumeng@outlook.com"
        # to_addr = "h.p.zhumeng@gmail.com"
        self.text_generator()
        print(self.text)
        msg = MIMEText(self.text, 'html', 'utf-8')
        msg['From'] = self._format_addr("蒙哥<%s>" % self.from_addr)
        msg['To'] = self._format_addr("谷歌<%s>" % self.to_addr)
        msg['Subject'] = Header('生物物理RSS', 'utf-8').encode()
        s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        s.starttls()
        s.login("h.p.zhumeng@outlook.com", "microsoft2014")
        s.sendmail("h.p.zhumeng@outlook.com",self.to_addr, msg.as_string())

    def text_generator(self):
        for key in self.feed["entries"][:self.limit]:
            # print('*'*50+ "\n")
            # print("标题：" + key["title"] + "\n")
            # href = key['link']
            self.text += '<h2><a href=' + key["link"] + '>'+ key['title'] + '</a>' + '</h2>'
            # print("更新日期：" + key["updated"] + "\n")
            self.text += '<p>' + '<strong>' + "更新日期：" + "</strong>"  + key["updated"] + '<br>'
            # print("作者：" + key["author"] + "\n")
            self.text += "作者：" + key["author"] + '<br>'
            regex = re.compile("作者：.*?<br/>摘要：")
            s = key["summary_detail"]['value']
            sub = ''
            result = re.sub(regex, sub, s, 0)
            self.text += '<div style="font-size:13px;line-height:22px;text-decoration:none;color:#333;display:block">'  + "摘要：" + result + '</div>' + '<br>' + '</p>'
        print(self.text)
        self.text += '</body></html>'
        return self.text
        # print("摘要：" + result + "\n")
        # print('*'*50+ "\n")
        # text = text + read_template('message.txt').safe_substitute(d)

# RssToEmail().text_generator()
# print(RssToEmail().text)
RssToEmail().send_message()
# print(text)
