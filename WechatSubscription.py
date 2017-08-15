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
print("check if it's Saturday........")
if time.strftime("%w") != '6':
	print("It's %s Just wait for the next Saturday......" % time.strftime("%Y%m%d"))
else:
	# start downloading
	# date = '20170812'
	date = time.strftime("%Y%m%d")
	# number = 9053 
	number = 9053 + int(time.strftime("%W")) - 32
	print('Now checking whether %s  issue is downloadable......' % date)
	link = 'http://audiocdn.economist.com/sites/default/files/AudioArchive/2017/' + date + \
		'/Issue_'+ str(number)+ '_' + date + '_The_Economist_Full_edition.zip'
	print(link)
	subprocess.run(["wget", link])
	# extract zip files and make a new directory to store them
	files = glob.glob('*.zip')[0]
	print(files)
	folder = os.path.splitext(files)[0]
	print(folder)
	subprocess.run(["mkdir", folder])
	os.system("ls -lh")
	subprocess.run(["unzip", files, "-d", folder])
	print("download and extracting finished\n" + "*"*100)
	# delete zip archieves
	subprocess.run(["rm", files])
