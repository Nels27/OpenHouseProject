import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


class excelParser(object):

    data = None
    filename = None
    sheetname = None
    names = None
    grades = None
    guests = None

    def init(self):
        data = pd.read_excel(filename,sheetname)
    
    def setFilename(self):
        
    def setNames(self):
        nameDataFrame = pd.DataFrame(data, columns = ['FirstName','LastName'])
        names = nameDataFrame

    def setGuests(self):
        adminNotesDataFrame = pd.DataFrame(data, columns = ['Adm Notes'])
        
        for i = notes in adminNotesDataFrame:
            
    def setGrades(self):
        gradesDataFrame = pd.DataFrame(data, columns = ['Grades'])
        grades = gradesDataFrame

    def setSheetname(self):

    


    def getFilename(self):
        return(self.filename)

    def getNames(self):
        return(names)

    def getGuests(self):
        return(guests)

    def getGrades(self):
        return(grades)

    def getSheetname(self):
        return(sheetname)

if __name__ == "__main__":
    xlParser = excelParser()
    xlParser.init()
    
