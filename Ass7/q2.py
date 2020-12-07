import library


def dydx(v,x):
    return v

def dzdx(y, z, x):
    return 1 - z - x

#initial values
x = 0
y = 2
z = 1
h = 0.3

y, x = library.runge_kuttaR4(dydx,dzdx , x, y, z, 11, h, "q2.txt")
print("For Q.2 Approximate solution at x = %.0f is %s" % (x, str(y)))

#Output
#For Q.2 Approximate solution at x = 11 is -39.70924865888711