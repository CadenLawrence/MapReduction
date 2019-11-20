from operator import itemgetter
import sys

current_key = None
current_count = 0
key = None
for line in sys.stdin:
    line = line.strip()
    key, count = line.split(',')
    count = int(count)
    if current_key == key:
        current_count +=count
    else:
        if current_key:
            print(current_key+', '+str(current_count-1))
        current_count = count
        current_key = key
        
if current_key == key:
    if current_key:
        print (current_key+", " + str(current_count-1))