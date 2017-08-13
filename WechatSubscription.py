import os
import time
import subprocess
import glob

# check local system before downloading
print("*" * 100)
print(os.uname(), "\n")
print(os.getcwd(), "\n")
os.chdir("/home/mathholic/Downloads/economist/audios")
print(os.getcwd(), "\n")
print("ALready Downloades Issues")
print(os.listdir(), "\n")
print("*" * 100)
# date = time.strftime("%Y%m%d")
# start downloading
date = '20170812'
number = 9053 
print('Now checking whether %s  issue is downloadable......' % date)
link = 'http://audiocdn.economist.com/sites/default/files/AudioArchive/2017/' + date + \
        '/Issue_'+ str(number)+ '_' + date + '_The_Economist_Full_edition.zip'
print(link)
subprocess.run(["wget", link])
filename = 

