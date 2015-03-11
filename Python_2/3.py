import sys
import re

reg = sys.argv[1];
n = 15

if(len(sys.argv) > 2): 
        n = int(float(sys.argv[2]))

for line in sys.stdin:
        words = re.search(reg, line)
        if(words):
                print line[(words.start()-n-1):(words.start())]+'  {!s}  '.format(reg) + line[(words.end()):(words.end()+n+1)]
