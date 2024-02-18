#!/usr/bin/python3
'''studentmapper.py'''
import sys
for line in sys.stdin:
	line=line.strip()
	words=line.split(',')
	print('%s\t%s\t%s'%(words[0],words[1],words[2]))
