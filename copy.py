# -*- coding:utf-8 -*-
import os
import time
import shutil
import sys
from fnmatch import fnmatch

# 복사를 진행하도록 할 기본 디렉토리를 구한다
root = '/Volumes/EOS_DIGITAL/DCIM'
if not os.path.exists(root):
	sys.exit()

os.system('/usr/local/bin/growlnotify -t "EOS_DIGITAL 폴더" -m "복사를 진행중입니다"')

def doCopy(target_path):
	"지점으로부터 복사를 진행한다"
	for dirname, dirnames, filenames in os.walk(target_path):
		for filename in filenames:
			filepath = os.path.join(dirname, filename)
			n_filepath = os.getenv("HOME") + "/Documents/Lightroom/" + str(time.strftime("%Y-%m-%d",time.localtime(os.path.getmtime(filepath))))
			if not os.path.exists(n_filepath):
				os.mkdir( n_filepath )
			shutil.copy2(filepath, n_filepath + "/" + filename)

# EOS5D가 붙는 디렉토리만을 복사하도록 지정한다
pattern = "*EOS5D"
for path, subdirs, files in os.walk(root):
	for name in subdirs:
		if fnmatch(name, pattern):
			doCopy(root+'/'+name)

os.system('/usr/local/bin/growlnotify -t "EOS_DIGITAL 폴더" -m "모든 파일이 정상적으로 복사되었습니다"')