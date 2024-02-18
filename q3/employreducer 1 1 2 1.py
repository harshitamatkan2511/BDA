#!/usr/bin/python3
'''employreducer.py'''
import sys
un={}
ans={}
for line in sys.stdin:
	line=line.strip()
	unit,salary=line.split('\t')
	if unit in un:
		un[unit].append(int(salary))
	else:
		un[unit]=list()
		un[unit].append(int(salary))
for x in un:
	ans[x]=sum(un[x])
	print(f"Unit name {x} has total salary {ans[x]}")	
