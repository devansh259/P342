def partial_pivot(a,b):
	for i in range((len(a))-1):
		if(a[i][i]==0):
			for j in range(i+1,len(a)):
				if(abs(a[j][i]) > abs(a[i][i])):
					a[i],a[j]=a[j],a[i]
					b[i],b[j]=b[j],b[i]

def gauss_jordan(a,b):
	partial_pivot(a,b)
	for i in range(len(a)):
		pivot=a[i][i]
		for j in range(i,len(a)):
			a[i][j]=a[i][j]/pivot
		b[i]=b[i]/pivot
		for k in range(len(a)):
			if(k==i or a[k][i] ==0):
				continue
			factor=a[k][i]
			for l in range(i,len(a)):
				a[k][l]=a[k][l]-factor*a[i][l]
			b[k] = b[k]-factor*b[i]

print("Question_1 :")
vect= open("b1.txt","r")
vec= vect.readline().split()
b=[]
a=[]
for i in vec:
	b.append(float(i))
with open("a1.txt") as file:
	for i in range(3):
		a.append(list(map(float, file.readline().split())))
gauss_jordan(a,b)
print("solution:",b)

print("Question_2 :")
vect= open("b2.txt","r")
vec= vect.readline().split()
b=[]
a=[]
for i in vec:
	b.append(float(i))
with open("a2.txt") as file:
	for i in range(3):
		a.append(list(map(float, file.readline().split())))
gauss_jordan(a,b)
print("solution:",b)
