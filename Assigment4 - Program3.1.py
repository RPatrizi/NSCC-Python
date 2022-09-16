"""
Student Name: Rodrigo Borges (W0420797)
Program Title: Assignment 4, Program 3, Student's Mark
Description: Design and write a program that accepts the students marks and their names in Python and data base course. 
"""


def stCourse(num):

    #variables
    pyTotalMark = int(0)
    dbTotalMark = int(0)
    pyAvgMark = float(0)
    dbAvgMark = float(0)
    fail = float(60)
    addMark = float(5)
    
    #lists
    stNames = []
    pyMarks = []
    dbMarks = []
    dbLessAvgMark = []
    dbLessAvgName = []
    

    print("Enter students names and marks for the {0} students".format(num))
        
    for x in range(num) : # for loop to ask user to inform name and marks of each student and calculate total mark of each couse
        stNames.append(input("Enter student's name # {0}\t: ".format(x+1)))
        pyMarks.append(int(input("Enter {0}'s mark in Python\t: ".format(stNames[x]))))
        if pyMarks[x] < 0 or pyMarks[x] > 100:
            print("Mark out of the range, restart!")
            return
        pyTotalMark = pyTotalMark + pyMarks[x]
        dbMarks.append(int(input("Enter {0}'s mark in DB\t: ".format(stNames[x]))))
        if dbMarks[x] < 0 or dbMarks[x] > 100 :
            print("Mark out of the range, restart!")
            return
        dbTotalMark = dbTotalMark + dbMarks[x]

    pyAvgMark = float(pyTotalMark / len(pyMarks))
    dbAvgMark = float(dbTotalMark / len(dbMarks))

    print("----------------------------------------------------------")
    print("StName     \tPython Course \tData Base Course")
    print("---------- \t------------- \t----------------")

    for y in range (len(stNames)) :
        print("{0} \t{1: .1f} \t\t{2: .1f}".format(stNames[y], pyMarks[y], dbMarks[y]))

    print("----------------------------------------------------------")
    print("The total mark of python couse is :{0: .1f}, and Data Base couse is :{1: .1f}".format(pyTotalMark, dbTotalMark))
    print("The average mark of python course is :{0: .2f}, and Data Base course is :{1: .2f}".format(pyAvgMark, dbAvgMark))
    print("---------------------The First Report---------------------")
    print("Students' Marks less than average in DB course")

    for z in range (len(dbMarks)) :
        if dbMarks[z] < dbAvgMark :
            dbLessAvgName.append(stNames[z])
            dbLessAvgMark.append(dbMarks[z])

    for n in range (len(dbLessAvgName)) :
        print("{0} got\t{1: .1f} for Data Base Course".format(dbLessAvgName[n], dbLessAvgMark[n]))

    print("---------------------The Second Report--------------------")
    print("Students' who were suported in Python course")

    for w in range (len(pyMarks)) :
        if pyMarks[w] < fail :
            print("{0} got\t{1: .1f} in Python course".format(stNames[w], pyMarks[w] + addMark))

    print("---------------------The EXTRA Report---------------------")
    print("Students' who fail in DB course (Mark below 60)")

    for k in range (len(dbMarks)) :
        if dbMarks[k] < fail :
            print("{0} got\t{1: .1f} in Python course".format(stNames[k], dbMarks[k]))

    print("---------------------The Third Report---------------------")
    print("Students' names before sorted in ascending order")
    print(stNames)
    print("Students' names after sorted in ascending order")
    stNames.sort()
    print(stNames)
    print("")

    return

# ask user to inform num of students and call function
st = int(input("\nHow many number of students: "))
stCourse(st)