from pathlib import Path
from PyPDF2 import PdfMerger
import os
from PIL import Image
import shutil

# Create a merger file where all pdfs will be appended
merger = PdfMerger()

source = r'C:\Users\Dev Patel\Desktop\PDF Merger'  # Add all file which needs to be merged
converted_PDF = r'C:\Users\Dev Patel\Desktop\JPG to PDF'  # JPG to be converted to pdf
list_of_files = os.listdir(source)  # Saves all files in this variable

for dirs, subdirs, files in os.walk(source):
    for file in files:
        if file.endswith(".pdf"):
            print("PDF moved: " + file)
            filename = os.path.join(source, dirs, file)
            shutil.copy(filename, converted_PDF)

for file in list_of_files:  # iterate through each file
    print(file)  # print file name
    if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):  # If file extension is .jpg or .png
        image = Image.open(os.path.join(source, file))  # Opening a jpg or png file
        image_converted = image.convert('RGB')  # Converting jpg to pdf
        image_converted.save(
            os.path.join(converted_PDF, '{0}.pdf'.format(file.split('.')[-2])))  # Saving Pdf to converted_PDF
#
# list_of_pdf = os.listdir(converted_PDF)  # Storing all PDF to a variable
# for file in list_of_pdf:  # Iterating through each PDF
#     merger.append(converted_PDF + '\\' + file)  # Appending Each PDF
# merger.write("merged.pdf")  # Naming the new merger pdf
# merger.close()  # Closing Merged PDF
