import PyPDF2

pdf1_file = open('meetingminutes.pdf','rb')
pdf1_read = PyPDF2.PdfFileReader(pdf1_file)
pdf2_file = open('meetingminutes2.pdf','rb')
pdf2_read = PyPDF2.PdfFileReader(pdf2_file)

pdf1_page1 = pdf1_read.getPage(0)
pdf2_page1 = pdf2_read.getPage(0)

pdf_writer = PyPDF2.PdfFileWriter()

pdf_writer.addPage(pdf1_page1)
pdf_writer.addPage(pdf2_page1)

pdf_ouput = open('mypdf.pdf','wb')
pdf_writer.write(pdf_ouput)

pdf1_file.close()
pdf_ouput.close()