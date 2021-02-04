import final_library

def linear_fit(x,y):
    d1=0
    d2=0

    for i in range(len(x)):
        d1+=x[i]*y[i]
        d2+=x[i]*x[i]
    a1=((len(x)*d1) - (sum(x)*sum(y)))/((len(x)*d2)-(sum(x)*sum(x)))
    a0=(sum(y)-a1*sum(x))/len(x)

    return a0,a1

x=[0,0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.7,3,3.3]
y=[2.2,1.96,1.72,1.53,1.36,1.22,1.10,1,0.86,0.75,0.65,0.60]
a1,a0=linear_fit(x,y)

print("for linear function:")
print("w_o=",a0)
print("w_1=",a1)

#output
#for linear function:
#w_o= -0.4747086247086247
#w_1= 2.029102564102564

