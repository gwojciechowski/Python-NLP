import sys

n = 3;

if(len(sys.argv) > 1):
        n = int(float(sys.argv[1]));
for line in sys.stdin:
        print [line[i:i+n] for i in range(0, len(line)-n)];
