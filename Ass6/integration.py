import math
import random

#derivative function
def derivative(f,a):
	h=0.0001
	return (f(a+h)-f(a-h))/(2*h)

#double derivative function
def double_derivative(f,a):
	h=0.0001
	return (f(a+h) +f(a-h) -2*f(a) )/(h**2)

#fourth derivative function
def fourth_derivative(f,a):
	h=0.0001
	return (double_derivative(f,a+h) +double_derivative(f,a-h) -2*double_derivative(f,a) )/(h**2)



#function to convert coefficient array into polynomial
def polynomial(coefficients,x):
	b=coefficients[-1]
	c=len(coefficients)
	for i in range(c-1):
		b+=coefficients[i]*(x**(c-i-1))
	return b


#derivative function for polynomials
def poly_dev(coefficients,a):
	h=0.000001
	return (polynomial(coefficients,a+h)-polynomial(coefficients,a-h))/(2*h)

#double derivative function for polynomials
def poly_double_dev(coefficients,a):
	h=0.000001
	return (polynomial(coefficients,a+h) + polynomial(coefficients,a-h) - (2*polynomial(coefficients,a)))/(h**2)
	#return (poly_dev(coefficients,a+h) - poly_dev(coefficients,a-h))/(2*h)

#midpoint /rectangular method
def midpoint(a, b, n, f):
    h = (b-a)/n
    sum=0
    for i in range(n):
        sum += h*f(((a+i*h)+(a+(i+1)*h))/2)

    return sum
# Trapezoidal rule
def trapezoidal(a,b,n,f):
    h = (b-a)/n
    sum = 0
    for i in range(1, n+1):
        sum += (h/2)*(f(a+((i-1)*h))+f(a+(i*h)))
    return sum

# Simpson's rule
def simpson(a, b, n, f):

    h = (b-a)/n
    sum=0
    for i in range(2 , n+1 , 2):
        sum += ( h /3 ) * (f(a + ((i - 2) * h)) + 4 * f(a + (( i - 1) * h)) + f( a + (i * h)) )
    return sum

# Montecarlo integration
def montecarlo(a, b, n, f):
    Fn = 0
    sigma = 0
    sum=0
    q=0
    for i in range(n):
        sum+= f(a+(b-a)*(random.random()))
        q += f(a+(b-a)*(random.random())) ** 2
    Fn=((b-a)*sum)/n
    sigma=(((q/n) - ((sum/n) ** 2))**(0.5))
    return Fn,sigma

#Finding the upper bound of N from the given error for different methods
def midpoint_iter_num(a, b, error , sec_der_max):
    return math.ceil(math.sqrt( (((b-a)**3) * sec_der_max) / (24 * error) ) )

def trapezoidal_iter_num(a, b, error ,sec_der_max):
    return math.ceil( math.sqrt( (((b-a)**3) * sec_der_max) / (12 * error) ) )

def simpson_iter_num(a, b, error , fourth_der_max):
    if(math.ceil(math.pow( ((((b-a)**5) * fourth_der_max) / (180 * error)) , (1/4) )) % 2 == 0):
        return math.ceil(math.pow( ((((b-a)**5) * fourth_der_max) / (180 * error)) , (1/4) ))
    else:
        return (math.ceil(math.pow( ((((b-a)**5) * fourth_der_max) / (180 * error)) , (1/4) )) + 1)
