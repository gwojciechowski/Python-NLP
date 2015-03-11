import sys
import operator
import re
from collections import Counter

content = [];
for line in sys.stdin:
	content.append(line.lower());
words = re.findall(r'\w+', ''.join(content))
dict = Counter(words);

for w in sorted(dict, key=dict.get, reverse = True):
	print "%s:\t%s" % (w, dict[w])
	
most_common_words = sorted(dict, key = dict.get, reverse = True)
top_10 = most_common_words[:10]
print top_10
