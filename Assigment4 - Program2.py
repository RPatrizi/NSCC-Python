"""
Student Name: Rodrigo Borges (W0420797)
Program Title: Assignment 4, Program 2, Factorial Calculation
Description: Write a program that accepts an integer n number, then displays the factorial value of the number n. 
"""


def factorial(number):

    #variables
    # variable initially set as 1 because of the multiplication
    factorialResult = 1

    #process
    # for loop decreasing number by 1 and multiplying by the variable factorialResult
    for x in range(number, 0, -1) :
        factorialResult = factorialResult * x

    return factorialResult

# ask user to inform n and call function
n = int(input("\nEnter the value of n: "))
factorial(n)

#output
print("The factorial value of {0} is: {1}\n".format(n, factorial(n)))