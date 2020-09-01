def partial_pivot(a,b):
	for i in range(len(a)):
		if(a[i][i]==0):
			for j in range(i+1,len(a)):
				if(abs(a[j][i]) > abs(a[i][i])):
					for k in range(len(a)):
						a[i][k],a[j][k]=a[j][k],a[i][k]
						b[i],b[j]=b[j],b[i]

def gauss_jordan(a,b):
	for i in range(len(a)):
		partial_pivot(a,b)
		pivot=a[i][i]
		for j in range(i,len(a)):
			a[i][j]=a[i][j]/pivot
		for j in range(i,len(b[0])):
			b[i][j]=b[i][j]/pivot
		for k in range(len(a)):
			if(k==i or a[k][i] ==0):
				continue
			factor=a[k][i]
			for l in range(i,len(a)):
				a[k][l]=a[k][l]-factor*a[i][l]
			for l in range(0,len(b[0])):
				b[k][l]=b[k][l]-factor*b[i][l]

def multiply(a,b):
	p=[[0,0,0],[0,0,0],[0,0,0]]
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				p[i][j]+= a[i][k] * b[k][j]
	for q in p:
		print(q)

A=[]
I=[]
with open("matrix.txt") as file:
	for i in range(3):
		A.append(list(map(float, file.readline().split())))

with open("vect.txt") as file:
	for i in range(3):
		I.append(list(map(float, file.readline().split())))

gauss_jordan(A,I)
print("Inverse of A matrix=")
for a in I:
	print(a)
print("Product of A matix and its inverse=")
c=[]
with open("matrix.txt") as file:
	for i in range(3):
		c.append(list(map(float, file.readline().split())))
multiply(c,I)
