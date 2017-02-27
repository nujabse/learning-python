# -*- coding:utf-8 -*-

import urllib2
import sys
import re


class hustPhysicsTeachers:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        # print sys.stdin.encoding
        self.num = 900
        self.total = 0
        # self.content = []

    def getpage(self, num):
        try:
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            headers = {'User-Agent': user_agent}
            url = 'http://phys.hust.edu.cn/xszdwjs/' + str(num) + '.htm'  # xi shi zi dui wu jie shao
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content   # 返回content 交给其他函数调用

        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print u"错误原因", e.reason

    def getInformation(self):
        content = self.getpage(self.num)
        total = 0  # 老师总人数
        pattern_teacher = re.compile('<strong>(.*?)</strong>.*?')
        pattern_contact = re.compile('[a-z0-9._%+-]+@[A-Z0-9.-]+\\.[a-z]+\\.[a-z]+\\.*', re.IGNORECASE)
        pattern_phone = re.compile('\d{3}-\d{8}|\d{4}-\d{7}')
        if not content:
            self.num += 1
            print ("page %d not found" % self.num)
        else:
            teachers = re.findall(pattern_teacher, content)
            print teachers[0]

            contacts = re.findall(pattern_contact, content)
            phone = re.findall(pattern_phone, content)
            # 防止找不到联系而退出循环
            if not contacts:
                print u"没有联系方式!\n"
            else:
                print contacts[0]
            if not phone:
                print u"没有电话号码!\n"
            else:
                print phone[0]

    def statistics(self):
        """
        统计人数
        """
        if self.getpage(self.num):
            # 计算有多少个老师
            self.total += 1

    def test(self):
        while self.num < 1054:
            self.getpage(self.num)
            self.statistics()
            self.num += 1
            print "*"*30
            print("checking page %d\n" % self.num)
            self.getInformation()

        print("总共有 %d 个老师\n" % self.total)

hustPhysicsTeachers().test()
# except urllib2.URLError, e:
#     if hasattr(e, "code"):
#         print e.code
#     if hasattr(e, "reason"):
#         print u"错误原因", e.reason
# print num
# print content

