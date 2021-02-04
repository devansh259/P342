import  final_library
import math

def func(x):
    return 1/math.sqrt(1 - (math.sin(math.pi/8))*(math.sin(x/2)*2))

n=10
t1=final_library.simpson(0,math.pi/2,n,func)
t=(4/math.sqrt(9.8))*t1

print("value of T for N=10 :")
print(t1)
