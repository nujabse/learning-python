# -*- coding:utf-8 -*-

import urllib2
import sys
import re


print sys.stdin.encoding
num = 900
content = []
class hustPhysicsTeachers:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        print sys.stdin.encoding
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

def getPage(num):
    try:
        url = 'http://phys.hust.edu.cn/xszdwjs/' + str(num) + '.htm'  # xi shi zi dui wu jie shao
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('utf-8')
        return content

    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print u"错误原因", e.reason


def getInformation():
    pattern_teacher = re.compile('<strong>(.*?)</strong>.*?')
    pattern_contact = re.compile('[a-z0-9._%+-]+@[A-Z0-9.-]+\\.[a-z]+\\.[a-z]+\\.*', re.IGNORECASE)
    teachers = re.findall(pattern_teacher, content)
    print teachers[0]
    contacts = re.findall(pattern_contact, content)
    print contacts[0]

while num < 1000:
    getPage(num)
    num += 1
    print("checking page %d" % num)
    getInformation()

# except urllib2.URLError, e:
#     if hasattr(e, "code"):
#         print e.code
#     if hasattr(e, "reason"):
#         print u"错误原因", e.reason
# print num
# print content

