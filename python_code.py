#Importing libraries
import pytesseract
import pandas as pd
from pytesseract import Output
from PIL import Image, ImageEnhance
import cv2
import os
import numpy as np
import pypdf
from pypdf import PdfReader

pytesseract.pytesseract.tesseract_cmd=("C:\Program Files\Tesseract-OCR\\tesseract.exe")

##Merging the pdf files into one file
pdfs = ["E:\دتامر.pdf","E:\تامر.pdf"]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
## First: converting pages in the scanned PDF file to images then saving the images

# appending the pages of the scanned pdf into a list"page_list"
pdf_reader = pypdf.PdfReader("result.pdf")
page_list=[]
for page in pdf_reader.pages:
    page_list.append(page)

# Saving the images    
counter=0
for i in page_list:
    i.images[0].image.save(f"E:\images\\new_image_{counter}.jpg", format="JPEG")
    counter=counter+1

## Second: Extracting the texts from the images
'''
Main code for extracting text from printout into a dataframe


'''
# function for extract numeric results.
def is_number(x):
    try:
        float(x)
        return x
    except ValueError:
        return x
    
# creating empty lists for appending CBC parameters data        
id_no=[]
date=[]
time=[]
nick_name=[]
platelet=[]
red_cells=[]
white_cells=[]
hemoglobin=[]
hematocrit=[]
m_c_v=[]
m_c_h=[]
m_c_h_c=[]
image=[]

# path of the file with images
for i in os.listdir('E:\images'):
    value=Image.open("E:\images\\"+i)
    
# Enhancing the image    
    contrast_enhancer=ImageEnhance.Contrast(value)
    new_img=contrast_enhancer.enhance(2)
    sharp_enhancer=ImageEnhance.Sharpness(new_img)
    new_img=sharp_enhancer.enhance(2)
    bright_enhancer=ImageEnhance.Brightness(new_img)
    value=bright_enhancer.enhance(2)
    
#extracting the data(CBC contents,date_time, instrument name and image no)    
    text=pytesseract.image_to_string(value)
    sample_no=(text[text.find("Sample No.: ")+len("Sample No.: "):text.find("Sample No.: ")+len("Sample No.: ")+len("24608381")])
    sample_no=is_number(sample_no)
    id_no.append(sample_no)
    d=text[text.find("Position")+len("Position")+3:text.find("Position")+len("Position")+15]
    date.append(d)
    t=text[text.find("Position:")+len("Position:")+13:text.find("Position:")+len("Position:")+23]
    time.append(t)
    name=text[text.find("Nickname: ")+len("Nickname: "):text.find("Nickname: ")+len("Nickname: ")+9]
    nick_name.append(name)
    plt=text[text.find("PLT")+len("PLT"):text.find("PLT")+len("PLT")+4]
    plt=is_number(plt.strip())
    platelet.append(plt)
    rbc=(text[text.find("RBC")+len("RBC"):text.find("RBC")+len("RBC")+6])
    rbc=is_number(rbc.strip())
    red_cells.append(rbc)
    wbc=text[text.find("WBC")+len("WBC"):text.find("WBC")+len("WBC")+6]
    wbc=is_number(wbc.strip())
    white_cells.append(wbc)
    hg=text[text.find("HGB")+len("HGB"):text.find("HGB")+len("HGB")+5]
    hg=is_number(hg.strip())
    hemoglobin.append(hg)
    hct=text[text.find("HCT")+len("HCT"):text.find("HCT")+len("HCT")+5]
    hct=is_number(hct.strip())
    hematocrit.append(hct)
    mcv=text[text.find("MCV")+len("MCV"):text.find("MCV")+len("MCV")+5]
    mcv=is_number(mcv.strip())
    m_c_v.append(mcv)
    mch=text[text.find("MCH")+len("MCH"):text.find("MCH")+len("MCH")+5]
    mch=is_number(mch.strip())
    m_c_h.append(mch)
    mchc=text[text.find("MCHC")+len("MCHC"):text.find("MCHC")+len("MCHC")+5]
    mchc=is_number(mchc.strip())
    m_c_h_c.append(mchc)
    image.append(i)
# Creating the dataframe    
df=pd.DataFrame()
df["id"]= id_no  
df["date"]=date
df["time"]=time
df["nick_name"]=nick_name
df["plt"]=platelet
df["rbc"]=red_cells
df["tlc"]=white_cells
df["hb"]=hemoglobin
df["hct"]=hematocrit
df["mcv"]=m_c_v
df["mch"]=m_c_h
df["mchc"]=m_c_h_c
df["image"]=image

## Saving data as a CSV file
pd.DataFrame.to_csv(df,"retained_sample.csv",index=False)
