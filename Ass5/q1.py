import math
import library

#for question 1(a)
def f(x):
	return math.log(x) -math.sin(x)

#for question 1(b)
def g(x):
	return ( -x - math.cos(x) )

#bisection method for 1(a)
library.bisection(f,1.5,2.5)

#regular falsi method for 1(a)
library.regular_falsi(f,1.5,2.5)

#newton raphson for 1(a)
library.newton_raphson(f,1.5)


#bisection method for 1(b)
library.bisection(g,-1,0)

#regular falsi method for 1(b)
library.regular_falsi(g,-1,0)

#newton raphson for 1(b)
library.newton_raphson(g,0)



#output for question 1(a):

#solution found from bisection method: 2.21905517578125
#solution found from regular falsi method: 2.218714563209797
#solution found from newton raphson method: 2.219107148913746


#output for question 1(b):

#solution found from bisection method: -0.73907470703125
#solution found from regular falsi method: -0.7390851332151607
#solution found from newton raphson method: -0.7390851332151607

