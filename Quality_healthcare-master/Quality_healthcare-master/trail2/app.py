from SaveLoad import Patient,Doctor,Booking




print(list(Doctor.load_from_db_by_userid_list("user2")))

"""b_details=Booking.load_from_db_by_userid('1')
disp_list=[]
for b in b_details:
    list1=[]  
    p_data=Patient.load_from_db_by_id(int(b[1]))
    list1.append(p_data.name)
    list1.append(p_data.ph)
    list1.append(b[-1])
    disp_list.append(list1)
print(disp_list)

"""

"""p_user_id="user6"
d_user_id="user1"
t_slot=['19:00']

pat_details=Patient.load_from_db_by_userid(p_user_id)
doc_details=Doctor.load_from_db_by_userid(d_user_id)

b_details=Booking(pat_details.id,doc_details.id,t_slot[0],None)
b_details.save_to_db()

"""





"""d_user=Doctor('user1','doc','Doctor1','Bone','18:00:00-20:00:00',None)
d_user.save_to_db()
p_user=Patient('user6','qwerty','Nanda','9123456789',None)
p_user.save_to_db()


b_details=Booking(1,1,'18:15:00-18:30:00',None)
b_details.save_to_db()


b_details=Booking.load_from_db_by_userid('1')
for b in b_details:    
    print(b[0],b[1],b[3])


d_user=Doctor('user2','doc','Doctor2','teeth','19:00:00-20:00:00',None)
d_user.save_to_db()



d_data=Doctor.load_from_db_all()
for d in d_data:    
    print(d[0],d[1],d[2],d[3],d[4],d[5]+"\n")
"""
