# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 23:19:35 2020

@author: DC
"""

#importing libraries

import datetime
import os
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER,TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from englisttohindi.englisttohindi import EngtoHindi
#Registering hindi font
pdfmetrics.registerFont(TTFont('hindi', 'dev.ttf'))
pdfmetrics.registerFont(TTFont('arial', 'arial.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

#Required Paramneters
college_name_english = "Indian Institute Of Information Technology, Nagpur"
college_name_hindi = EngtoHindi(message="Indian Institute of Information Technology, Nagpur".encode('utf-8'))
logo = "iiitlogo.png"               
save_location = "C:/Users/DC/Downloads/test.pdf"
name = "Mudit Gupta"
enrolment = "BT18ECE013"
branch = "Electronics and Communication Engineering"
degree = "Bachelors Of Technology"

#Footnotes
footnote1 = "Note : Candidate has successfully completed all requirements for award of degree Medium of instruction : English"
footnote2 = "Abbreviations: SGPA - Semester Grade Point Average, CGPA - Cumlative Grade Point Average, EGP - Earned Grade Points"
footnote3 = "(The Statment is subject to correction, if any)"
footnote4 = "Date : "+str(datetime.datetime.today().strftime ('%d-%b-%Y'))

#Sem Notes
semno = ("SEM. 1 (July-Nov. 2018) ","SEM. 2 (Jan-May. 2019)","SEM. 3 (July-Nov. 2019) ","SEM. 4 (Jan-May. 2020)","SEM. 5 (July-Nov. 2020) ","SEM. 6 (Jan-May. 2021)","SEM. 7 (July-Nov. 2021) ","SEM. 8 (Jan-May. 2022)")


#Creating Canvas
x= canvas.Canvas(save_location,pagesize = A4,)

#Giving Font 


#College Name,Logo,Header 
x.setFont('hindi', 14)
x.drawString(135,780,college_name_hindi.convert)
x.setFont('arial', 18)
x.drawString(135,750,college_name_english)
x.drawImage(logo,50,750,width=1*inch,height=1*inch)
x.setLineWidth(2)
x.setStrokeColor('red')
x.line(50,740,550,740)

#Student Details 
x.setFont('Times-Bold', 18)
x.drawCentredString(300,720,"GRADE CARD")

x.setFont('VeraBd', 10)
x.drawString(50,700,"Name   :")
x.drawString(330,700,"Enrolment No :")
x.drawString(50,680,"Branch :")
x.drawString(330,680,"Degree           :")

x.setFont('Vera', 9)
x.drawString(100,700,name)
x.drawString(420,700,enrolment)
x.drawString(100,680,branch)
x.drawString(420,680,degree)

#Bottom Notes printing
x.setFont('Vera', 6)
x.drawString(50,70,footnote1)
x.drawString(50,60,footnote2)
x.drawString(50,50,footnote3)
x.drawString(50,40,footnote4)


#Sem Template Grids
x.setLineWidth(0.5)
x.setStrokeColor('black')
mt=670
ml=50
for i in range(0,8):
    x.grid([ml,ml+245],[mt,mt-13])
    x.grid([ml,ml+39,ml+169,ml+209,ml+245],[mt-13,mt-30+1,mt-40+1,mt-50+1,mt-60+1,mt-70+1,mt-80+1,mt-90+1,mt-100+1])
    x.grid([ml,ml+39,ml+169,ml+209,ml+245],[mt-110,mt-120,mt-130])
    if(i%2==0):
        ml=ml+250
    else:
        mt=mt-150
        ml=ml-250
        

#Save The PDF
x.save()
