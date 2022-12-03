import sqlite3
con=sqlite3.connect('test_db')
cur=con.cursor()
cur.execute('pragma foreign_keys=on')

'''
cur.execute("""
create table operator
(opid integer primary key not null,
name text not null,
phno integer not null,
email text not null,
address text not null,
password text not null)""")

cur.execute("""
create table bus
(bid integer primary key not null,
type text ,
capacity tinyint not null,
company text,
lfare integer not null,
op_id integer not null ,
FOREIGN KEY(op_id) REFERENCES operator(opid) ON DELETE CASCADE ON UPDATE CASCADE)
""")

cur.execute("""
create table route
(rid integer not null,
sid integer not null,
s_name text not null,
b_fare integer not null,
distance integer not null,
PRIMARY KEY(rid,sid))
""")

cur.execute("""
create table running(b_id integer not null,
r_id integer not null,
r_date date not null,
brd INTEGER not null PRIMARY KEY AUTOINCREMENT,
UNIQUE(b_id,r_id,r_date),
FOREIGN KEY(b_id) REFERENCES bus(bid) ON DELETE CASCADE ON UPDATE CASCADE
)
""")

cur.execute("""
create table seats (
b_rd integer not null,
s_id integer not null,
counter integer not null CHECK(counter > 0 OR counter = 0),
SeatMatrix integer not null ,
PRIMARY KEY (b_rd,s_id),
FOREIGN KEY (b_rd) REFERENCES running(brd) ON DELETE CASCADE ON UPDATE CASCADE
)
""")

'''
'''
cur.execute("""
create table travelers(
t_phone integer PRIMARY KEY not null,
t_source text ,
t_destination ,
num_seats integer ,
t_fare integer ,
t_brd integer
)
""")

cur.execute("""
create table t_details(
t_name text ,
t_age integer ,
t_gender text ,
t_seat integer ,
t_phonenumber integer not null,
FOREIGN KEY (t_phonenumber) REFERENCES travelers(t_phone) ON DELETE CASCADE ON UPDATE CASCADE
)
""")
'''
src='jabalpur'
dest='shridham'
cur.execute('select rid,sid,s_name,distance from route  where s_name=? or s_name=? ',(src,dest))
var1=cur.fetchall()
#print(var1)
rid=[]
sid=[]
dest_sid=[]
dis=[]
temp=1
for i in var1:
    if temp >= len(var1):
        break
    if i[0]==var1[temp][0]:
        if i[2]==src:
            rid.append(i[0])
            sid.append(i[1])
            dis.append((int(var1[temp][3])-int(i[3])))
            dest_sid.append(var1[temp][1])
    temp+=1
#print(rid[1])
cur.execute("select name,type,company,capacity,lfare,brd from operator,bus,running,seats where opid=op_id and bid=b_id and r_id=? and r_date=? and brd=b_rd and s_id=?",(int(rid[1]),'1-12-2022',1))
var=cur.fetchall()
#print(var)

n=len(rid)
var2=[]
Available=[] #available seats
i=0
k=0
while i<n:
    #try:
    cur.execute("""select name,type,company,capacity,lfare,brd from operator,bus,running,seats where opid=op_id and bid=b_id and r_id=? and r_date=? and brd=b_rd and s_id=?""",(rid[i],'1-12-2022',sid[i]))
    print(rid[i])
    var2.append(cur.fetchall())
    print(len(var2[i]))

    try:
        cur.execute("""select counter from  seats where b_rd=? and s_id>=? and s_id <? """,(var2[i][0][5],sid[i],dest_sid[i]))
        temp_seat=(cur.fetchall())
        a=var2[i][0][3]
        for value  in  temp_seat:
            if int(value[0])<int(a):
                a=int(a)-(int(a)- int(value[0]))
        k+=1
        Available.append(a)
    except:
        kkk=0
    i+=1
print(Available)




#cur.execute('update seats set counter =20 where b_rd=40 and s_id >=3 and s_id <5')
#except sqlite3.IntegrityError:
#    print("Operator id already exisit")
#except TypeError:
#    print("TypeError")
con.commit()
con.close()
