import library

#question1
a=[]
b=[]
library.file_to_matrix('q1(a).txt',a)
library.read('q1(b).txt',b)

#Doing partial pivoting on the matrices
y=library.partial_pivot(a,b)

#LU Decompostion
library.LuDecomposition(a)

#Doing forward and backward substitution
sol=library.for_back(a,b)

#printing the solution
print("solution of q1=")
library.display(sol)


#output

#solution of q1=
#1.0
#-1.0
#1.0
#2.0
