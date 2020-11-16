import psycopg2
names=['AKHIL','BHAVNA','CHETNA','DIPTI','GREESHMA',]
usn=['1CR19CS101','1CR19CS102','1CR19CS103','1CR19CS104','1CR19CS105']

def create_physics(list_1,list_2):
    for i in range(len(names)):
        conn=psycopg2.connect("dbname='postgres' user='CMRITERP' password='CMRITERP' host='database-1.cvurrxgydpsj.ap-south-1.rds.amazonaws.com' port ='5432' ")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS physics (name TEXT,usn TEXT,classes_conducted TEXT,classes_attended TEXT,total_marks TEXT,obtained_marks TEXT)")
        #cur.execute("INSERT INTO physics VALUES ('%s','%s')" %(names[i],usn[i]))
        if list_1[i]=="" and list_2[i]=="":
            continue
        else:
            cur.execute("UPDATE physics SET classes_conducted=%s,classes_attended=%s WHERE name=%s",(list_1[i],list_2[i],names[i]))        
        
        conn.commit()
        conn.close()

def create_chemistry(list_1,list_2):
    for i in range(len(names)):
        conn=psycopg2.connect("dbname='postgres' user='CMRITERP' password='CMRITERP' host='database-1.cvurrxgydpsj.ap-south-1.rds.amazonaws.com' port ='5432' ")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS chemistry (name TEXT,usn TEXT,classes_conducted TEXT,classes_attended TEXT,total_marks TEXT,obtained_marks TEXT)")
        #cur.execute("INSERT INTO chemistry VALUES ('%s','%s')" %(names[i],usn[i]))
        if list_1[i]=="" and list_2[i]=="":
            continue
        else:
            cur.execute("UPDATE chemistry SET classes_conducted=%s,classes_attended=%s WHERE name=%s",(list_1[i],list_2[i],names[i]))        
        conn.commit()
        conn.close()
def create_maths(list_1,list_2):
    for i in range(len(names)):
        conn=psycopg2.connect("dbname='postgres' user='CMRITERP' password='CMRITERP' host='database-1.cvurrxgydpsj.ap-south-1.rds.amazonaws.com' port ='5432' ")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS maths (name TEXT,usn TEXT,classes_conducted TEXT,classes_attended TEXT,total_marks TEXT,obtained_marks TEXT)")
        #cur.execute("INSERT INTO maths VALUES ('%s','%s')" %(names[i],usn[i]))
        if list_1[i]=="" and list_2[i]=="":
            continue
        else:
            cur.execute("UPDATE maths SET classes_conducted=%s,classes_attended=%s WHERE name=%s",(list_1[i],list_2[i],names[i]))

        
        conn.commit()
        conn.close()

def create_english(list_1,list_2):
    for i in range(len(names)):
        conn=psycopg2.connect("dbname='postgres' user='CMRITERP' password='CMRITERP' host='database-1.cvurrxgydpsj.ap-south-1.rds.amazonaws.com' port ='5432' ")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS english (name TEXT,usn TEXT,classes_conducted TEXT,classes_attended TEXT,total_marks TEXT,obtained_marks TEXT)")
        #cur.execute("INSERT INTO english VALUES ('%s','%s')" %(names[i],usn[i]))
        if list_1[i]=="" and list_2[i]=="":
            continue
        else:
            cur.execute("UPDATE english SET classes_conducted=%s,classes_attended=%s WHERE name=%s",(list_1[i],list_2[i],names[i]))       
        
        conn.commit()
        conn.close()

def create_computer(list_1,list_2):
    for i in range(len(names)):
        conn=psycopg2.connect("dbname='postgres' user='CMRITERP' password='CMRITERP' host='database-1.cvurrxgydpsj.ap-south-1.rds.amazonaws.com' port ='5432' ")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS computer (name TEXT,usn TEXT,classes_conducted TEXT,classes_attended TEXT,total_marks TEXT,obtained_marks TEXT)")
        #cur.execute("INSERT INTO computer VALUES ('%s','%s')" %(names[i],usn[i]))
        if list_1[i]=="" and list_2[i]=="":
            continue
        else:
            cur.execute("UPDATE computer SET classes_conducted=%s,classes_attended=%s WHERE name=%s",(list_1[i],list_2[i],names[i]))   
        
        conn.commit()
        conn.close()
def create_physics_marks(list_1,list_2):
    for i in range(len(names)):
        conn=psycopg2.connect("dbname='postgres' user='CMRITERP' password='CMRITERP' host='database-1.cvurrxgydpsj.ap-south-1.rds.amazonaws.com' port ='5432' ")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS physics (name TEXT,usn TEXT,classes_conducted TEXT,classes_attended TEXT,total_marks TEXT,obtained_marks TEXT)")
        #cur.execute("INSERT INTO physics VALUES ('%s','%s')" %(names[i],usn[i]))
        if list_1[i]=="" and list_2[i]=="":
            continue
        else:
            cur.execute("UPDATE physics SET total_marks=%s,obtained_marks=%s WHERE name=%s",(list_1[i],list_2[i],names[i]))        
        
        conn.commit()
        conn.close()
