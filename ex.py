# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        x = line[19:]
        ft = float(x)
        total = total+ft
        count = count + 1
    else : continue
#print(count)
#print(total)
#print(total/count)
print("Average spam confidence: ",total/count)
