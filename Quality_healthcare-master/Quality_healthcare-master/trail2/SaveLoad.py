import psycopg2 as pg

class Patient:
    def __init__(self, userid, password,name,ph,id):
        self.userid=userid
        self.password=password
        self.name=name
        self.ph=ph
	self.id=id

    def __repr__(self):
	    return "<User {}>".format(self.userid)
		
    
    def save_to_db(self):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT into ptable (userid,pass,pname,ph) values (%s,%s,%s,%s)',(self.userid,self.password,self.name,self.ph))
	    

    
    @classmethod
    def load_from_db_by_userid(cls,userid):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from ptable where userid=%s',(userid,))
                p_data=cursor.fetchone()
                return cls(p_data[1],p_data[2],p_data[3],p_data[4],p_data[0])
 
    @classmethod
    def load_from_db_by_id(cls,p_id):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from ptable where id=%s',(p_id,))
                p_data=cursor.fetchone()
                return cls(p_data[1],p_data[2],p_data[3],p_data[4],p_data[0])
	    
class Doctor:
    def __init__(self, userid, password,name,specialization,free_time,id):
        self.userid=userid
        self.password=password
        self.name=name
        self.specialization=specialization
        self.free_time=free_time
	self.id=id
		
    def __repr__(self):
	    return "<User {}>".format(self.userid)
		
    
    def save_to_db(self):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT into dtable (userid,pass,dname,specialization,free_time) values (%s,%s,%s,%s,%s)',(self.userid,self.password,self.name,self.specialization,self.free_time))
	    

    
    @classmethod
    def load_from_db_by_userid(cls,userid):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from dtable where userid=%s',(userid,))
                d_data=cursor.fetchone()
                return cls(d_data[1],d_data[2],d_data[3],d_data[4],d_data[5],d_data[0])
    @classmethod
    def load_from_db_by_userid_list(cls,userid):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from dtable where userid=%s',(userid,))
                d_data=cursor.fetchone()
                return d_data

    @classmethod
    def load_from_db_all(cls):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from dtable')
                d_data=cursor.fetchall()
                return d_data

	    
class Booking:
    def __init__(self, p_id, d_id,time_allocated):
            self.p_id=p_id
            self.d_id=d_id
            self.time_allocated=time_allocated
		
    def __repr__(self):
	    return "<User {}>".format(self.userid)
		
    
    def save_to_db(self):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('INSERT into btable (p_id,d_id,time_allocated) values (%s,%s,%s)',(self.p_id,self.d_id,self.time_allocated))
	    
    def del_from_db_by_userid(self,d_id):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('delete * from btable where d_id=(%s)',(self.d_id))
                
    
    @classmethod
    def load_from_db_by_userid(cls,d_id):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from btable where d_id=%s',(d_id,))
                d_data=cursor.fetchall()
                return d_data
    @classmethod
    def load_from_db_by_puserid(cls,p_id):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('select * from btable where p_id=%s',(p_id,))
                p_data=cursor.fetchall()
                return p_data

    @classmethod
    def del_from_db_by_userid(cls,d_id):
        with pg.connect(user='postgres', password='Ankita123', database='postgres',host='localhost') as connection:
            with connection.cursor() as cursor:
                cursor.execute('delete from btable where d_id=%s',str(d_id))
    
