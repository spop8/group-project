'''
Understand: 
I have to get a number and calculate the factorial
Input: number output: factorial

Clues
- 

Assemble
INPUT --> ask user for an integer

create FUNCTION factorial that takes 1 parameter (the integer from above)
create VARIABLE that will be the result
create FOR LOOP that will iterate over a range of numbers 
    - the range starts at 1 and goes up to the number + 1 so the number is included  
    - multiplies the previous result by the next number
returns the RESULT
PRINTS --> the factorial/RESULT in a sentence


'''


num = int(input("Enter a number you would like to know the factorial of: "))

def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result      
print("The factorial of " + str(num) + " is " + str(factorial(num)))
