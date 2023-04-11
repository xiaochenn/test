import docx
def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return ''.join(fullText)

filename = 'F:\\python\\test.docx'
print(getText(filename))
r'tes.*'