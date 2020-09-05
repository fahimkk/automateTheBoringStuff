import PyPDF2

pdf1_file = open('meetingminutes.pdf','rb')
pdf1_read = PyPDF2.PdfFileReader(pdf1_file)
pdf2_file = open('meetingminutes2.pdf','rb')
pdf2_read = PyPDF2.PdfFileReader(pdf2_file)
pdf_writer = PyPDF2.PdfFileWriter()

for pageNum in range(pdf1_read.numPages):
    pdf1_page = pdf1_read.getPage(pageNum)
    pdf_writer.addPage(pdf1_page)

for pageNum in range(pdf2_read.numPages):
    pdf2_page = pdf2_read.getPage(pageNum)
    pdf_writer.addPage(pdf2_page)

pdf_output_file = open('combinedminutes.pdf','wb')
pdf_writer.write(pdf_output_file)
pdf_output_file.close()
pdf1_file.close()
pdf2_file.close()

f = open('combinedminutes.pdf','rb')
fr = PyPDF2.PdfFileReader(f)
print(fr.numPages)