def create_chemistry_marks(list_1,list_2):
    for i in range(len(names)):
        conn=psycopg2.connect("dbname='postgres' user='CMRITERP' password='CMRITERP' host='database-1.cvurrxgydpsj.ap-south-1.rds.amazonaws.com' port ='5432' ")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS chemistry (name TEXT,usn TEXT,classes_conducted TEXT,classes_attended TEXT,total_marks TEXT,obtained_marks TEXT)")
        # cur.execute("INSERT INTO chemistry VALUES ('%s','%s')" %(names[i],usn[i]))
        if list_1[i]=="" and list_2[i]=="":
            continue
        else:
            cur.execute("UPDATE chemistry SET total_marks=%s,obtained_marks=%s WHERE name=%s",(list_1[i],list_2[i],names[i]))        
        conn.commit()
        conn.close()
def create_maths_marks(list_1,list_2):
    for i in range(len(names)):
        conn=psycopg2.connect("dbname='postgres' user='CMRITERP' password='CMRITERP' host='database-1.cvurrxgydpsj.ap-south-1.rds.amazonaws.com' port ='5432' ")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS maths (name TEXT,usn TEXT,classes_conducted TEXT,classes_attended TEXT,total_marks TEXT,obtained_marks TEXT)")
        
        #cur.execute("INSERT INTO maths VALUES ('%s','%s')" %(names[i],usn[i]))
        if list_1[i]=="" and list_2[i]=="":
            continue
        else:
            cur.execute("UPDATE maths SET total_marks=%s,obtained_marks=%s WHERE name=%s",(list_1[i],list_2[i],names[i]))

        
        conn.commit()
        conn.close()

def create_english_marks(list_1,list_2):
    for i in range(len(names)):
        conn=psycopg2.connect("dbname='postgres' user='CMRITERP' password='CMRITERP' host='database-1.cvurrxgydpsj.ap-south-1.rds.amazonaws.com' port ='5432' ")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS english (name TEXT,usn TEXT,classes_conducted TEXT,classes_attended TEXT,total_marks TEXT,obtained_marks TEXT)")
        # cur.execute("INSERT INTO english VALUES ('%s','%s')" %(names[i],usn[i]))
        if list_1[i]=="" and list_2[i]=="":
            continue
        else:

            cur.execute("UPDATE english SET total_marks=%s,obtained_marks=%s WHERE name=%s",(list_1[i],list_2[i],names[i]))       
        
        conn.commit()
        conn.close()

def create_computer_marks(list_1,list_2):
    for i in range(len(names)):
        conn=psycopg2.connect("dbname='postgres' user='CMRITERP' password='CMRITERP' host='database-1.cvurrxgydpsj.ap-south-1.rds.amazonaws.com' port ='5432' ")
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS computer (name TEXT,usn TEXT,classes_conducted TEXT,classes_attended TEXT,total_marks TEXT,obtained_marks TEXT)")
        # cur.execute("INSERT INTO computer VALUES ('%s','%s')" %(names[i],usn[i]))
        if list_1[i]=="" and list_2[i]=="":
            continue
        else:
            cur.execute("UPDATE computer SET total_marks=%s,obtained_marks=%s WHERE name=%s",(list_1[i],list_2[i],names[i]))   
        
        conn.commit()
        conn.close()

# create_physics(list_1,list_2)
# create_chemistry(list_1,list_2)
# create_english(list_1,list_2)
# create_computer(list_1,list_2)
# create_maths(list_1,list_2)
'''
    the below codes is to fetch data from tables of teachers
'''

def fetch_data():
    conn=psycopg2.connect("dbname='postgres' user='CMRITERP' password='CMRITERP' host='database-1.cvurrxgydpsj.ap-south-1.rds.amazonaws.com' port ='5432' ")
    cur1=conn.cursor()
    cur1.execute("SELECT * FROM MATHS")
    rows1=cur1.fetchall()


    cur2=conn.cursor()
    cur2.execute("SELECT * FROM PHYSICS")
    rows2=cur2.fetchall()


    cur3=conn.cursor()
    cur3.execute("SELECT * FROM COMPUTER")
    rows3=cur3.fetchall()


    cur4=conn.cursor()
    cur4.execute("SELECT * FROM CHEMISTRY")
    rows4=cur4.fetchall()


    cur5=conn.cursor()
    cur5.execute("SELECT * FROM ENGLISH")
    rows5=cur5.fetchall()

    return ([rows1,rows2,rows3,rows4,rows5])


    # return ([rows1,rows2,rows3,rows4,rows5])

