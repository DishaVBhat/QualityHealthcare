from flask import Flask, redirect, url_for, request, render_template
import pview as ts
from SaveLoad import Doctor,Patient,Booking
import os
import time
x="nul"
p_user_id="nul"
print(ts.final_list)
app = Flask(__name__,static_url_path='/static')

@app.route('/success',methods=['POST'])
def success():
   global x
   input_list=request.form.items()
   if input_list[0][0][0]=='p':
      x='p'
   else:
      x='d'
   return redirect(url_for('session',session_id=input_list[0][0][1:]))
	
@app.route('/history',methods=['POST'])
def history():
    input_list=request.form.items()
    b_details=Booking.load_from_db_by_puserid(input_list[0][0])
    disp_list=[]
    for b in b_details:
               list1=[]  
               print("HI",b[2])
               d_data=Doctor.load_from_db_by_userid(b[2])
               list1.append(d_data.name)
               list1.append(b[-1])
               list1.append(b[0])
               disp_list.append(list1)
    return render_template('patien.html',result=disp_list)
            
    
@app.route('/session/<session_id>/')
def session(session_id):
   global x
   print(x)
   return render_template("index.html",x1=x)

@app.route('/confirm',methods = ['POST', 'GET'])
def result():
   global p_user_id
   if request.method == 'POST':
      user_id=request.form.keys()
      t_slot=request.form.values()

      #Adding to btable
      d_user_id=user_id[0]
      pat_details=Patient.load_from_db_by_userid(p_user_id)
      doc_details=Doctor.load_from_db_by_userid(d_user_id)
      b_details=Booking(pat_details.id,doc_details.id,t_slot[0])
      b_details.save_to_db()

      #Starting the Refresh Process:
      for b in ts.final_list:
          if(b[1]==d_user_id):
              if(b[-1]==0):
                  print(doc_details.id)
                  parent(str(doc_details.id))
                  b[-1]=1
      #Removing the occupied slot:
      for b in ts.final_list:
          if user_id[0] in b:
              b1=b[-2]
              b1.remove(t_slot[0])
      return render_template('confirm.html')


@app.route('/login',methods = ['POST'])
def login():
    global p_user_id
#Login For Doctor:
    input_list=request.form.items()
    cat_id=input_list[0][0]
    if(cat_id =='d_id'):
        user_id=input_list[0][1]
        e_pass=input_list[2][1]
        user_details=Doctor.load_from_db_by_userid(user_id)
	print(user_details)
        o_pass=user_details.password
	print(o_pass)
        if(e_pass==o_pass):
            b_details=Booking.load_from_db_by_userid(str(user_details.id))
            disp_list=[]
            for b in b_details:
               list1=[]  
               p_data=Patient.load_from_db_by_id(int(b[1]))
               list1.append(p_data.name)
               list1.append(p_data.ph)
               list1.append(b[-1])
               list1.append(b[0])
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
            return render_template('pat.html',result = ts.final_list,userid=p_user_id)   
        return "Wrong Password"

@app.route('/', methods=['GET', 'POST'])
def doc1():
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

@app.route('/dr_signup',methods=['POST'])
def dr_signup():
    input_list=request.form.items()
    userid=input_list[0][1]
    name=input_list[4][1]
    specialization=input_list[3][1]
    free_time=input_list[2][1]
    password=input_list[1][1]
    d=Doctor(userid, password,name,specialization,free_time,None)
    d.save_to_db()
    list1=list(Doctor.load_from_db_by_userid_list(userid))
    print(list1)
    hour_diff=int(((list1[-1].split('-'))[1].split(':'))[0])-int(((list1[-1].split('-'))[0].split(':'))[0])
    min_diff=int(((list1[-1].split('-'))[1].split(':'))[1])-int(((list1[-1].split('-'))[0].split(':'))[1])
    if(min_diff<0):
        hour_diff-=1
        min_diff*=(-1)
    no_blocks=hour_diff*4+round((min_diff/60)*4)

    #Calculating Time Slots:
    min=((list1[-1].split('-'))[0].split(':'))[1]
    hour=(list1[-1].split('-')[0].split(':'))[0]
    
    t_slot=[]
    t_slot.append(str(hour).zfill(2)+":"+str(min).zfill(2))
    for i in range(0,int(no_blocks)):
        hour=str(int(hour)+(int(min)+15)//60).zfill(2)
        min=str((int(min)+15) % 60).zfill(2)
        t_slot.append(hour+":"+min)
    list1.append(t_slot)
    list1.append(0)
    ts.final_list.append(list1)
    print(ts.final_list)
    return render_template('new.html')

def child(t,d_id):
   time.sleep(t)
   Booking.del_from_db_by_userid(d_id)
   print(d_id+" doctor appointment info deleted from Booking table")
   os._exit(0)  

def parent(d_id):#Parameter Time Period and Discount Price
   while True:
      print(d_id)
      newpid = os.fork()
      last_time='20:00'
      start_time_hour=time.localtime().tm_hour
      start_time_min=time.localtime().tm_min
      last_time=last_time.split(':')
      last_time_hour=int(last_time[0])
      last_time_min=int(last_time[1])

      if((last_time_hour-start_time_hour)>0):
         wait_hour=last_time_hour-start_time_hour
      else:
         wait_hour=24-abs(last_time_hour-start_time_hour)
      if((last_time_min-start_time_min)>=0):
         wait_min=last_time_min-start_time_min
      else:
         wait_min=(last_time_min-start_time_min)+60
         wait_hour=wait_hour-1
         print(wait_hour)
         print(wait_min)
      #t=wait_min*60+wait_hour*60*60
      t=120; 
      if(newpid==0):
          child(t,d_id)
      break


if __name__ == '__main__':
    app.run()
