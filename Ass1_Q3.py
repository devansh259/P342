x=True
i=1
sum=1
pre=0
while(x==True):
    sum=sum+1/(i+1)
    pre=pre+1/i
    if((sum-pre)<0.001):
        x=False
    else:
        i+=1
print(sum)
