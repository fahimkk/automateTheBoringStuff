import PyPDF2, os, logging

logging.basicConfig(level=logging.DEBUG, filename='logfile.log', filemode='w')
logging.disable(logging.INFO)

pdf_files = []
for files in os.listdir():
    if files.endswith('.pdf'):
        pdf_files.append(files)
pdf_files.sort()

logging.debug(pdf_files)

pdf_writer = PyPDF2.PdfFileWriter()

logging.debug(pdf_files[0])
page1_read = PyPDF2.PdfFileReader(open((pdf_files[0]),'rb'))
logging.debug(pdf_files[0])
pdf_writer.addPage(page1_read.getPage(0))

for pdfFile in pdf_files:
    pdf_read = PyPDF2.PdfFileReader(open(pdfFile,'rb'))
    logging.warning(pdf_read)
    if not pdf_read.isEncrypted:
        logging.warning(pdf_read)
        logging.error(pdf_read.numPages)
        for pageNum in range(1,pdf_read.numPages):
            pdf_writer.addPage(pdf_read.getPage(pageNum))

result_pdf = open('allminutes.pdf','wb')
pdf_writer.write(result_pdf)
result_pdf.close()



