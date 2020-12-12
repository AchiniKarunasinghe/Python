fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox.txt"
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip() #remove whitespace
    if not line.startswith('From:'): continue
    word = line.split() #split into list
    count = count + 1
    print(word[1])
print("There were", count, "lines in the file with From as the first word")
