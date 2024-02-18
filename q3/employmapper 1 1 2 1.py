#!/usr/bin/python3
'''employmapper.py'''
import sys
for line in sys.stdin:
	line=line.strip()
	Empno,EmpName,Unit,Desig,Salary=line.split(',')
	print('%s\t%s'%(Unit,Salary))
