num = int(input("Enter a number you would like to know the factorial of: "))

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result      
print("The factorial of " + str(num) + " is " + str(factorial(num)))
