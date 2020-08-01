# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 07:49:51 2020

@author: DC
"""

import report_creator as rc
import datetime
location = "C:/Users/DC/Desktop/test.pdf"
name = "Mudit Gupta"
enrolment = "BT18ECE013"
branch = "Electronics and Communication Engineering"
degree = "Bachelors Of Technology"
    
#Footnotes
footnote = ("Note : Candidate has successfully completed all requirements for award of degree Medium of instruction : English","Abbreviations: SGPA - Semester Grade Point Average, CGPA - Cumlative Grade Point Average, EGP - Earned Grade Points","(The Statment is subject to correction, if any)","Date : "+str(datetime.datetime.today().strftime ('%d-%b-%Y')))

#Sem Notes
semno = ("SEM. 1 (July-Nov. 2018) ","SEM. 2 (Jan-May. 2019)","SEM. 3 (July-Nov. 2019) ","SEM. 4 (Jan-May. 2020)","SEM. 5 (July-Nov. 2020) ","SEM. 6 (Jan-May. 2021)","SEM. 7 (July-Nov. 2021) ","SEM. 8 (Jan-May. 2022)")
    
    
#Student Marks 
marks = ([["MAl 101","Mathemathics-1","4","BB"],["HUl 101","Numerical Methods and Probability Theory","3","BB"],["ECl 101","Electonics,Devices and Circuits","4","AB"]],[],[["MAl 101","Mathemathics-1","4","BB"],["HUl 101","Coomunication Skills","3","BB"],["ECl 101","Electonics,Devices and Circuits","4","AB"]])
    

rc.expo(location,name,enrolment,branch,degree,footnote,marks,semno)