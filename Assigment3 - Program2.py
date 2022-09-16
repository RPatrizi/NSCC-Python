"""
Student Name: Rodrigo Borges (W0420797)
Program Title: SecondLoop
Description:
Print:
1. the sum of all even number between 2 and 200 (inclusive)
2. the sum of all square numbers between 1 and 200 (inclusive)
"""

def sumOfEvenNumbers():
    sumEven = int(0)

    for counter in range (201) :
        if counter % 2 == 0:
            sumEven = int(sumEven + counter)
    return sumEven

def sumOfSquares():
    num = int(0)
    sumSquare = int(0)

    while (num ** 2) < 201 :
        sumSquare = sumSquare + (num ** 2)
        
        num += 1
    return sumSquare

#variables
    
#input

#process and output

print("\nThe sum of all even numbers between two and two hundred is:", sumOfEvenNumbers())
print("\nThe sum of all square numbers between one and two hundred is:", sumOfSquares())
print("")



