import sys

for line in sys.stdin:
    if line.startswith('#'):
        continue
    else:
        line = line.strip()
        # split the line into words
        words = line.split()
        # increase counters
        pair = (words[0], 1)
        print(str(words[0])+","+ str(1))