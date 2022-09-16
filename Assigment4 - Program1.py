"""
Student Name: Rodrigo Borges (W0420797)
Program Title: Assignment 4, Program 1, Time Sheet
Description: Design and write a program that accepts the number of hours worked on each of five work days from the user,
then displays different information calculated about those entries as output. 
"""


def workInformation():

    #variables

    workDays = ["Day #1", "Day #2", "Day #3", "Day #4", "Day #5"]
    workHours = [0, 0, 0, 0, 0]
    maxHour = 0
    maxHours = []
    maxDays = []
    sumHour = 0
    averageHour = 0
    insufDays = []
    insufHours = []

    #input and process
    # For loop created to ask user to input number of hours worked in each day (workHours list)
    for i in range (len(workDays)) :
        workHours[i] = int(input("Please enter hours worked on Day #{0}: ".format(i + 1)))
        # sumHour variable to calculate the total number of hours worked
        sumHour = sumHour + workHours[i]
        # if statement to look for more than one day with maximum hours of work
        if workHours[i] == maxHour :
            maxDays.append(workDays[i])
            maxHours.append(workHours[i])
        # if statement to update, if needed, the highest number of work hours (maxHour variable)
        # Also, if statement delete the lists containing the old maximum number of Work hour (maxHours list) and Work day (maxDays list)
        # and create a new one to update the list and keep just the highest value
        if workHours[i] > maxHour :
            maxHour = workHours[i]
            del maxDays
            del maxHours
            maxDays = []
            maxHours = []
            maxDays.append(workDays[i])
            maxHours.append(workHours[i])
        # if statement to check and update (insufDays and insufHours list) if any day of work has less than 7h of work
        if workHours[i] < 7 :
            insufDays.append(workDays[i]) 
            insufHours.append(workHours[i])
    # calculate the average hours (averageHour variable) considering the work hour inputed
    averageHour = sumHour / len(workHours)

    #output

    print("---------------------------------------------------------")
    print("The most hours worked was on:")
    for y in range(len(maxDays)) :
        print("{0} when you worked {1} hours.".format(maxDays[y], maxHours[y]))
    print("---------------------------------------------------------")
    print("The total number of hours worked was: {0}".format(sumHour))
    print("The average number of hours worked each day was: {0}".format(averageHour))
    print("---------------------------------------------------------")
    print("Days you slacked off (i.e. worked less than 7 hours):")
    for x in range(len(insufDays)) :
        print("{0}: {1} hours".format(insufDays[x], insufHours[x]))

workInformation()