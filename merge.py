import PyPDF2
import os
import sys, getopt
import glob
from PIL import Image

dirname = "./raw/"
split = "./split/"
script_dir = os.path.dirname(os.path.abspath(__file__))


if sys.argv[1] == "merge":
    pdfMerger = PyPDF2.PdfFileMerger()
    names = []
    imgs = []
    for fname in os.listdir(dirname):
        print("open: "+ fname)
        if not (fname.endswith(".jpg") or fname.endswith(".png") or fname.endswith(".JPG") or fname.endswith(".jpeg")):
            print("file not merged: "+ fname)
            continue
        path = os.path.join(dirname,fname)
        if os.path.isdir(path):
            continue
        img= Image.open(os.path.join(script_dir, path))
        img = img.convert('RGB')
        imgs.append(img)
        names.append(fname[0:-4]+ ".pdf"+"\n")
    imgs[0].save(os.path.join(script_dir,"merged.pdf"),save_all=True,append_images=imgs[1:]) 
   			
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
