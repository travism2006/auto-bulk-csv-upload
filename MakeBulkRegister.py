"""
    Makes a CSV for bulk uploading and registering recipients to
    take in the Healthcare Provider (HCP) Portal.
"""




#       Sample Row Data for Recipients
#                                       High/Low, Employee/Individual
#Travis103,Mit,tmitchumEY+i23@gmail.com,High,Employee
#Travis104,Mit,tmitchumEY+i24@gmail.com,High,Employee
#Travis105,Mit,tmitchumEY+i25@gmail.com,High,Employee

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


# Reads max values
def readDataFile():
    with open("data last wrote.csv", 'r') as dataFile:
        dataReader = csv.reader(dataFile, delimiter=',')

        toUnpackList = []

        for row in dataReader:
            if "Last" in row[0]: toUnpackList.append(row[1])
    return toUnpackList

# REGION ENDS-------------------------------------------------------------


emailChar = "r"
firstName = input("First Name: ")



# check what was last written
lastWroteList = readDataFile()

fileUpdateValue = int(lastWroteList[0])
firstNameUpdateValue = int(lastWroteList[1])
emailUpdateValue = int(lastWroteList[2])

csvFileName = FileConstants.FILE_BASE_NAME + str(fileUpdateValue) + '.csv'

with open(csvFileName, 'w', newline='') as csvfile:
    # creating a csv writer object 
    csvWriter = csv.writer(csvfile)


    #write header string
    csvWriter.writerow(FileConstants.HEADER)


    #get Amt. of new recipients to register
    amtOfRows = input("Amt. of new recipients: ")
    
    for i in range(int(amtOfRows)):
        
        #build field values
        firstNameField = firstName + str(firstNameUpdateValue)
        lastNameField = "Monr" + str(firstNameUpdateValue)
        emailField = FileConstants.BASE_GMAIL + "+" + emailChar + str(emailUpdateValue) + "@gmail.com"
        #riskLevelField = "High"
        #personTypeField = "Employee"


        #wrap fields in row and write data to csv
        row = [firstNameField, lastNameField, emailField]
        csvWriter.writerow(row)


        #update row values here
        emailUpdateValue += 1
        firstNameUpdateValue += 1

    
    fileUpdateValue += 1
    updateDataFile(fileUpdateValue, firstNameUpdateValue, emailUpdateValue)
        
    

