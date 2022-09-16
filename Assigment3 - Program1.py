"""
Student Name: Rodrigo Borges (W0420797)
Program Title: FirstLoop
Description:
Print:
1. all positive numbers that are divided by 10 and smaller than the number chosen by user.
2. all power of two that are smaller than the number chosen by user
"""

def printPositiveNumbers(number):
    x = int(1)

    while x < number :
        if x % 10 == 0:
            print(x, end = " ")

        x += 1
    return

def printPowersOfTwo(number):
    y = int(0)

    while (2 ** y) < number :
        print((2 ** y), end = " ")

        y += 1
    return

#variables

n = int(0)
    
#input

print("")
n = int(input("Please type your number: "))

#process and output

print("")
print("All positive numbers less than {} and divisible by 10 are: ".format(n))
printPositiveNumbers(n)
print("\n")
print("All powers of two numbers less than {} are: ".format(n))
printPowersOfTwo(n)
print("")



