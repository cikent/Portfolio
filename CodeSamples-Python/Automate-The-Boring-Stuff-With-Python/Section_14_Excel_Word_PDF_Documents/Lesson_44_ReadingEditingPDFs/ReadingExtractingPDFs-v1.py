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

# Create a PDF File Object
pdfFile = open('meetingminutes1.pdf', 'rb')                   # 1st argument can be a Relative Path IF the CWD is accurate, otherwise, provide Absolute File Path; 2nd argument is for Mode, to indicate how the document should be interacted with; wb == read binary

# Create a variable to store the PDF File
reader = PyPDF2.PdfReader(pdfFile)              # Use new syntax, PdfFileReader() is deprecated

# Verify the # of Pages in the PDF Document
print(len(reader.pages))                        # Use new syntax, numPages is deprecated

# Read the contents from Page 1 (index 0) from the PDF
page0 = reader.pages[0]                         # Use new syntax, getPage() is deprecated

# Create a Variable to store the extracted the Text from Page 1 (index 0) from the PDF
page0Text = page0.extract_text                             # Use new syntax, extractText() is deprecated

# DEBUG Print the Current Working Directories File Path
print(page0Text)

# Loop over Page Object pages to extract PDF contents
for pageNum in range(len(reader.pages)):
    print(reader.pages[pageNum].extract_text)