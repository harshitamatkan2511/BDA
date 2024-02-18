#!/usr/bin/python3
import sys
current_word = None
current_count = 0
word = None
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t',1)
    try:
    	count = int(count)
    except ValueErrors:
    	     continue
    if current_word == word:
    	current_count += count
    else:
    	if current_word:
    		print ('%s\t%s' % (current_word, current_count))
    	current_count = count
    	current_word = word
    	
if current_word == word:
	print('%s\t%s' % (current_word, current_count))
	
	
	
#hadoop jar '/home/hdoop/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar' -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /temp.txt -output /out2
# above is the code to link the mapper to reducer
