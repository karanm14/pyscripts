import os
from PIL import Image
import pandas as pd
import xlsxwriter



##################
#WE HAVE TWO CSV FILES 1) WITH LABELS 2)WITH INDEX 

df1 = pd.read_csv("Desktop/Book3.csv") #INDEX OF SUBREGIONS WITH 1


##################

df2 = pd.read_excel("Desktop/imageskaist1.xlsx") #FILES WITH LABELS 



##################
x=[]
for i in range(0,len(df1)):
    x.append(df1["index"][i]-1)

    
    
##################
z=[]
for i in x:
    z.append(df2['Label'][i])

    
    

##################    
#NOW we will read the boxes of all predictions which are 1 and store them with label 

h=[]
for i in range(0,len(df1)):
    df4 = pd.read_csv("Desktop/text_detection/kaist/KAISTsubregions/"+z[i][0:-4]+".csv",header=None)
    h.append([z[i],float(df4[0]),float(df4[1]),float(df4[2]),float(df4[3])])


##################
#to check if its working correctly
print(h[1][0],h[1][1],h[1][2],h[1][3],h[1][4])



##################
workbook = xlsxwriter.Workbook('Desktop/kaist72withboxtrainbai.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'BaseImage')
worksheet.write('B1', 'Label')
worksheet.write('C1', 'x')
worksheet.write('D1', 'y')
worksheet.write('E1', 'w')
worksheet.write('F1', 'h')

j=2 
for i in range(0,150):
        worksheet.write('A'+str(j), h[i][0].split('_')[0])
        worksheet.write('B'+str(j), h[i][0])
        worksheet.write('C'+str(j), h[i][1])
        worksheet.write('D'+str(j), h[i][2])
        worksheet.write('E'+str(j), h[i][3])
        worksheet.write('F'+str(j), h[i][4])
        j=j+1 
workbook.close()
