import os
import time

#Linux版本
# Windows tip
# windows钟把反斜杠（\）作为目录分隔符，而python中反斜杠表示转义符。用双斜杠或者在前面加r
# The files and directories to be backed up are specified in a list.
source = ['/home']

# the backup must be stored in a main backup directory
target_dir = 'D:\code\python'

# 版本1
# the files are backed up into a zip file.
# the name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
# we use the zip commond (in Uniix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target,' '.join(source))

# run the backup
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')

# 版本2
# the current day is the name of the subdirectory in the main directory
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
        os.mkdir(today)
        print('successfully created directory',today)
# os.sep ——会根据你的操作系统给出目录分隔符，在unix系统是'/',在windows 是'\\'，mac OS 下是':'
target = today + os.sep +now +'.zip'
zip_command = "zip -qr '%s' %s" %(target,' '.join(source))

if os.system(zip_command) == 0:
    print('successful backup to',target)
else:
    print('backup failed')


# 版本3
today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

comment = input('enter a comment:')
if len(comment) == 0:
    target = today + os.sep + now +'.zip'
else:
    target = today + os.sep + now +'_' + comment.replace(' ','_') +  '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('successfully created directory',today)

zip_command = "zip -qr '%s' %s" %(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('successful backup to', target)
else:
    print("backup failed")