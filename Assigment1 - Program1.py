"""
Student Name: Rodrigo Borges    
Program Title:  Hipster's Local Vinyl Record
Description: Write a program that calculates Delivery Cost, Purchase Cost and Total Cost for each customer purchase.
"""

def main():
    
    print("Hipster's Local Vinyl Records - Customer Order Details")
    print("")

    #input

    customerName = str(input("Enter the customer's name: "))
    distance = float(input("Enter the distance in kilometers for delivery: "))
    costOfRecords = float(input("Enter the cost of records purchased: "))
    
    #process

    costOfDelivery = float(distance * 15)
    costAfterTax = float(costOfRecords * 1.14)
    totalCost = float(costOfDelivery + costAfterTax)

    #output

    print("")
    print("Purchase sumary for", customerName)
    print("Delivery Cost: ${0: .2f}" .format(costOfDelivery))
    print("Purchase Cost: ${0: .2f}" .format(costAfterTax))
    print("Total Cost   : ${0: .2f}" .format(totalCost))

if __name__ == "__main__":
    main()