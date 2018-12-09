from collections import Counter
found1 = open('found1','r')
found1text = found1.read()
found2 = open('found2','r')
found2text = found2.read()
found3 = open('found3','r')
found3text = found3.read()
key = open('key','r')
keytext = key.read()
found = found1text + found2text + found3text
foundcounts = Counter(found)
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = len(found) - foundcounts[' '] - foundcounts['\n']
for i in alpha:
    print(i,100* foundcounts[i]/total)
