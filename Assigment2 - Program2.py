"""
Student Name: Rodrigo Borges (W0420797)
Program Title: Erewhon Mobile Data Plans
Description: Calculate cost based on range's cost
"""

#variables
dataUsage = float(0)
totalCharge = float(0)

def main():
    
    #input

    dataUsage = float(input("Enter Data Usage (Mb): "))

    #process

    if dataUsage <= 200 :
        totalCharge = 20

    elif dataUsage > 200 and dataUsage <= 500 :
        totalCharge = dataUsage * 0.105

    elif dataUsage > 500 and dataUsage <= 1000 :
        totalCharge = dataUsage * 0.110

    else :
        print("Data Usage out of range, please try again")
        totalCharge = 0

    #output

    print("Total charge is ${0: .2f}".format(totalCharge))


if __name__ == "__main__":
    main()