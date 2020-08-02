# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 23:19:35 2020

@author: DC
"""

#importing libraries
import os
import datetime
import reportlab
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics


#Registering hindi font
#pdfmetrics.registerFont(TTFont('hindi', 'dev.ttf'))
pdfmetrics.registerFont(TTFont('arial', 'arial.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))

#Required Paramneters
college_name_english = "Indian Institute Of Information Technology, Nagpur"
college_name_hindi = "भारतीय सूचना प्रौद्योगिकी संस्थान, नागपुर"
logo = "iiitlogo.png" 


def expo(loc,name,enrol,dept,deg,note1pg,student_marks,student_marks_cumlative,sem_details):
    
                  
    save_location = loc
    namee = name
    enrolment = enrol
    branch = dept
    degree = deg
    
    #Footnotes
    footnote = note1pg
    #Sem Notes
    semno = sem_details
    
    #Student Marks 
    marks = student_marks
    marks2 =student_marks_cumlative

    #Creating Canvas
    x= canvas.Canvas(save_location,pagesize = A4,)

    #Giving Font 


    #College Name,Logo,Header 
    #x.setFont('hindi', 14)
    x.drawString(135,780,college_name_hindi)
    x.setFont('Times-Bold', 18)
    x.drawString(135,750,college_name_english)
    x.drawImage(logo,50,750,width=1*inch,height=1*inch)
    x.setLineWidth(4)
    x.setStrokeColor('crimson')
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
    x.drawString(100,700,namee)
    x.drawString(420,700,enrolment)
    x.drawString(100,680,branch)
    x.drawString(420,680,degree)

    #Bottom Notes printing page 1
    x.setFont('Vera', 6)
    x.drawString(50,70,footnote[0])
    x.drawString(50,60,footnote[1])
    x.drawString(50,50,footnote[2])
    x.drawString(50,40,footnote[3])


    #Sem Template Grids
    x.setLineWidth(0.5)
    x.setStrokeColor('black')
    mt=670
    ml=50
    for i in range(0,8):
        #Printing Grid
        x.grid([ml,ml+245],[mt,mt-13])
        x.grid([ml,ml+30,ml+169,ml+209,ml+245],[mt-13,mt-30+1,mt-40+1,mt-50+1,mt-60+1,mt-70+1,mt-80+1,mt-90+1,mt-100+1])
        x.grid([ml,ml+47],[mt-112,mt-132])
        x.grid([ml+122,ml+170],[mt-112,mt-132])
        x.grid([ml+47,ml+72,ml+97,ml+122],[mt-112,mt-122,mt-132])
        x.grid([ml+170,ml+195,ml+220,ml+245],[mt-112,mt-122,mt-132])
        
        #Printing Sem Numbers 
        x.setFont('VeraBd',8)
        x.drawString(ml+5,mt-10,semno[i])
    
        #Printing Sr. No Course Code Credits and Grade Heading 
        x.setFont('VeraBd',7)
        x.drawString(ml+5,mt-24,"CODE")
        x.drawString(ml+35,mt-24,"COURSE")
        x.drawString(ml+175,mt-24,"CREDIT")
        x.drawString(ml+213,mt-24,"GRADE")
        x.setFont('arial',9)
        x.drawString(ml+7,mt-125,"SGPA")
        x.drawString(ml+129,mt-125,"CGPA")
        x.setFont('arial',6)
        x.drawString(ml+50,mt-120,"Credit")
        x.drawString(ml+75,mt-120,"EGP")
        x.drawString(ml+100,mt-120,"SGPA")
        x.drawString(ml+173,mt-120,"Credit")
        x.drawString(ml+198,mt-120,"EGP")
        x.drawString(ml+223,mt-120,"CGPA")
        
        #Printing Subjects 
        #Condition for the subjects to  there and sem has to be present 
        if(len(marks)>i and len(marks[i])>0):
            for j in range(0,len(marks[i])):
                x.setFont('arial',6)
                x.drawString(ml+2,mt-37-j*10,marks[i][j][0])
                x.drawString(ml+32,mt-37-j*10,marks[i][j][1])
                x.drawString(ml+172,mt-37-j*10,marks[i][j][2])
                x.drawString(ml+212,mt-37-j*10,marks[i][j][3])
                
            #Printing Cumlative Subjects
            shift=0
            for j in range(0,6):
                x.drawString(ml+50+shift,mt-130,str(marks2[i][j]))
                shift += 75 if j==2 else 25


        
        if(i%2==0):
            ml=ml+250
        else:
                mt=mt-150
                ml=ml-250
                
    #Save The PDF
    x.save()    
    