import PyPDF2

minutes_read = PyPDF2.PdfFileReader(open('meetingminutes.pdf','rb'))
water_read = PyPDF2.PdfFileReader(open('watermark.pdf','rb'))
water_page = water_read.getPage(0)


pdf_writer = PyPDF2.PdfFileWriter()

for pageNum in range(minutes_read.numPages):
    minutes_page = minutes_read.getPage(pageNum)
    minutes_page.mergePage(water_page)
    pdf_writer.addPage(minutes_page)

output_file = open('watermarkedMinute.pdf','wb')
pdf_writer.write(output_file)
output_file.close()

