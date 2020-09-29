import PyPDF2
import os
import sys, getopt
import glob
from PIL import Image
import img2pdf

dirname = "./raw/"
split = "./split/"

if sys.argv[1] == "merge":
    pdfMerger = PyPDF2.PdfFileMerger()
    names = []
    with open("merged.pdf", "wb") as f:
        imgs = []
        for fname in os.listdir(dirname):
            if not (fname.endswith(".jpg") or fname.endswith(".png")):
                continue
            path = os.path.join(dirname,fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
            names.append(fname[0:-4]+ ".pdf"+"\n")
        f.write(img2pdf.convert(imgs))
        '''
    for filename in os.listdir(os.path.join(os.getcwd(), dirname)):
        names.append(filename+ "\n")
        image1 = Image.open(os.path.join(dirname,filename))
        im1 = image1.convert('RGB')
        print(filename)
        pdfMerger.append(im1)
       # pdfMerger.append(open(os.path.join(path,filename), 'rb'))
   '''         
			
    nameFile = open('filenames.txt', 'w')
    nameFile.writelines(names)
    nameFile.close()


if sys.argv[1]=="split":
    inputPDF = PyPDF2.PdfFileReader(open("./merged.pdf", "rb"))
    print("open")
    nameFile = open('./filenames.txt', 'r')
    names = nameFile.readlines()
    for i in range(inputPDF.numPages):
        output = PyPDF2.PdfFileWriter()
        output.addPage(inputPDF.getPage(i))
        print(names[i])
        with open(os.path.join("./split/", names[i].rstrip()), "wb") as outputStream:
            output.write(outputStream)