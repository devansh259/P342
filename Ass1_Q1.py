n=int(input("Enter any integer"))
s=0
if(n>=0):
    for i in range(n):
        s=s+i
    print("sum upto to the number=" + str(s))
else:
    for i in range(-n):
        s=s+i
    print("sum upto to the number=" + str(-s))
        
