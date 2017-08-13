import os
import time
import subprocess

print("*" * 100)
print(os.uname(), "\n")
print(os.getcwd(), "\n")
os.chdir("/home/mathholic/Downloads/economist/audios")
print(os.getcwd(), "\n")
print("ALready Downloades Issues")
print(os.listdir(), "\n")
print("*" * 100)
# date = time.strftime("%Y%m%d")
date = '20170812'
number = 9053 
print('Now checking whether %s  issue is downloadable......' % date)
link = 'http://audiocdn.economist.com/sites/default/files/AudioArchive/2017/' + date + \
        '/Issue_'+ str(number)+ '_' + date + '_The_Economist_Full_edition.zip'
print(link)
os.system('wget link')
