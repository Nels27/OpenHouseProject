import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

filename = 'TourandOpenHouseAdmissionsReporting.xlsx'
sheetname = 'Tour and Open House Admissions '

data = pd.read_excel(filename,sheetname)

#print("Column headings:")
#print(df.columns)  #Access column names using .columns method


#Storing the relevant info for the parent to be ported over.


#Storing the names of the parents.
firstNamesData = data['FirstName']
lastNamesData = data['LastName']

nameDataFrame = pd.DataFrame(data, columns = ['FirstName','LastName'])

#Storing the grades of the students they are bringing
gradesDataFrame = pd.DataFrame(data, columns = ['Grades'])

#Storing the tour times of the people attending 
tourTimesDataFrame = pd.DataFrame(data, columns = ['TourTimes'])
#TourTimes = data['TourTimes']  # per the formatting these contain 
                             # the phone numbers of the parents.

#Storing the Source of where they found us
SourceAdDataFrame = pd.DataFrame(data, columns = ['Source'])

#Storing the Admin Notes on the Sheet

#Figure out how to pull the number of guests from a string.
adminNotesDataFrame = pd.DataFrame(data, columns = ['Adm Notes'])
guestCnt = 0
for i in (0,length(adminNotesDataFrame)):
    if  'guests' in adminNotesDataFrame:
        guestCnt +=
        
print('Here are the number of guests')
print(guestCnt)
        

#Admin notes contain the guest estimate number 
#Will have to check for the number of guests or if they even have guests
#parsing by checking for if it contains the word 'guests'

#print('Names of parents')
#print(nameDataFrame)

#print('Here are the grades of the kids attending')
#print(gradesDataFrame)

#print('Here are the phone numbers of the parents')
#print(tourTimesDataFrame)

#print('Here is how they found us')
#print(SourceAdDataFrame)
