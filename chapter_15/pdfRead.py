import PyPDF2

pdfFileObj = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.isEncrypted)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(1)
print(pageObj.extractText())
