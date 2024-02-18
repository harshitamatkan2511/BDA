#!/usr/bin/python3
'''studentreducer.py'''
import sys
i=0
reg=[x for x in range(20)]
name=[x for x in range(20)]
marks=[x for x in range(20)]
for line in sys.stdin:
	line=line.strip()
	reg[i],name[i],marks[i]=line.split("\t")
	i=i+1
for x in range(20):
	for y in range(19-x):
		if name[y]>name[y+1]:
			temp=name[y]
			name[y]=name[y+1]
			name[y+1]=temp
				

			temp=reg[y]
			reg[y]=reg[y+1]
			reg[y+1]=temp
			

			temp=marks[y]
			marks[y]=marks[y+1]
			marks[y+1]=temp
			
print("Sorted based on names:")
for i in range(20):
	print('%s\t%s\t%s'%(reg[i],name[i],marks[i]))


