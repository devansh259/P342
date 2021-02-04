import final_library
import math

def f(x):
    return (x-5)*math.exp(x) +5

final_library.newton_raphson(f,5)
s=4.965114231744276
print("value of wein constant=")
print(((6.626*3/1.381)/s)*0.001)


#output
#solution found from newton raphson method: 4.965114231744276
#value of wein constant=
#0.0028990103307382923