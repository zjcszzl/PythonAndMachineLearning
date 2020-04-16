import PyPDF2 as pdf

with open("Assignment4EML.pdf", "rb") as file:
    reader = pdf.PdfFileReader(file)
    print(reader.numPages)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = pdf.PdfFileWriter()
    writer.addPage(page)
    with open("rotated.pdf", "wb") as output:
        writer.write(output)
    # writer.insertPage(page)
    # weiter.insertBlankPage()

    merger = pdf.
