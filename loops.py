largest = None
smallest = None
eee = None
while True:
    num = input("Enter a number: ")
    try:
        n = int(num)
    except:
        eee = 'Invalid input'
    if largest is None:
        largest = n
    elif largest < n:
    	largest = n
    if smallest is None:
        smallest = n
    elif smallest > n:
    	smallest = n
    if num == "done" : break
if eee is not None:
    print(eee)
print("Maximum is", largest)
print("Minimum is", smallest)
