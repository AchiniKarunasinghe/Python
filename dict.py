name = input("Enter file:")
if len(name) < 1 : name = "mbox.txt"
handle = open(name)

count = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    word = line.split()
    for w in word:
        count[w] = count.get(w,0)+1

mostmail = None
mostcount = None

for m,c in count.items():
    if not '@' in m: continue
    if mostcount is None or c>mostcount:
        mostmail = m
        mostcount = c

print(mostmail,mostcount)
