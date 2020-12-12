name = input("Enter file name: ")
if len(name) < 1: name = "mbox.txt"
handle = open(name)

count = dict()
for line in  handle:
    line = line.rstrip()
    if not line.startswith('Date:'): continue
    #if not '2008-01-03' in line: continue
    word = line.split()
    x = word[5]
    if not ':' in x: continue
    temp = x.split(':')
    rel = temp[0].split()
    #print(rel)

    for i in rel:
        count[i] = count.get(i,0)+1
#print(count)

for k,v in sorted(count.items()):
    print(k,v)
#emp = sorted(emp,reverse=True)
