from operator import itemgetter
import sys
longest_list = 0
longest_key = None
smallest_list = 0
current_key = None
current_value = None
key = None
values = []
for line in sys.stdin:
    line = line.strip()
    key, value = line.split(',')
    if current_key == key:
        values.append(value)
    else:
        if current_key:
            print(current_key+', '+str(values))
            leng = len(values)
            if leng >= longest_list:
                longest_list = leng
                longest_key = current_key
            values = []
            values.append(value)
        current_key = key
        
if current_key == key:
    leng = len(values)
    if leng >= longest_list:
        longest_list = leng
        longest_key = current_key
    print (current_key+", " + str(values))

print("The longest adjency list is "+longest_key+" and the length is "+str(longest_list))
    
    

