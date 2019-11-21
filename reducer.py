!/usr/bin/python
from operator import itemgetter
import sys
longest_list_dir = 0
longest_list_undir = 0
longest_key_dir = None
longest_key_undir = None
smallest_list_dir = 10000000
smallest_list_undir = 1
smallest_key_undir = None
smallest_key_dir = None
current_key = None
current_value = None
key = None
values = []
for line in sys.stdin:
    line = line.strip()
    key, value = line.split(',')
    print('--'*20 +'UnDir Adj List' +'--'*20)
    print(value+', '+ key)
    longest_list_undir = len(value)
    smallest_key_undir = key
    if current_key == key:
        values.append(value)
    else:
        if current_key:
            print('--'*20 +'UnDir/Dir Adj List' +'--'*20)
            print(current_key+', '+str(values))
            leng = len(values)
            if leng <= smallest_list_dir:
                smallest_list_dir = leng
                smallest_key_dir = current_key
            if leng >= longest_list_dir:
                longest_list_dir = leng
                longest_list_undir= leng
                longest_key_dir = current_key
                longest_key_undir = current_key
            values = []
            values.append(value)
        current_key = key
        current_value = value
        
if current_key == key:
    leng = len(values)
    if leng >= longest_list_dir:
        longest_list_dir = leng
        longest_key_dir = current_key
    print('--'*20 +'UnDir/Dir Adj List' +'--'*20)
    print (current_key+", " + str(values))
print('--'*20 +'Directed' +'--'*21)
print("The longest adjency list and maxium connectivity is "+longest_key_dir+" and the length is "+str(longest_list_dir))
print("The smallest adjency list and minmum connectivity is "+smallest_key_dir+" and the length is "+str(smallest_list_dir))
print('--'*20 +'Undirected' +'--'*21)
print("The longest adjency list and maxium connectivity is "+longest_key_undir+" and the length is "+str(longest_list_undir))
print("The smallest adjency list and minmum connectivity is "+smallest_key_undir+" and the length is "+str(smallest_list_undir))
    
    

