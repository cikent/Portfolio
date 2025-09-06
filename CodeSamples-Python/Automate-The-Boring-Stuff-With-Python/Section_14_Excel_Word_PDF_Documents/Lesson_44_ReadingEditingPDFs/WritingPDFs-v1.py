# The PyPDF2 module can read and write PDFs.
# Opening a PDF is done by calling open() and passing the file object to PdfReader(); PdfFileReader() is deprecated
# A Page object can be obtained from the PDF object with the pages[0] method; getPage() is deprecated
# The text from a Page object is obtained with the extract_text method, which can be imperfect; extractText() is deprecated
# New PDFs can be made from PdfWriter(); PdfFileWriter() is deprecated
# New pages can be appended to a writer object with the add_page(page) method; addPage() is deprecated
# Call the write() method to save its changes.

# Import relevant modules
import PyPDF2, os

# Update Working Directory to Local Lesson Folder where the example.xlsx file resides
os.chdir('C:\\Development\\Python-Projects\\Automate-The-Boring-Stuff-With-Python\\Section_14_Excel_Word_PDF_Documents\\Lesson_44_ReadingEditingPDFs')

# Verify the Current Working Directory
filePath = os.getcwd()

# DEBUG Print the Current Working Directories File Path
print(filePath)

# Create a PDF File Object for each PDF
pdf1File = open('meetingminutes1.pdf', 'rb')                # 1st PDF File Object
pdf2File = open('meetingminutes2.pdf', 'rb')                # 2nd PDF File Object

# Create variables to store the PDF File 1 & 2
reader1 = PyPDF2.PdfReader(pdf1File)                    # Use new syntax, PdfFileReader() is deprecated
reader2 = PyPDF2.PdfReader(pdf2File)                    # Use new syntax, PdfFileReader() is deprecated

# Write the contents of both PDF's to a new file
writer = PyPDF2.PdfWriter()                             # Use new syntax, PdfFileWriter() is deprecated

# Loop over Page Object pages to Read and Write the PDF contents from both files
for pageNum in range(len(reader1.pages)):
    page = reader1.pages[pageNum]
    writer.add_page(page)                               # Use new syntax, addPage() is deprecated
    
for pageNum in range(len(reader2.pages)):
    page = reader2.pages[pageNum]
    writer.add_page(page)                               # Use new syntax, addPage() is deprecated

# Create a new File Object for the combined PDFs
outputFile = open('combinedminutes.pdf', 'wb')                  # 1st argument can be a Relative Path IF the CWD is accurate, otherwise, provide Absolute File Path; 2nd argument is for Mode, to indicate how the document should be interacted with; wb == write binary

# Create a new PDF based upon the File Object
writer.write(outputFile)

# Close relevant Objects
outputFile.close()
pdf1File.close()
pdf2File.close()