import re
hd = open('ex.txt')
datalist = list()
sum = 0
#count = 0
for line in hd:
    line = line.rstrip()
    numbers = re.findall('[0-9]+',line)
    if len(numbers) == 0 : continue
    datalist.extend(numbers)

for num in datalist:
    x = float(num)
    sum = sum+x
    #count = count+1
print(sum)
#print(count)
