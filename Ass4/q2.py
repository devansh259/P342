import library

a=[]
b=[]
library.file_to_matrix('q2(A).txt',a)
library.file_to_matrix('q2(I).txt',b)

#partial pivoting
num=library.partial_pivot(a,b)

#LU decomposition
library.LuDecomposition(a)

#Determinant
det=library.determinant(a)

#Finding number of row operations
print("Determinant of A=",((-1)**num)*det)

#finding if inverse exists or not
if(det==0):
	print("Inverse does not exist for this matix")

else:
	print("Inverse exists for this matrix as Determinant is non zero")
#Forward-Backward Substition
x=library.forward_backward(a,b)

print("solution for Q2=")
library.display(x)

#output
#Determinant of A= -36.0
#Inverse exists for this matrix as Determinant is non zero
#solution for Q2=
#[-0.25000000000000006, 1.6666666666666672, -1.8333333333333333, 0.3333333333333333]
#[0.08333333333333337, -0.666666666666667, 0.8333333333333333, 0.0]
#[0.16666666666666666, -0.33333333333333326, -0.3333333333333333, 0.0]
#[-0.08333333333333333, 0.6666666666666666, 0.16666666666666666, 0.0]