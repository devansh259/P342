import math
import library

def func(x,y):
    return (y*math.log(y))/x

x=[]
y=[]

x.append(2)
y.append(2.71828)

library.euler_forward(func,x,y,50)

f = open("q1a.txt", 'a')
for i in range(len(x)):
    f.write("%5.21f                %5.21f\n" % (x[i] , y[i]))
f.close()

print("For Q1.(a) solution at x = %.0f is %s" % (x[-1], y[-1]))

#output
#For Q1.(a) solution at x = 50 is 92.99236355318602