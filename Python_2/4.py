import sys
import re
from collections import Counter

count = []
for line in sys.stdin:
	count.append(line);

char = re.findall(r'[a-zA-Z]', ''.join(count));
dict = Counter(char);

for key in sorted(dict.iterkeys()):
	print "%s:\t%s" % (key, dict[key]);
