import PyPDF2

pdf1_file = open('meetingminutes.pdf','rb')
pdf1_read = PyPDF2.PdfFileReader(pdf1_file)

pdf1_page1 = pdf1_read.getPage(0)
pdf1_page1.rotateClockwise(90)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(pdf1_page1)
pdf_output = open('rotatepage.pdf','wb')
pdf_writer.write(pdf_output)

