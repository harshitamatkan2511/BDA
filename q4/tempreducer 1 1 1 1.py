#!/usr/bin/python3
'''tempreducer.py'''
import sys
temperature={}
ans={}
for line in sys.stdin:
	line=line.strip()
	year,temp=line.split('\t')
	if year in temperature:
		temperature[year].append(int(temp))
	else:
		temperature[year]=list()
		temperature[year].append(int(temp))
for x in temperature:
	ans[x]=[sum(temperature[x])/len(temperature[x]),min(temperature[x]),max(temperature[x])]
	print(f"Average for year {x} is {ans[x][0]}")
	print(f"Minimum for year {x} is {ans[x][1]}")
	print(f"Maximum for year {x} is {ans[x][2]}\n")
	
