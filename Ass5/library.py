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

#bisection function 
def bisection(f,a,b):
	max_itr=200
	tol=0.0001
	n=1
	k=1
	beta=1.5
	counter=0
	#bracketing loop
	while(f(a)*f(b)>0 and counter!=12):
		if abs(f(a)) < abs(f(b)) :
			a=a-(beta*(b-a))
		elif abs(f(a)) > abs(f(b)) :
			b=b+(beta*(b-a))
		counter=counter+1
	#loop for checking convergence
	while(n<=max_itr and k==1):		
		c=(a+b)/2
		file=open("q1(b)bisection.txt",'a')
		file.write("%i         %5.21f\n" % (n, abs(a-b)))
		file.close()
		if(f(c)==0 or ((b -a)/2 < tol)):
			print("solution found from bisection method:",c)
			k=2

		else:
			n=n+1
			if f(a)*f(c) < 0:
				b=c
			elif f(b)*f(c) < 0:
				a=c
			else:
				print("bisection method fails")
				return None

#regular falsi function
def regular_falsi(f,a,b):
	tol=0.000001
	max_itr=200
	n=1
	k=1
	beta=1.5
	counter=0
	l=0
	c=0
	#bracketing loop
	while(f(a)*f(b)>0 and counter!=10):
		if abs(f(a)) < abs(f(b)) :
			a=a-(beta*(b-a))
		elif abs(f(a)) > abs(f(b)) :
			b=b+(beta*(b-a))
		counter=counter+1


	#loop for checking convergence
	while(n<=max_itr and k==1):
		l=c
		c= b-(((b-a)*f(b))/(f(b)-f(a)))

		file=open("q1(b)regular.txt",'a')
		file.write("%i         %5.21f\n" % (n, abs(l-c)))
		file.close()
		if(f(c)==0 or ((b -a)/2 < tol)):
			print("solution found from regular falsi method:",c)
			k=2

		else:
			n=n+1
			if f(a)*f(b) < 0:
				b=c
			elif f(a)*f(b) > 0:
				a=c
			else:
				print("regular_falsi method fails")
				return None		

#derivative function
def derivative(f,a):
	h=0.0001
	return (f(a+h)-f(a-h))/(2*h)

#double derivative function
def double_derivative(f,a):
	h=0.0001
	return (f(a+h) +f(a-h) -2*f(a) )/(h**2)

#newton raphson function
def newton_raphson(f,a):
	n=1
	k=1
	max_itr=200
	tol=0.000001
	c=a
	#loop for checking convergence
	while(n<=max_itr and k==1):

		c=a-f(a)/derivative(f,a)
		file=open("q1(b)newton.txt",'a')
		file.write("%i         %5.21f\n" % (n, abs(c-a)))
		file.close()
		if(abs(c-a)<tol):
			k=2
			print("solution found from newton raphson method:",c)
		else:
			n+=1
			a=c	

#function to convert coefficient array into polynomial
def polynomial(coefficients,x):
	b=coefficients[-1]
	c=len(coefficients)
	for i in range(c-1):
		b+=coefficients[i]*(x**(c-i-1))
	return b

#derivative function for polynomials
def poly_dev(coefficients,a):
	h=0.000001
	return (polynomial(coefficients,a+h)-polynomial(coefficients,a-h))/(2*h)

#double derivative function for polynomials
def poly_double_dev(coefficients,a):
	h=0.000001
	return (polynomial(coefficients,a+h) + polynomial(coefficients,a-h) - (2*polynomial(coefficients,a)))/(h**2)
	#return (poly_dev(coefficients,a+h) - poly_dev(coefficients,a-h))/(2*h)

#lagurre function to find a root of a polynomial
def lagurre(coefficients,a):
	degree=len(coefficients)-1
	max_itr=100
	tol=0.000001
	k=1
	i=1
	while(i!=max_itr and k==1):
		if((polynomial(coefficients,a)) < tol):
			k=2
			return a
		else:
			g=(poly_dev(coefficients,a))/(polynomial(coefficients,a))
			h=g**2-((poly_double_dev(coefficients,a))/(polynomial(coefficients,a)))
			b=(((degree*h)- (g**2))*(degree-1))**(0.5)

			if(g>0):
				c=degree/(g+b)
			else:
				c=degree/(g-b)
			a=a-c
			i+=1

#fucntion to divide a polynomial by an binomial
def synthetic_division(f,q):
	tol=0.000001
	
	for i in range(1,len(f)):
		e=(-1)*q[-1]*f[i-1]
		f[i]+=e

	if(f[-1]<tol):
		f.pop(-1)
	return f

def root_finder(fag):
	#fag=[1,-3,-7,27,-18]
	while(len(fag)>1):
		a=lagurre(fag,10)
		print(a)
		fag=synthetic_division(fag,[1,-a])
					

