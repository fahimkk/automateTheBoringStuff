import PyPDF2

varOpen = open('encrypted.pdf','rb')
varRead = PyPDF2.PdfFileReader(varOpen)
print(varRead.isEncrypted)

varRead.decrypt('rosebud')
varPage = varRead.getPage(0)
print(varRead.numPages)
print(varPage.extractText())