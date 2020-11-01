import integration
import matplotlib.pyplot as plt

def f(x):
    return 4/(1+x**2)

max = 50000
a= []
b=[]
n=[]
#Loop for calculating the pi value and error in each iteration
for i in range(10 , max, 50):
    n.append(i)
    fn, sigma = integration.montecarlo(0, 1, i, f)
    a.append(fn)
    b.append(sigma)

print("values after 50000 iterations=")
print(n[-1]," ",a[-1]," ",b[-1])

#solution:

#values after 50000 iterations=
#49990   3.147131376275127   0.6476014086975239