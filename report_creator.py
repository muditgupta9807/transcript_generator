# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 23:19:35 2020

@author: DC
"""

#importing libraries

import time
import os
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
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
x.drawString(50,700,"Name : ")
x.drawString(330,700,"Enrolment No : ")
x.drawString(50,680,"Branch : ")
x.drawString(330,680,"Degree : ")

x.setFont('Vera', 9)
x.drawString(120,700,name)
x.drawString(420,700,enrolment)
x.drawString(120,680,branch)
x.drawString(420,680,degree)






#Save The PDF
x.save()
