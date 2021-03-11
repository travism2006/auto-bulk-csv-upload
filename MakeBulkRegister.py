"""
    Makes a CSV for bulk uploading and registering recipients to
    take in the Healthcare Provider (HCP) Portal.
"""




#       Sample Row Data for Recipients
#
#Travis103,Mit,tmitchumEY+i23@gmail.com
#Travis104,Mit,tmitchumEY+i24@gmail.com
#Travis105,Mit,tmitchumEY+i25@gmail.com

import csv
import fnmatch
import os,sys
from datetime import datetime

#personalized constants
import FileConstants as fc
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

CWD = os.getcwd()
NOW = str(datetime.now())
LOG_FILE = "\\InputLog.txt"

# REGION START Functions--------------------------------------------------
def startLog():
    with open(CWD+LOG_FILE,'a') as logF:
        logF.write("-"*len(NOW)+"\n")
        logF.write(NOW + "\n")
        logF.write("-"*len(NOW)+"\n")
# How to Log:
def logInput(dataKW:dict):
    if dataKW==None:return
    if len(list(dataKW))==0:return
    with open(CWD+LOG_FILE,'a') as logF:
        logF.write('File Name: ' + dataKW['fileX']+"\n")
        logF.write('Person For: ' + dataKW['pf']+"\n")
        logF.write('Portal: ' + dataKW['p']+"\n")
        logF.write('Email+: ' + dataKW['seq']+"\n")
        logF.write('Limit: ' + str(dataKW['L'])+"\n")
        logF.write('Rows: ' + str(dataKW['rows'])+"\n")
        

# End log with spacing
def endLog():
    with open(CWD+LOG_FILE,'a') as logF:
        logF.write("\n")

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
startLog()
emailChar = input('email char seq: ')
firstName = input("First Name: ")
lastName = input("Last Name: ")
testEmail = input("Test email: ")
dob = input("DOB(MM/DD/YYYY): ")

# check what was last written
lastWroteList = readDataFile()

fileUpdateValue = int(lastWroteList[0])
firstNameUpdateValue = int(lastWroteList[1])
emailUpdateValue = int(lastWroteList[2])

csvFileName = fc.FILE_BASE_NAME + str(fileUpdateValue) + '.csv'
rows = []
with open(csvFileName, 'w', newline='') as csvfile:
    # creating a csv writer object 
    csvWriter = csv.writer(csvfile)


    #write header string
    csvWriter.writerow(fc.HEADER)


    #get Amt. of new recipients to register
    amtOfRows = input("Amt. of new recipients: ")
    
    for i in range(int(amtOfRows)):
        
        #build field values
        firstNameField = firstName + str(firstNameUpdateValue)
        lastNameField = lastName + str(firstNameUpdateValue)
        emailField = testEmail + "+" + emailChar + str(emailUpdateValue) + "@gmail.com"

        #wrap fields in row and write data to csv
        row = [firstNameField, lastNameField, dob, emailField]
        csvWriter.writerow(row)
        rows.append(row)
        
        #update row values here
        emailUpdateValue += 1
        firstNameUpdateValue += 1

    
    fileUpdateValue += 1
    updateDataFile(fileUpdateValue, firstNameUpdateValue, emailUpdateValue)
dataKW = {}

#logInput(dataKW)
print(str(datetime.now()))
endLog()
with open('log history generated.txt', 'a', newline='') as tfile:
    for r in rows:
        line=f"{r[0]},{r[1]},{r[2]}\n"
        tfile.write(line)
