
import library

def func(x,y):
    return 6-2*y/x

x=[]
y=[]

x.append(3)
y.append(1)
library.euler_forward(func,x,y,50)

f = open("q1b.txt", 'a')
for i in range(len(x)):
    f.write("%5.21f                %5.21f\n" % (x[i] , y[i]))
f.close()

print("For Q1.(b) solution at x = %.0f is %s" % (x[-1], str(y[-1])))

#Output
#For Q1.(b) solution at x = 50 is 434.9243991472538