import pdfrw
import pypdfium2
from math import ceil

pypdfium2.logger
def get_pdf_pages(path):
    pdf = pdfrw.PdfReader(path)
    return len(pdf.pages)

            
def make1with4(p2,m1,m2):
    if p2[1]:
        m4 = pdfrw.PageMerge() + p2[0] + m1 + p2[1] + m2
    else:
        m4 = pdfrw.PageMerge() + p2[0] + m1
    for i,page in enumerate(m4):
        page.scale(1/2)
        page.x = page.w if i & 1 else 0
        page.y = 0 if i & 2 else page.h
    return m4.render()

# def watermaker(path,watermark,output):
#     pdf = pdfrw.PdfReader(path)
#     watermark = pdfrw.PdfReader(watermark)
#     for page in pdf.pages:
#         pdfrw.PageMerge(page).add(watermark.pages[0]).render()
#     writer = pdfrw.PdfWriter()
#     writer.write(output,pdf)
s
def pdf4in1(input,output):
    pdf = pdfrw.PdfReader(input)
    m1 = pdfrw.PdfReader('model1.pdf')
    m2 = pdfrw.PdfReader('model2.pdf')
    pages = [make1with4(pdf.pages[i:i+2],m1.pages[0],m2.pages[0]) for i in range(0,len(pdf.pages),2)]
    writer = pdfrw.PdfWriter()
    for page in pages:
        writer.addpage(page)
    writer.write(output)

def concatenate(paths,output):              #合并pdf
    writer = pdfrw.PdfWriter()
    for path in paths:
        reader = pdfrw.PdfReader(path)
        writer.addpages(reader.pages)
    
    writer.write(output)

if __name__ == '__main__':
    path = 'CH04.pdf'
    front_pages_num = get_pdf_pages(path)
    after_pages_num = ceil(front_pages_num / 4)
    pdf4in1('CH04.pdf','CH04_4in1.pdf')