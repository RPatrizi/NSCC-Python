"""
Student Name: Rodrigo Borges    
Program Title: Weekly Loan Calculator
Description: Develop a short term loan calculator program as a console application with the following specifications. 
Begin by designing your solution to this problem in pseudocode, which will be submitted along with the program
"""

def main():
    
    print("Weekly Loan Calculator")
    print("")

    #input

    loanAmount = float(input("Enter the Amount of Loan: "))
    interestRate = float(input("Enter the Interest Rate (%): "))
    NumberOfYears = int(input("Enter the number of Years: "))
    
    #process

    iValue = float(interestRate / 5200)
    weeklyPayment = float((iValue / (1 - (1 + iValue) ** (-52 * NumberOfYears))) * loanAmount)

    #output

    print("")
    print("Your weekly payment will be: ${0: .2f}" .format(weeklyPayment))
    
if __name__ == "__main__":
    main()