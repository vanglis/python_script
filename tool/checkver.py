#!/usr/bin/env python
#-*-coding:utf-8-*-

import os

def main():
	path = '/data/httpd/'
	drs = sorted([x for x in os.listdir(path) if x.startswith('game')])
	for dr in drs:
		new_path = os.path.join(path,dr)
		if os.path.isdir(new_path):
			e_dir = os.listdir(new_path)
			e_size = os.popen('du -sh %s'%new_path).read().replace('\n','')
			print (e_size,e_dir)

if __name__ == '__main__':
	main()
