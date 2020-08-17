a=[2,5,7]
b=[3,8,1]
sum=0
c=[]
for i in range(3):
	c.append(a[i]+b[i])
	sum+=a[i]*b[i]
print("sum of vectors A and B =" + str(c))
print("dot  products of vector=" + str(sum))
