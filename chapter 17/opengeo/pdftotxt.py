import pymupdf

doc = pymupdf.open("suc.pdf") # open a document
out = open("outputold.txt", "wb") # create a text output

for page in doc: # iterate the document pages
    text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
    out.write(text) # write text of page
    out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
out.close()