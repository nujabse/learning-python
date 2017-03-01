# -*- coding:utf-8 -*-
import urllib2
import re
import sys
from lxml import etree
from openpyxl import load_workbook
from openpyxl.compat import range
import time



reload(sys)
sys.setdefaultencoding('utf-8')

counter = []
ids =[]
title = []
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Referer':'http://m.xiami.com/',

           'Cookie':'unsign_token=4f23ab3b94ae95850c9c5da7aef287e2; bdshare_firstime=1460894873450; cna=aSmVD89xbyQCAcdTMxgCkCtM; gid=146233966652053; CNZZDATA921634=cnzz_eid%3D1056600907-1470359568-%26ntime%3D1472796701; CNZZDATA2629111=cnzz_eid%3D1838752247-1470359096-%26ntime%3D1472796766; _xiamitoken=d1fb6eac5ee905225c46226aef039c7b; login_method=emaillogin; member_auth=1zmQGYxLvj0xivSXS41me3AW5rCATDfXlokE27Aq5QFydYxYNYOrkKuTQApN3iSSq2FCRfnEhWQSRr0; user=22156413%22mathholic%22images%2Favatar_new%2F443%2F22156413_1394536403_1.jpg%222%2219655%22%3Ca+href%3D%27%2Fwebsitehelp%23help9_3%27+%3EDo%E2%80%A2%3C%2Fa%3E%22179%2267%2211887%2215e6c2b9dc%221488254727; _m_h5_tk=7c41b5eb2452b26db16b5b747b515b9c_1488283863638; _m_h5_tk_enc=15ff1a0b4a8465622b67a195472776fe; sec=58b57dd3547bf80f1f4a31a21817dcede3d13cc6; t_sign_auth=1; l=Ar29SsHoaUXW1EPeOTyxcTHnTRO3X/G5; isg=AoaGbUI5IiROGvZBVu5Xyu5Y13U5A8qhmkUoi3Cvd6mRcyaN2XcasWxDJRhF'
           }
def getdata():
    """由于虾米部分音乐下架，可能部分音乐数据无法查证"""
    for i in range(1, 10000):
        try:
            url = 'http://www.xiami.com/count/getplaycount?id=' + str(i) + '&type=song&_xiamitoken=d1fb6eac5ee905225c46226aef039c7b'  # song ID
            song_url = 'http://www.xiami.com/song/' + str(i)
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            pattern_count = re.compile('[:](\d{1,100000000})[,]')
            count = re.findall(pattern_count, content)
            #
            # request_song = urllib2.Request(song_url, headers=headers)
            # response_song = urllib2.urlopen(request_song)
            # content_song = response_song.read().decode('utf-8')
            # page = etree.HTML(content_song)
            # index_song = '//*[@id="title"]/h1/text()'

            # name = page.xpath(index_song)

            # song = name
            id = i
            if counter:
                counter.append(count[0])
            else:
                counter.append(None)
            ids.append(id)
            # title.append(name)
            print ("song number %d  play count %s" % (i, count))


        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print "reason", e.reason

        time.sleep(3)  # 设置时间间隔为3秒
        print(u"休息一下。。。。。")

def writeToExcel():
    """
    存储采集数据到excel
    :return:
    """
    wb = load_workbook(u"数据采集.xlsx")
    ws1 = wb["xiami"]
    # ws1['A1'] = u"编号"
    # ws1['B1'] = "ids"
    # ws1['C1'] = "title"
    # ws1['D1'] = "counter"
    # ws1['E1'] = "artist"

    colA = ws1['A']
    colB = ws1['B']
    colC = ws1['C']
    colD = ws1['D']

    for i in range(len(ids)):
        index = 'B' + str(i + 2)
        ws1[index] = ids[i]
    print(u"写入id.....")
    # for i in range(len(title)):
    #     index = 'C' + str(i + 2)
    #     ws1[index] = title[i]
    # print(u"写入title成功")
    for i in range(len(counter)):
        index = 'D' + str(i + 2)
        ws1[index] = counter[i]
    print(u"写入counter.....")
    wb.save(u"数据采集.xlsx")
    print(u"采集数据完成！")

    # for i in range(len(self.working_degree1)):
    #     index = 'G' + str(i + 2)
    #     ws1[index] = self.working_degree1[i]
    # print(u"写入讲师成功")

getdata()
writeToExcel()




