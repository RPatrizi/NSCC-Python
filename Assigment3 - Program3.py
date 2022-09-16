"""
Student Name: Rodrigo Borges (W0420797)
Program Title: ThirdLoop
Description:
Print:
1. the smalest and largest numbers inputed by user.
2. the quantity of even numbers inputed by user.
"""

#variables
smallest = int()
biggest = int()
numOfEven = int(0)
num = str("")
initial = True

#input and process

num = input("Please enter a number: ")

while num.lower() != "exit" :

    while initial == True :
        smallest = int(num)
        biggest = int(num)
        initial = False

    if int(num) < smallest :
        smallest = int(num)

    elif int(num) > biggest :
        biggest = int(num)

    if int(num) % 2 == 0 :
        numOfEven += 1

    num = input("Please enter a number or type EXIT to finish: ")
    
#output

print("\nThe smallest number typed is:", smallest)
print("\nThe largest number typed is:", biggest)
print("\nThe quantity of even numbers typed is:", numOfEven)
print("")