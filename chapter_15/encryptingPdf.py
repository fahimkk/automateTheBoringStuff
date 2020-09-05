import PyPDF2

pdf1_file = open('meetingminutes.pdf','rb')
pdf1_read = PyPDF2.PdfFileReader(pdf1_file)

pdf_writer = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1_read.numPages):
    pdf_writer.addPage(pdf1_read.getPage(pageNum))

pdf_writer.encrypt('swordfish')
pdf_output_file = open('encryptedminutes.pdf','wb')
pdf_writer.write(pdf_output_file)
pdf_output_file.close()
pdf1_file.close()
