#LU Decomposition function
def LuDecomposition(a):
	n=len(a)
	for i in range(n):
		for j in range(n):
			sum=0
			#For lower triangular matrix
			if(i<=j):
				for k in range(i):
					sum+=a[i][k]*a[k][j]
				a[i][j]=a[i][j]-sum
			#For upper triangular matrix
			else:
				for k in range(j):
					sum+=a[i][k]*a[k][j]
				a[i][j]=(a[i][j]-sum)/a[j][j]

#Forward and backward substituion Function
def forward_backward(a, b):
	n=len(a)
	m=len(b[0])
	y=[[0 for y in range(m)] for x in range(n)]
	x=[[0 for y in range(m)] for x in range(n)]
	#forward substitution
	for i in range(n):
		for j in range(m):
			sum=0
			for k in range(i):
				sum=sum+(a[i][k] * y[k][j])
			y[i][j]= b[i][j] - sum
	#backward substitution
	for i in range(n-1,-1,-1):
		for j in range(m):
			sum=0
			for k in range(i+1,n):
				sum+=a[i][k]*x[k][j]
			x[i][j]=(y[i][j]-sum)/a[i][i]

	return x

#Matrix reading function
def file_to_matrix(file,name):
	f=open(file,'r')
	for i in f:
		name.append([float(n) for n in i.split()])

def read(file,name):
	f=open(file, 'r')
	lsplit = f.readline().split()
	for val in lsplit:
		name.append(float(val))

#function to print matrix
def display(x):
	for q in x:
		print(q)

#partial pivot function
def partial_pivot(a,b):
	num=0
	for i in range(len(a)):
		if(a[i][i]==0):
			for j in range(i+1,len(a)):
				if(abs(a[j][i]) > abs(a[i][i])):
					num+=1
					for k in range(len(a)):
						a[i][k],a[j][k]=a[j][k],a[i][k]
					if(b!=0):
						b[i],b[j]=b[j],b[i]
	return num

#gauss_jordan function
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

#matix multiplication function
def multiply(a,b):
	l=len(b)
	m=len(b[0])
	n=len(a)
	p= [[0 for y in range(m)] for x in range(n)]
	for i in range(n):
		for j in range(m):
			for k in range(l):
				p[i][j]+= a[i][k] * b[k][j]
	return p

#determinant function
def determinant(a):
	det=1
	for i in range(len(a)):
		det=det*a[i][i]
	return det

def for_back(a, b):
    n = len(a)
    z = []
    for i in range(n):
        z.append(float(0))
  
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += a[i][j]*z[j]
        z[i]+=b[i]-sum

    x = []
    for i in range(n):
        x.append(float(0))
 
    for i in range(n-1,-1,-1):
    	sum=0
    	for k in range(i+1,n):
    		sum+=a[i][k] *x[k]
    	x[i]+= (z[i] -sum)/a[i][i]

    return x




					

