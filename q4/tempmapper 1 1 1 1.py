#!/usr/bin/python3
'''tempmapper.py'''
import sys
for line in sys.stdin:
	line=line.strip()
	year,temp=line.split('\t')
	print("%s\t%s"%(year,temp))
