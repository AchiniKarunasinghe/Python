def computepay(h,r):
    if h>40:
    	gross = (r*1.5)*(h-40)
        gross = gross+(40*r)
    else:
        gross = h*r
    return gross

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay(h,r)
print("Pay",p)
