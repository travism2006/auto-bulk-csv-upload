"""
    Makes a CSV for bulk uploading and registering recipients to
    take in the HCP and Employer Portals.


       Sample Row Data for Recipients
                                       
Travis103,Mit,tmitchumEY+i23@gmail.com
Travis104,Mit,tmitchumEY+i24@gmail.com
Travis105,Mit,tmitchumEY+i25@gmail.com
"""

import csv
import fnmatch
import os

#personalized constants
import FileConstants

# REGION START Functions--------------------------------------------------
# Updates max values
def updateDataFile(fileUpdateValue, firstNameUpdateValue, emailUpdateValue):
    with open("data last wrote.csv", 'w', newline='') as dataFile:
        dataWriter = csv.writer(dataFile)
        
        dataHeader = ["","Last Wrote"]
        dataWriter.writerow(dataHeader)
        
        dataWriter.writerow(["Last File Value", fileUpdateValue-1])
        dataWriter.writerow(["Last First Name Value", firstNameUpdateValue])
        dataWriter.writerow(["Last Email Value", emailUpdateValue])
        dataWriter.writerow(["Last Char Value", emailUpdateValue])

# Reads max values
def readDataFile():
    with open("data last wrote.csv", 'r') as dataFile:
        dataReader = csv.reader(dataFile, delimiter=',')

        toUnpackList = []

        for row in dataReader:
            if "Last" in row[0]: toUnpackList.append(row[1])
    return toUnpackList
# REGION ENDS-------------------------------------------------------------


emailCharList = ['q']

# handling y/n input
validMap = {'y':True, 'Y':True, 'yes': True, 'Yes': True,
        'n':False, 'N':False, 'no':False, 'No':False}
askReset = input("Add a new char to email (y/n): ")
shouldReset = [val for k,val in validMap.items() if askReset==k]
willReset = shouldReset[0]


firstName = input("First Name: ")
lastName = input("Last Name: ")

lastWroteList = readDataFile()

fileUpdateValue = int(lastWroteList[0])
firstNameUpdateValue = int(lastWroteList[1])
emailUpdateValue = int(lastWroteList[2])

# if you said 'Y' to reset then values will go back to 1 and future emails will still be unique
if willReset:
    emailCharList.append(emailCharList[0])
    print(firstNameUpdateValue, ' is now reset to 1')
##    print(emailUpdateValue, ' is now reset to 1')
    firstNameUpdateValue = 1
    emailUpdateValue = 1



with open("BULK upload this.csv", 'w', newline='') as csvfile:
    csvWriter = csv.writer(csvfile)
    csvWriter.writerow(FileConstants.HEADER)


    #get Amt. of new recipients to register
    amtOfRows = input("Amt. of new recipients: ")
    
    for i in range(int(amtOfRows)):
        firstNameField = firstName + str(firstNameUpdateValue)
        lastNameField = lastName + str(firstNameUpdateValue)
        emailCharSeq = "".join(emailCharList)
        emailField = FileConstants.BASE_GMAIL + "+" + emailCharSeq + str(emailUpdateValue) + "@gmail.com"

        #wrap fields in row and write data to csv
        row = [firstNameField, lastNameField, emailField]
        csvWriter.writerow(row)

        #update row values here
        emailUpdateValue += 1
        firstNameUpdateValue += 1

    fileUpdateValue += 1
    updateDataFile(fileUpdateValue, firstNameUpdateValue, emailUpdateValue)
    
