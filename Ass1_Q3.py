n=int(input("Enter the number of terms to find sum "))
x=True
i=1
sum=1
pre=0
if(n<=0):
    print("enter positive integers only")
else:
    while(x==True ):
        sum=sum+1/(i+1)
        pre=pre+1/i
        if((sum-pre)<0.001)|(i==n):
            x=False
        else:
            i=i+1
    if(x==True):
        print("sum doesn't change by 0.001 and sum=" + str(sum))
    else:
        print("sum for " + str(n) + " terms=" +str(sum))
