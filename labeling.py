import os
from PIL import Image
import pandas as pd
import xlsxwriter

listing = os.listdir("Desktop/text_detection/SNIPS/IMG/")

len(listing)


#new_directory = "Desktop/resultestcopy/folder4000/"

def move_file(old_file_path, new_directory):
    if not os.path.isdir(new_directory):
        os.mkdir(new_directory)
    base_name = os.path.basename(old_file_path)
    new_file_path = os.path.join(new_directory, base_name)
    os.rename(old_file_path, new_file_path)

workbook = xlsxwriter.Workbook('Desktop/sample.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'Image')
worksheet.write('B1', 'NAME')
worksheet.write('C1', 'LABEL')
k=1
for k in range(len(listing)):
    worksheet.set_row(k,80)

j=2 
for i in listing:
    if i.endswith(".jpg"):
        #move_file("Desktop/resultestcopy/subreg/"+i,new_directory)
        worksheet.insert_image('A'+str(j), "Desktop/text_detection/SNIPS/IMG/"+i, {'x_scale': 0.4, 'y_scale': 0.4})
        worksheet.write('B'+str(j), i)
        j=j+1 
        if j>1100:
            break
workbook.close()
