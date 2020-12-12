name = input("Enter file:")
if len(name) < 1 : name = "mbox.txt"
handle = open(name)

count = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    word = line.split()
    #time = word[5]
    tsp = word.split(':')
    t1 = tsp[0].split()

    for t in t1:
        if t not in count:
            count[t] = 1
        else:
            count[t] = count[t] + 1
    #for w in word:
    #    count[w] = count.get(w,0)+1
#print(count)
temp = list()
for k,v in count.items():
    newtup = (v,k)
    temp.append(newtup)

temp = sorted(temp,reverse=True)

for v,k in temp:
    print(v,k)
