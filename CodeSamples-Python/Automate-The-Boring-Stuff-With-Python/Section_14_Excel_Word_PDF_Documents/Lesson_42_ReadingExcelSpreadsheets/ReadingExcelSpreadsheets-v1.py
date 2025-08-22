# The OpenPyXL third-party module handles Excel spreadsheets (.xlsx files).
# openpyxl.load_workbook(filename) returns a Workbook object.
# get_sheet_names() and get_sheet_by_name() help get Worksheet objects.
# The square brackets in sheet[‘A1'] get Cell objects.
# Cell objects have a "value" member variable with the content of that cell.
# The cell() method also returns a Cell object from a sheet.

# Import relevant modules
import openpyxl, os

# Update Working Directory to Local Lesson Folder where the example.xlsx file resides
os.chdir('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_14_Excel_Word_PDF_Documents\\Lesson_42_ReadingExcelSpreadsheets')

# Verify the Current Working Directory
filePath = os.getcwd()

# Print DEBUG
print(filePath)

# Create a Workbook Object by passing the File Name IF in the Current Working Directory
workbook = openpyxl.load_workbook('example.xlsx')

# Create a Sheet Object (New Syntax)
sheet = workbook['Sheet1']

# Obtain Workbook Sheet Names (New Syntax)
workbookSheetNames = workbook.sheetnames()
# workbook.sheetnames()

# Print DEBUG
print(str(workbookSheetNames))
# print(workbook.sheetnames())
 