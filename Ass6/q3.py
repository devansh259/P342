import math
import integration

def f(x):
    return math.exp(-x**2)

#finding number of iterations for given error
print("using midpoint method, integral=",integration.midpoint(0,1,integration.midpoint_iter_num(0,1,0.001,2),f))
print("using trapezoidal method, integral=",integration.trapezoidal(0,1,integration.trapezoidal_iter_num(0,1,0.001,2),f))
print("using simpson method, integral=",integration.simpson(0,1,integration.simpson_iter_num(0,1,0.001,12),f))


#solution
#using midpoint method, integral= 0.7471308777479975
#using trapezoidal method, integral= 0.7464612610366896
#using simpson method, integral= 0.7468553797909873