import PyPDF2
import pypdfium2

pdf_reader = pypdfium2.PdfDocument('F:\\python\\test2.pdf')
page = pdf_reader.get_page(0).get_textpage().get_text_range()
page = page.encode("utf-8", errors="ignore").decode("utf-8")
print(len(pdf_reader))
print(page[0])
print(page[0].encode('utf-8'))
print('实'.encode('utf-8'))