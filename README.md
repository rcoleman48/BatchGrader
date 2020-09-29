# BatchGrader
This is a short python script to convert and combine .jpg and .png files into a single pdf and then split into their original components as pdfs

# Requirements
The libraries used in this code (can be installed using "pip install") are:
pyPDF2, os, sys, img2pdf

# Usage
the script takes one arguement, either "merge" or "split"

"merge.py merge"
this will take all files with .png and .jpg extensions in the directory "./raw/" convert them to pdfs and merge them into a single pdf file called "merged.pdf" and store the filenames in a txt file "filenames.txt". This can then be annotated/graded in the desired program and saved.

"merge.py split"
This will take "merged.pdf" and "filenames.txt" stored in the same directory as the script and split them page by page with filenames being taken line by line from filenames.txt and all pdfs will be stored in the directory "./split/"
