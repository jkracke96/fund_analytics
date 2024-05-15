import PyPDF2

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

file = open("data/Depotauszug.pdf", "rb")

pdf_reader = PyPDF2.PdfReader(file)

pages = pdf_reader.pages

stk = []
for page in pages:
    text = page.extract_text()
    split_text = text.split(("Stk."))
    for j in split_text:
        n1 = j.rfind("\n", 0, j.rfind("\n"))
        n2 = j.rfind("\n")
        stk.append(j[n1+1:n2-1])

print(stk)

i = 0
while i < len(stk):
    elem = stk[i]
    if is_float(elem):
        i += 1
    else:
        stk.remove(elem)



print(stk)
file.close()
