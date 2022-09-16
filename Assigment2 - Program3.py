"""
Student Name: Rodrigo Borges (W0420797)
Program Title: Auto Insurance
Description: Compute monthly insurance according schedule
"""

#variables

sex = str("")
age = int(0)
gender = str("")
vehiclePrice = int(0)
insuranceAmount = float(0)

def main():
    
    #input

    sex = str(input("Are you 'Male' or 'Female': "))
    age = int(input("Enter your age: "))
    vehiclePrice = int(input("Enter the purchase price of the vehicle: "))

    #process

    if sex.lower() == "male" :
        if age > 14 and age < 25 :
            insuranceAmount = vehiclePrice * 0.25 / 12

        elif age >= 25 and age < 40 :
            insuranceAmount = vehiclePrice * 0.17 / 12

        elif age >= 40 and age < 70 :
            insuranceAmount = vehiclePrice * 0.1 / 12

        else :
            print ("Your age is out of the range")
            insuranceAmount = 0

    elif sex.lower() == "female" :
        if age > 14 and age < 25 :
            insuranceAmount = vehiclePrice * 0.2 / 12

        elif age >= 25 and age < 40 :
            insuranceAmount = vehiclePrice * 0.15 / 12

        elif age >= 40 and age < 70 :
            insuranceAmount = vehiclePrice * 0.1 / 12

        else :
            print ("Your age is out of the range")
            insuranceAmount = 0

    else :
        print("Please enter your correct gender")
        insuranceAmount = 0

    #output

    print("Your monthly insurance will be ${0: .2f}".format(insuranceAmount))


if __name__ == "__main__":
    main()