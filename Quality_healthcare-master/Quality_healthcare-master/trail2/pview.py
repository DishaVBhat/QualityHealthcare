from SaveLoad import Doctor,Patient,Booking

#Importing Doctors Details
d_data=Doctor.load_from_db_all()
final_list=[]
for list1 in d_data:
    list1=list(list1)
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
    final_list.append(list1)
print(final_list)
