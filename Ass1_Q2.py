def factorial(n):
    if n>=1:
        if n==1:
            return n
        else:
            return n * factorial(n-1)
    else:
        print("please take positive integers")
n = int(input("Enter an integer: "))
print("factorial of the number =" + str(factorial(n)))
