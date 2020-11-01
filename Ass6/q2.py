import integration

def f(x):
    return x/(1+x)
res = 1.30685281944  #  anlaytical result
#for n=5
n = 5
m1 = integration.midpoint(1, 3, n, f)
t1 = integration.trapezoidal(1, 3, n, f)
s1 = integration.simpson(1, 3, n, f)
# for n=10
n = 10
m2 = integration.midpoint(1, 3, n, f)
t2 = integration.trapezoidal(1, 3, n, f)
s2 = integration.simpson(1, 3, n, f)
# for n=25
n = 25
m3 = integration.midpoint(1, 3, n, f)
t3 = integration.trapezoidal(1, 3, n, f)
s3 = integration.simpson(1, 3, n, f)

solution = [['N', 'Midpoint', 'Trapezoidal', 'Simpson', 'Analytical result'],
        [5, m1, t1, s1, res], [10, m2, t2, s2, res], [25, m3, t3, s3, res]]

for b in solution:
    print(b)

#solution
#['N', 'Midpoint', 'Trapezoidal', 'Simpson', 'Analytical result']
#[5, 1.308092114284065, 1.3043650793650796, 1.3121693121693123, 1.30685281944]
#[10, 1.3071646395900398, 1.3062285968245722, 1.3068497693110694, 1.30685281944]
#[25, 1.3069028019555275, 1.3067528394240817, 1.3270554475235471, 1.30685281944]

