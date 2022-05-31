import platform
import os
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('touch .prox.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("cythonn").mulai()
elif 'aarch' in arc:
	__import__("cython").mulai()
else:
	exit(f' Unknow device machine {arc}')
