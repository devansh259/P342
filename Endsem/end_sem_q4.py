import final_library

g=-9.8
def dydx(v,x):
    return v

def dzdx(y,z,x):
    return g
x0 =0
y0=2
x_lim=5
yn=45
h=0.03
z1=30
zh=50

y,z=final_library.ode_ShootingMethod(dydx,dzdx,x0,x_lim,y0,yn,z1,zh,h,"write.txt")
print("velocity at the lauch pad =",z)

#output
#velocity at the lauch = 33.13183433133732