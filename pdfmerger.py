import PyPDF2

merger = PyPDF2.PdfMerger()

pdfiles = ["1d.pdf", "2d.pdf", "3d.pdf"]

for x in pdfiles:
    pdfile = open(x, "rb")
    pdfreader = PyPDF2.PdfReader(pdfile)
    merger.append(pdfreader)

pdfile.close()
merger.write("Dunki.pdf")    