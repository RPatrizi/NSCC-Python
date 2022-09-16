"""
Student Name: Rodrigo Borges (W0420797)
Program Title: Landscape Calculator
Description: Computes the price of landscaping for a new housing development
Work orders are based on: address, plot length and width in feet, type of grass (“fescue”, “bentgrass” or “campus”), and number of trees
"""

#Variables

houseNumber = str("Not Informed")
length = float(0)
width = float(0)
grassType = str("Not Informed")
numberOfTree = int(0)
surface = float(0)
totalCost = float(0)


def main():
    
    #input

    houseNumber = str(input("Enter House Number: "))
    length = float(input("Enter property depth (feet): "))
    width = float(input("Enter property width (feet): "))
    grassType = str(input("Enter type of grass (fescue, bentgrass or campus): "))
    numberOfTree = int(input("Enter number of trees: "))
    
    #process

    surface = length * width

    if grassType.lower() == "fescue" :
        totalCost = 1000 + (surface * 0.05)

    elif grassType.lower() == "bentgrass" :
        totalCost = 1000 + (surface * 0.02)

    elif grassType.lower() == "campus" :
        totalCost = 1000 + (surface * 0.01)

    else :
        print("No grass type informed! ")
    
    if surface > 5000 :
        totalCost = totalCost + 500

    if numberOfTree > 0 :
        totalCost = totalCost + (numberOfTree * 100)

    #output

    print("Total cost for house", houseNumber, "is ${0: .2f}".format(totalCost))


if __name__ == "__main__":
    main()