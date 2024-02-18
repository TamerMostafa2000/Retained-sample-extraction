# Retained-Sample-Text-Extraction
Python code for extracting texts from scanned PDF file of Sysmex CBC instrument printouts

Retained samples refer to any portion of a patient's sample (blood, tissue, urine, etc.) that is set aside after the initial testing is complete. These samples are stored for a specific period under defined conditions for various purposes.
One of these purposes is quality control to ensure the accuracy and reliability of their testing procedures.
The result of the retained samples are collected for farther calculations and statistics procedures.
The challeng is to extract the data from hundereds of instrument printouts.
In this project, we worked on retained samples results from 2 CBC instruments(Sysmex XN1000-1 and XN1000-2).
Data are the CBC parameters(HB, HCT, MCV,MCH,MCHC,TLC,RBCs,PLTs) and printout data (instrument name,date and time).
Instrument printouts (hard copy) were scanned into a single PDF file with hundereds of pages.
I have used several open sorced librarie as pytesseract, pypdf, PIL and other libraries.

First, I convert the pages into images.
Then, I extract the texts from the images.
finally, I collected the data into a DataFrame then into CSV file.

