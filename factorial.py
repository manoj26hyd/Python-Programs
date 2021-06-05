# Program for Factorial of given number

def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    print("Factorial of" ,number, "is", fact)

factorial(number = 5)        