# Retained-Sample-Text-Extraction
Python code for extracting texts from scanned PDF file of Sysmex CBC instrument printouts

Beside internal and external controls, Retained samples refer to any kind of a patient's blood sample, that is set aside after the initial testing is complete. These samples are stored for a specific period under defined conditions for various purposes. One of these purposes is quality control to ensure the accuracy and reliability of their testing procedures. 
The result of the retained samples are collected for farther calculations and statistics procedures. The challenge is to extract the data from tens of instrument printouts. In this project, we worked on retained samples results from 2 CBC instruments(Sysmex XN1000-1 and XN1000-2). The data are the CBC parameters(HB, HCT, MCV, MCH, MCHC, TLC, RBCs, PLTs) and printout data (instrument name, date and time), (new_image_97.jpg) is an example. Instrument printouts (hard copy) were scanned into several PDF files with tens of pages. I have used several open sourced libraries like pytesseract, pypdf, PIL and other libraries.

First, I merged the pdf files into one single pdf file. After that, I convert the pages into images. Then, I extract the texts from the images after enhancing the quality of the images. finally, I collected the data into a DataFrame (Screenshot 2024-02-21 202229.png) then into a CSV file.


This work needs more work to enhance the quality of the text extraction.

