# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 04:57:58 2019

@author: ankita1999
"""

from flask import Flask, redirect, url_for, request, render_template
import pview as ts
from SaveLoad import Doctor,Patient,Booking

p_user_id="nul"

app = Flask(__name__,static_url_path='/static')

@app.route('/dr_signup',methods=['POST', 'GET'])
def dr_signup():
    input_list=request.form.items()
    userid=input_list[0][1]
    name=input_list[4][1]
    specialization=input_list[3][1]
    free_time=input_list[2][1]
    password=input_list[1][1]
    d=Doctor(userid, password,name,specialization,free_time,None)
    d.save_to_db()
    return render_template('new.html')
    
@app.route('/p_signup',methods=['POST', 'GET'])
def p_signup():
    input_list=request.form.items()
    userid=input_list[0][1]
    name=input_list[1][1]
    ph=input_list[2][1]
    password=input_list[3][1]
    d=Patient(userid, password,name,ph,None)
    d.save_to_db()
    return render_template('new.html')
    
@app.route('/signup',methods = ['POST', 'GET'])
def signup():
    input_list=request.form.items()
    btn=input_list[0][0]
    if(btn=='dr_signup'):
        return render_template('doctor.html')
    if(btn=='p_signup'):
        return render_template('patient.html')
    
@app.route('/login',methods = ['POST', 'GET'])
def login():
    global p_user_id
#Login For Doctor:
    input_list=request.form.items()
    cat_id=input_list[0][0]
    if(cat_id =='d_id'):
        user_id=input_list[0][1]
        e_pass=input_list[-1][-1]
        user_details=Doctor.load_from_db_by_userid(user_id)
        o_pass=user_details.password
        if(e_pass==o_pass):
            b_details=Booking.load_from_db_by_userid(str(user_details.id))
            disp_list=[]
            for b in b_details:
               list1=[]  
               p_data=Patient.load_from_db_by_id(int(b[1]))
               list1.append(p_data.name)
               list1.append(p_data.ph)
               list1.append(b[-1])
               disp_list.append(list1)
            print(disp_list)
            return render_template('doc.html',result=disp_list,name=user_details.name) 
        return "Wrong Password"  
#Login For Patient:       
    else:
        user_id=input_list[0][1]
        p_user_id=user_id
        print(p_user_id)
        e_pass=input_list[-1][-1]
        user_details=Patient.load_from_db_by_userid(user_id)
        o_pass=user_details.password
        if(e_pass==o_pass):
            return render_template('pat.html',result = ts.final_list)   
        return "Wrong Password"

@app.route('/', methods=['GET', 'POST'])
def doc1():
   return render_template('new.html')
      
if __name__ == '__main__':
    app.run()
