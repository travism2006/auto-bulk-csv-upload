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
def updateDataFile(rows):
    with open("Track bulk limit test.csv", 'w', newline='') as dataFile:
        dataWriter = csv.writer(dataFile)
        
        dataHeader = ["","Last Wrote"]
        dataWriter.writerow(dataHeader)
        dataWriter.writerows(rows)
##        dataWriter.writerow(["File wrote to", fileName])
##        dataWriter.writerow(["File limit", limitValue])
##        dataWriter.writerow(["File last First Name Value", firstNameUpdateValue])
##        dataWriter.writerow(["File last Email Value", emailUpdateValue])
##        dataWriter.writerow(["", ''])
##        dataWriter.writerow(["", ''])
##        dataWriter.writerow(["Last Char Value", charUpdateValue])

def portalQs():
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    preGmail = input("Your Gmail account: ")
    personFor = input("Who is this for: ")
    portalName = input("Portal name: ")
    
    dataDict = {'fn':firstName,'ln':lastName,'pg':preGmail,'pf':personFor,'pn':portalName}
    return dataDict

# Reads max values
def readDataFile():
    with open("Track bulk limit test.csv", 'r') as dataFile:
        dataReader = csv.reader(dataFile, delimiter=',')

        toUnpackList = []
        for row in dataReader:
            if "File" in row[0]: toUnpackList.append(row[1])
    return toUnpackList
# REGION ENDS-------------------------------------------------------------

testLimit = int(input("Upload limit: "))
testPair = (testLimit, testLimit+1)


toUnpack = portalQs()
lastWroteList = readDataFile()


#fileUpdateValue = int(lastWroteList[0])
firstNameUpdateValue = 1
emailUpdateValue = 1
emailCharStr = 'r4r'
emailCharList = [c for c in emailCharStr]

updateRows = []


for val in testPair:
    fileName = "Bulk Upload Limit Test " + toUnpack['pn'] +' '+ str(val) +' '+ toUnpack['pf'] + '.csv'
    updateRows.append(["File wrote to", fileName])
    updateRows.append(["File test value", val])
    
    with open(fileName, 'w', newline='') as csvfile:
        csvWriter = csv.writer(csvfile)
        csvWriter.writerow(FileConstants.HEADER)


        #get Amt. of new recipients to register
    
        for i in range(val):
            firstNameField = toUnpack['fn'] + str(firstNameUpdateValue)
            lastNameField = toUnpack['ln'] + str(firstNameUpdateValue)
            emailCharSeq = "".join(emailCharList)
            emailField = toUnpack['pg'] + "+" + emailCharSeq + str(emailUpdateValue) + "@gmail.com"

            row = [firstNameField, lastNameField, emailField]
            
            csvWriter.writerow(row)

            #update row values here
            emailUpdateValue += 1
            firstNameUpdateValue += 1
            charUpdateValue = emailCharSeq

        #fileUpdateValue += 1
updateDataFile(updateRows)
