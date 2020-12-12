fname = input("Enter file name: ")
fh = open(fname)
allWords = list()
result = list()
for words in fh:
    words.rstrip()
    x = words.split()
    allWords = allWords + x

for i in allWords:
    if i not in result:
        result.append(i)
result.sort()
print(result)
