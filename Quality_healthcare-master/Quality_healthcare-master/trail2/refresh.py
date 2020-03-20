import os
import time
from SaveLoad import Patient,Doctor,Booking

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
      t=30; 
      if(newpid==0):
          child(t,d_id)
      break
       
parent('3')
