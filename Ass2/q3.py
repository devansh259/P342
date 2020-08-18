m=[[1,2,3],
   [4,5,6],
   [7,8,9]] 
n=[[-1,2,7],
   [9,-5,6],
   [7,8,-9]]

a=[2,5,7]
b=[]
p=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for row in m:
	sum=0
	for i in range(3):
		sum+=row[i]*a[i]
	b.append(sum)

for i in range(len(m)):
	for j in range(len(n[0])):
		for k in range(len(n)):
			p[i][j]+= m[i][k] * n[k][j]

print("Product of A and M = " + str(b))
print("Product of M and N = ")
for row in p:
    print(row)
