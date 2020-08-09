n=int(input("Enter any natural number"))
s=0
if(n>1):
    for i in range(n):
        s=s+i
    print("sum upto to the number=" + str(s))
else:
    print("please enter positive number greater than 1")
        
