import sqlite3
con=sqlite3.connect('test_db')
cur=con.cursor()
cur.execute('pragma foreign_keys=on')
#############################################################################################################################
try:
    from tkinter import *
    from tkinter.messagebox import *
except:
    from Tkinter import *
    from Tkinter.messagebox import *

class python_bus:

#######################################################################################################################
    def Confirmation(self,phone):
        root=Tk()
        l,w=root.winfo_screenwidth(),root.winfo_screenheight()
        root.geometry('%dx%d+0+0'%(l,w))
        root.columnconfigure(0,weight=1)

        frame=Frame(root,relief="groove",bd=3,padx=30,pady=20)
        frame.grid(row=3,column=0)
        frame2=Frame(root)
        frame2.grid(row=4,column=0,padx=(30,0))

        try:
            img=PhotoImage(file=".\\resourses\Bus_for_project.png")
            home=PhotoImage(file=".\\resourses\home.png")
        except:
            img=PhotoImage(file=".//resourses/Bus_for_project.png")
            home=PhotoImage(file="./resourses/home.png")
        def GotoHome():
            root.destroy()
            self.HomePage()

        Label(root,image=img).grid(row=0,column=0)
        Label(root,text='Online Bus Booking System',font='Arial 20 bold',bg='Light Blue',fg='red').grid(row=1,column=0,pady=20)

        cur.execute('select t_source,t_destination,num_seats,t_fare,r_date from travelers,running where t_phone=? and brd=t_brd ',(phone,))
        var=cur.fetchall()
        if len(var)==0:
            root.bell()
            showerror('Not Found','Booking Not Found')
            return

        Label(frame,text="Phone Number: ",font="Arial 14 bold").grid(row=0,column=0)
        Label(frame,text=phone,font="Arial 14").grid(row=0,column=1,padx=(0,30))
        Label(frame,text="Bording: ",font="Arial 14 bold").grid(row=0,column=2)
        Label(frame,text=var[0][0],font="Arial 14").grid(row=0,column=3,padx=(0,30))
        Label(frame,text="Destination: ",font="Arial 14 bold").grid(row=0,column=4)
        Label(frame,text=var[0][1],font="Arial 14").grid(row=0,column=5,padx=(0,30))
        Label(frame,text="Number of Seats: ",font="Arial 14 bold").grid(row=0,column=6)
        Label(frame,text=var[0][2],font="Arial 14").grid(row=0,column=7,padx=(0,30))
        Label(frame,text="Fare:",font="Arial 14 bold").grid(row=0,column=8)
        Label(frame,text=var[0][3],font="Arial 14").grid(row=0,column=9,padx=(0,30))
        Label(frame,text="Journy Date:",font="Arial 14 bold").grid(row=0,column=10)
        Label(frame,text=var[0][4],font="Arial 14").grid(row=0,column=11,padx=(0,30))

        cur.execute('select t_name,t_gender,t_seat from t_details where t_phonenumber=? ',(phone,))
        var1=cur.fetchall()
        print(var1)
        Label(frame2,text=" Name of Passanger ",font="Arial 14 bold").grid(row=0,column=0,pady=(20,10))
        Label(frame2,text=" Gender ",font="Arial 14 bold").grid(row=0,column=1,padx=150,pady=(20,10))
        Label(frame2,text=" Seat Number ",font="Arial 14 bold").grid(row=0,column=2,pady=(20,10))
        j=1
        for i in var1:
            Label(frame2,text=i[0]).grid(row=j,column=0)
            if i[1]==1:
                Label(frame2,text='M').grid(row=j,column=1)
            else:
                Label(frame2,text='F').grid(row=j,column=2)
            j+=1

        Button(root,image=home,command=GotoHome).grid(row=6,column=0,pady=50)

        root.mainloop()

#######################################################################################
    def AddRun(self,opid):
        root = Tk()
        h, w = root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        try:
            img = PhotoImage(file='.//resourses/Bus_for_project.png')
            home = PhotoImage(file='.//resourses/home.png')
        except:
            img = PhotoImage(file='.\\resourses\Bus_for_project.png')
            home = PhotoImage(file='.\\resourses\home.png')

        root.columnconfigure(0, weight=1)

        frame1 = Frame(root)
        frame1.grid(row=0, column=0)
        frame2 = Frame(root)
        frame2.grid(row=1, column=0)
        frame3= Frame(root)
        frame3.grid(row=2,column=0)
        def GotoHome():
            root.destroy()
            self.HomePage()
        def add(option):
            i=0
            str=('  Add  ','Delete')
            def new():
                try:
                    bid=int(B_id.get())
                    cur.execute('select bid from bus where bid=? and op_id=?',(bid,opid))
                    var=cur.fetchall()
                    if len(var)==0:
                        root.bell()
                        showerror('Error!','Bus Id not related to you.')
                        return
                except:
                    root.bell()
                    showerror('Error!','Invalid Bus Id')
                    return
                try:
                    rid=int(R_id.get())
                    cur.execute('select rid from route where rid=?',(rid,))
                    var=cur.fetchall()
                    if len(var)==0:
                        root.bell()
                        showerror('Error!','Route Id doesn\'t Exist.')
                        return
                except:
                    root.bell()
                    showerror('Error!','Invalid Route Id')
                    return

                d=R_date.get()
                date=d.split("-")
                try:
                    day=int(date[0])
                    month=int(date[1])
                    year=int(date[2])
                    if len(date) != 3:
                        raise
                    if year < 2022 or month > 12 or day > 31:
                        raise
                except:
                    root.bell()
                    showerror('Error!','Invalid Date ')
                    return

                if option == 0:
                    cur.execute('select brd from running where b_id=? and r_date=? and r_id=?',(bid,d,rid))
                    check1=cur.fetchall()
                    if len(check1) !=0:
                        root.bell()
                        showerror('Error!','Running Already Exist')
                        return

                    cur.execute('select brd from running where b_id=? and r_date=?',(bid,d))
                    check2=cur.fetchall()

                    if len(check2)==0:
                        cur.execute('insert into running(b_id,r_id,r_date) values(?,?,?)',(bid,rid,d))
                    else:
                        root.bell()
                        showerror('Error!','The Bus is already running on this date in another route')
                        return

                    cur.execute("""
                    select brd,sid,capacity from running,route,bus
                    where rid=? and bid=? and r_date=? and bid=b_id
                    """,(rid,bid,d))
                    var1=cur.fetchall()

                    for i in var1:
                        i=i+(0,)
                        cur.execute("""
                        insert into seats (b_rd,s_id,counter,SeatMatrix)
                        values(?,?,?,?)
                        """,i)
                    showinfo('Success','Running Added Successfully.')
                    con.commit()
                    add(0)
                else:
                    try:
                        cur.execute('delete from running where b_id=? and r_id=? and r_date=?',(bid,rid,d))
                        showinfo('Success','Running Deleted Successfully.')
                        con.commit()
                    except:
                        root.bell()
                        showerror('Error!','Something went wrong')
                        return
                    add(1)

            Label(frame2,text='Bus id: ').grid(row=i,column=0)
            B_id=Entry(frame2)
            B_id.grid(row=i,column=1,padx=(0,20))

            Label(frame2,text='Route id ').grid(row=i,column=3)
            R_id=Entry(frame2)
            R_id.grid(row=i,column=4,padx=(0,20))

            Label(frame2,text='Date of Running: ').grid(row=i,column=5)
            Label(frame2,text='(dd-mm-yyyy)').grid(row=1,column=5)
            R_date=Entry(frame2)
            R_date.grid(row=i,column=6,padx=(0,20))

            Button(frame2,text=str[option],bg='palegreen1',command=new).grid(row=i,column=9,padx=(15,0))


        Label(frame1, image=img).grid(row=0, column=0)
        Label(frame1, text='Online Bus Booking System', font='Arial 20 bold', bg='Light Blue', fg='red').grid(row=1,column=0)
        Label(frame1,text='    Add New Run    ',font='Arial 16 bold',bg='Light Green',fg='Dark green').grid(row=2,column=0,pady=20)

        Button(frame3,text='Add New Run',bg='palegreen1',command=lambda:add(0)).grid(row=0,column=1,pady=20,padx=30)
        Button(frame3,text='Delete Exising Run',bg='palegreen1',command=lambda:add(1)).grid(row=0,column=2,pady=20,padx=30)

        Button(root,image=home,command=GotoHome).grid(row=3,column=0)

        root.mainloop()

#################################################################################################################################
#****
    def AddRoute(self):
        root = Tk()
        h, w = root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0' % (w, h))

        try:
            img = PhotoImage(file='.//resourses/Bus_for_project.png')
            home = PhotoImage(file='.//resourses/home.png')
        except:
            img = PhotoImage(file='.\\resourses\Bus_for_project.png')
            home = PhotoImage(file='.\\resourses\home.png')

        root.columnconfigure(0, weight=1)

        frame1 = Frame(root)
        frame1.grid(row=0, column=0)
        frame2 = Frame(root)
        frame2.grid(row=1, column=0)
        frame3 = Frame(root)
        frame3.grid(row=3,column=0)
        frame4=Frame(root)
        frame4.grid(row=2,column=0)

        def GotoHome():
            root.destroy()
            self.HomePage()
        def proceed():
            try:
                R_id=int(routeid.get())
                cur.execute('select rid from route where rid=?',(R_id,))
                var=cur.fetchall()
                if len(var) !=0:
                    root.bell()
                    showerror('Error!','Route Id already Exist')
                    return
            except :
                root.bell()
                showerror('Error!','Route Id must be Numeric and Can\'t be Empty')
                return
            frame2.destroy()
            Label(frame4,text='Add Bus Stations',font='Arial 17 bold',fg='Red').grid(row=1,column=1,pady=10)
            Label(frame3,text='Station No.',font='Arial 15 bold').grid(row=0,column=1)
            Label(frame3,text='Station Name',font='Arial 15 bold').grid(row=0,column=2,padx=150)
            Label(frame3,text='Distance',font='Arial 15 bold').grid(row=0,column=3)
            #Label(frame3,text='Basic Fare',font='Arial 15 bold').grid(row=0,column=4,padx=70)

            def done():
                root.destroy()
                self.AddRoute()
            def add(j):
                def exe():
                    entry=(Sname.get(),Sdis.get())
                    for c in entry:
                        if len(c) ==0:
                            root.bell()
                            showerror("Error!",'All fields are Required')
                            return
                    try:
                        dis=int(entry[1])
                        if dis < 0 :
                            raise ValueError()
                    except:
                        root.bell()
                        showerror('Error!','Distance must be Numeric and Positive')
                        return
                    cur.execute('insert into route(rid,sid,s_name,b_fare,distance) values(?,?,?,?,?)',(R_id,j,entry[0],entry[1],entry[1]))
                    con.commit()
                    showinfo('Successfull','Route Added Successfully')
                    add(j+1)

                Label(frame3,text=str(j)+'.',font='Arial 12 bold').grid(row=j,column=1)
                Sname=Entry(frame3)
                Sname.grid(row=j,column=2)
                Sdis=Entry(frame3)
                Sdis.grid(row=j,column=3)
                #Sfare=Entry(frame3)
                #Sfare.grid(row=j,column=4)
                Button(frame3,text='  Add  ',font='Arial 12 bold',command=exe).grid(row=j,column=5,padx=30)

            i=1
            add(i)
            Label(root,text='NOTE: Distance is from 1st station to current station and Distance of 1st station must be 0',font='Arial 13 italic ').grid(row=4,column=0,pady=20)
            Button(root,text='    Done    ',font='Arial 12 bold',bg='green',command=done).grid(row=5,column=0)

        Label(frame1, image=img).grid(row=0, column=0)
        Label(frame1, text='Online Bus Booking System', font='Arial 20 bold', bg='Light Blue', fg='red').grid(row=1,column=0)
        Label(frame1,text='Add New Route',font='Arial 16 bold',bg='Light Green',fg='Dark green').grid(row=2,column=0,pady=20)
        Label(frame2,text='Create Route Id: ',font='Arial 12 bold').grid(row=0,column=0)
        routeid=Entry(frame2)
        routeid.grid(row=0,column=1)
        Button(frame2,text='Proceed',command=proceed).grid(row=0,column=2,padx=20)
        Button(root,image=home,command=GotoHome).grid(row=6,column=0,pady=20)
        root.mainloop()

######################################################################################################################################
#******
    def AddBus(self,opid):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        try:
            img=PhotoImage(file='.//resourses/Bus_for_project.png')
            home=PhotoImage(file='.//resourses/home.png')
        except:
            img=PhotoImage(file='.\\resourses\Bus_for_project.png')
            home=PhotoImage(file='.\\resourses\home.png')

        root.columnconfigure(0,weight=1)

        frame1=Frame(root)
        frame1.grid(row=0,column=0)
        frame2=Frame(root)
        frame2.grid(row=1,column=0)

        frame3=Frame(root)
        frame3.grid(row=2,column=0)
        def GotoHome():
            root.destroy()
            self.HomePage()

        Label(frame1,image=img).grid(row=0,column=0)
        Label(frame1,text='Online Bus Booking System',font='Arial 20 bold',bg='Light Blue',fg='red').grid(row=1,column=0)
        Label(frame1,text='    Add Bus    ',font='Arial 16 bold',bg='light green',fg='dark green').grid(row=2,column=0,pady=20)

        def delete():
            def dlt():
                try:
                    bus_id=int(busid.get())
                    cur.execute('select bid from bus where op_id=? and bid=?',(opid,bus_id))
                    chk=cur.fetchall()
                    if len(chk) :
                        root.bell()
                        showerror('Error!','Bus Id not belongs to you')
                        return
                    ans=askyesno('Confirmation','Do you really want to Delete ')
                    if ans:
                        cur.execute('delete from bus where bid=? ',(bus_id,))
                        showinfo('Confirmation','Bus Deleted successfully')
                        con.commit()
                    else:
                        root.destroy()
                        self.AddBus()
                except:
                    root.bell()
                    showerror('Error!','Invalid Bus Id')
                    return

            frame3.destroy()
            frame4=Frame(root)
            frame4.grid(row=1,column=0)

            Label(frame4,text='Enter Bus Id: ').grid(row=0,column=0,pady=30,padx=30)
            busid=Entry(frame4)
            busid.grid(row=0,column=1,pady=30,padx=30)
            Button(frame4,text='Delete',bg='palegreen1',command=dlt).grid(row=0,column=2,padx=30,pady=30)


        def add():
            frame3.destroy()
            i=0
            def new():
                try:
                    Bid=int(B_id.get())
                except:
                    root.bell()
                    showerror('Error!','Invalid Bus Id')
                    return

                type=bus_type.get()
                cap=0
                if type == 'Bus Type':
                    root.bell()
                    showerror('Error!','Select Bus Type')
                    return
                else:
                    if type == 'AC 2X2' or type == 'Non AC 2X2':
                        cap+=28
                    if type == 'AC 3X2' or type =='Non AC 3X2':
                        cap+=40
                com=B_company.get()
                try:
                    if len(B_fare.get()) == 0:
                        fare=0
                    else:
                        fare=int(B_fare.get())
                        if fare<0:
                            root.bell()
                            showerror('Error!','Luxury Fare can\'t be Negative')
                            return
                except:
                    root.bell()
                    showerror('Error!','Luxury Fare must be numeric')
                    return

                try:
                    cur.execute('insert into bus(bid,type,capacity,company,lfare,op_id) values(?,?,?,?,?,?)',(Bid,type,cap,com,fare,opid))
                except:
                    root.bell()
                    showerror('Error!','Bus Id Already Exist')
                    return
                showinfo('Confirmation','Bus with Id %d  has added successfully'%Bid)
                add()
                con.commit()

            Label(frame2,text='Bus id: ').grid(row=i,column=0,pady=20)
            B_id=Entry(frame2)
            B_id.grid(row=i,column=1,pady=20)

            bus_type=StringVar()
            bus_type.set('Bus Type')
            option=['AC 2X2','AC 3X2','Non AC 2X2','Non AC 3X2']
            d_menu=OptionMenu(frame2,bus_type, *option)
            d_menu.grid(row=i,column=2,padx=20,pady=20)

            Label(frame2,text='Company: ').grid(row=i,column=5,pady=20)
            B_company=Entry(frame2)
            B_company.grid(row=i,column=6,padx=(0,20),pady=20)
            Label(frame2,text='Luxury Fare: ').grid(row=i,column=7,pady=20)
            B_fare=Entry(frame2)
            B_fare.grid(row=i,column=8,pady=20)
            Button(frame2,text='Add',bg='palegreen1',command=new).grid(row=i,column=9,padx=(15,0),pady=20)


        Button(frame3,text='Add New Bus',bg='palegreen1',command=add).grid(row=0,column=1,pady=20,padx=30)
        Button(frame3,text='Delete Exising Bus',bg='palegreen1',command=delete).grid(row=0,column=2,pady=20,padx=30)
        Button(root,image=home,command=GotoHome).grid(row=6,column=0,pady=50)
        root.mainloop()


######################################################################################################################################
#****
    def AddOperator(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        try:
            img=PhotoImage(file='.//resourses/Bus_for_project.png')
            home=PhotoImage(file='.//resourses/home.png')
        except:
            img=PhotoImage(file='.\\resourses\Bus_for_project.png')
            home=PhotoImage(file='.\\resourses\home.png')

        root.columnconfigure(0,weight=1)

        frame1=Frame(root)
        frame1.grid(row=0,column=0)
        frame2=Frame(root)
        frame2.grid(row=1,column=0,pady=20)
        frame3=Frame(root,relief='groove',bd=3,padx=10,pady=10)
        frame3.grid(row=1,column=0)

        def GotoHome():
            root.destroy()
            self.HomePage()

        def add(i,m=-10):
            def proceed():
                if i==-2:
                    entry=(Pass.get(),Oname.get(),Oemail.get(),Oadd.get())
                    for j in entry:
                        if len(j)==0:
                            root.bell()
                            showerror('Error!','All fields are mandatory')
                            return
                    try:
                        o_id=int(Oid.get())
                        if o_id<1:
                            root.bell()
                            showerror('Error!','Operator Id must be positive')
                            return
                        o_ph=(Oph.get())
                        if len(o_ph) != 10 :
                            root.bell()
                            showerror('Error!','Enter valid Phone Number')
                            return
                        ph=int(Oph.get())
                    except:
                        root.bell()
                        showerror('Error!','Operator Id & Phone Number must be numeric')
                        return
                    try:
                        entry=entry+(o_id,ph)
                        cur.execute('insert into operator(password,name,email,address,opid,phno) values(?,?,?,?,?,?)',entry)
                    except:
                        root.bell()
                        showinfo('Error!','Operator Id already Exist')
                        return
                    con.commit()
                    showinfo('Added',"Operator Added Successfully")
                    root.destroy()
                    self.AddOperator()
                else:
                    u_id=Oid.get()
                    u_pass=Pass.get()
                    u_name=Oname.get()
                    u_ph=Oph.get()
                    u_email=Oemail.get()
                    u_add=Oadd.get()
                    if len(u_id) != 0:
                        try:
                            try:
                                check=int(u_id)
                            except:
                                root.bell()
                                showerror('Error!','Operator Id must be numeric')
                                return
                            if int(u_id) >0:
                                cur.execute('update operator set opid=? where opid=?',(u_id,m))
                            else:
                                root.bell()
                                showerror('Error!','Operator Id must be positive')
                                return
                        except:
                            root.bell()
                            showerror('Error!','Operator Id already Exist')
                    if len(u_pass) !=0:
                        cur.execute('update operator set password=? where opid=?',(u_pass,m))
                    if len(u_name) !=0:
                        cur.execute('update operator set name=? where opid=?',(u_name,m))
                    if len(u_ph) !=0:
                        try:
                            p=int(u_ph)
                            if len(u_ph)==10:
                                cur.execute('update operator set phone=? where opid=?',(u_ph,m))
                            else:
                                root.bell()
                                showerror('Error!','Enter valid Phone Number')
                        except:
                            root.bell()
                            showerror('Error!','Phone Number must be numeric')
                    if len(u_email) !=0:
                        cur.execute('update operator set email=? where opid=?',(u_email,m))
                    if len(u_add) !=0:
                        cur.execute('update operator set address=? where opid=?',(u_add,m))
                    showinfo('Success',"Edit Successfull")
                    self.AddOperator()
                    con.commit()


            frame2.destroy()
            txt=('Create ','Change ')
            Label(frame3,text=txt[i]+'Operator Id:').grid(row=0,column=0)
            Oid=Entry(frame3)
            Oid.grid(row=0,column=1)
            Label(frame3,text=txt[i]+'Password:').grid(row=1,column=0)
            Pass=Entry(frame3)
            Pass.grid(row=1,column=1)
            Label(frame3,text='Name:').grid(row=2,column=0)
            Oname=Entry(frame3)
            Oname.grid(row=2,column=1)
            Label(frame3,text='Phone:').grid(row=3,column=0)
            Oph=Entry(frame3)
            Oph.grid(row=3,column=1)
            Label(frame3,text='Email:').grid(row=4,column=0)
            Oemail=Entry(frame3)
            Oemail.grid(row=4,column=1)
            Label(frame3,text='Address:').grid(row=5,column=0)
            Oadd=Entry(frame3)
            Oadd.grid(row=5,column=1)
            Button(frame3,text='Proceed',command=proceed).grid(row=6,column=1)

        def edit(temp):
            def done():
                try:
                    oid=int(Oid.get())
                    pas=Pass.get()
                    cur.execute('select opid from operator where opid=? and password=?',(oid,pas))
                    var=cur.fetchall()
                    k=int(var[0][0])
                except:
                    showerror('Error!','Sorry, your username or password was incorrect. Please double-check it.')
                    return
                if len(var)==0:
                    showerror('Error!','Sorry, your username or password was incorrect. Please double-check it.')
                    return
                if temp == 1:
                    add(1,k)
                else:
                    answer=askyesno('Confirmation','This action will Delete all Buses associated with you . Are you sure ?')
                    if answer:
                        cur.execute('delete from operator where opid=?',(k,))
                        con.commit()
                        showinfo('Success','Operator Deleted Successfully')
                    else:
                        return
            frame2.destroy()

            Label(frame3,text='Enter Operator id:').grid(row=0,column=0)
            Oid=Entry(frame3)
            Oid.grid(row=0,column=1)
            Label(frame3,text='Enter Password:').grid(row=1,column=0)
            Pass=Entry(frame3,show='*')
            Pass.grid(row=1,column=1)
            Button(frame3,text='Proceed',command=done).grid(row=2,column=1)

        Label(frame1,image=img).grid(row=0,column=0)
        Label(frame1,text='Online Bus Booking System',font='Arial 20 bold',bg='Light Blue',fg='red').grid(row=1,column=0)
        Label(frame1,text='Operator Details',font='Arial 16 bold',bg='light green',fg='dark green').grid(row=2,column=0,pady=20)
        Button(frame2,text='Add New Operator',font='Arial 14 bold',bg='tan1',command=lambda:add(-2)).grid(row=3,column=0,pady=20,padx=5)
        Button(frame2,text='Edit Operator',font='Arial 14 bold',bg='tan1',command=lambda:edit(1)).grid(row=3,column=1,pady=20,padx=5)
        Button(frame2,text='Delete Operator',font='Arial 14 bold',bg='tan1',command=lambda:edit(2)).grid(row=3,column=2,pady=20,padx=5)

        Button(root,image=home,command=GotoHome).grid(row=3,column=0)

        root.mainloop()

##############################################################################################################################
#****
    def OperatorLogin(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        try:
            img=PhotoImage(file='.//resourses/Bus_for_project.png')
            home=PhotoImage(file='.//resourses/home.png')
        except:
            img=PhotoImage(file='.\\resourses\Bus_for_project.png')
            home=PhotoImage(file='.\\resourses\home.png')

        root.columnconfigure(0,weight=1)

        frame1=Frame(root)
        frame1.grid(row=0,column=0)
        frame2=Frame(root)
        frame2.grid(row=1,column=0)
        frame3=Frame(root,relief="groove",bd=3,padx=10,pady=5)
        frame3.grid(row=2,column=0,pady=15)
        def NewOperator():
            root.destroy()
            self.AddOperator()

        def login(select):
            def page():
                user=opid.get()
                password=passw.get()
                try:
                    cur.execute('select opid from operator where opid=? and password=?',(user,password))
                    var=cur.fetchall()
                    if len(var) == 0:
                        root.bell()
                        showerror("Error!",'Sorry, your username or password was incorrect. Please double-check it.')
                        return
                    var1=var[0][0]
                except:
                    root.bell()
                    showerror("Error!",'Sorry, your username or password was incorrect. Please double-check it.')
                    return
                root.destroy()
                if select==1:
                    self.AddBus(var1)
                elif select==2:
                    self.AddRoute()
                else :
                    self.AddRun(var1)

            Label(frame3,text='Username : ').grid(row=0,column=0)
            opid=Entry(frame3)
            opid.grid(row=0,column=1)
            Label(frame3,text='Password : ').grid(row=1,column=0)
            passw=Entry(frame3,show='*')
            passw.grid(row=1,column=1)
            Button(frame3,text='Login',command=page).grid(row=2,column=1)

        def GotoHome():
            root.destroy()
            self.HomePage()

        Label(frame1,image=img).grid(row=0,column=0)
        Label(frame1,text='Online Bus Booking System',font='Arial 20 bold',bg='Light Blue',fg='red').grid(row=1,column=0)
        Label(frame1,text='Add New Database',font='Arial 16 bold',bg='light green',fg='dark green').grid(row=2,column=0,pady=20)

        Button(frame2,text='New Operator',command=NewOperator).grid(row=0,column=0)
        Button(frame2,text='New Bus',bg='gainsboro',command=lambda:login(1)).grid(row=0,column=1,padx=10)
        Button(frame2,text='New Route',command=lambda:login(2)).grid(row=0,column=2)
        Button(frame2,text='New Run',bg='gainsboro',command=lambda:login(3)).grid(row=0,column=3,padx=10)
        Button(root,image=home,command=GotoHome).grid(row=3,column=0)
        root.mainloop()

##############################################################################################################################
    def BookingStatus(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        try:
            img=PhotoImage(file='.//resourses/Bus_for_project.png')
            home=PhotoImage(file='.//resourses/home.png')
        except:
            img=PhotoImage(file='.\\resourses\Bus_for_project.png')
            home=PhotoImage(file='.\\resourses\home.png')

        root.columnconfigure(0,weight=1)

        frame1=Frame(root)
        frame1.grid(row=0,column=0)
        frame2=Frame(root)
        frame2.grid(row=1,column=0)
        def GotoHome():
            root.destroy()
            self.HomePage()
        def search():
            q=1
            try:
                ph=go.get()
                if len(ph) != 10 :
                    root.bell()
                    showerror('Error!','Invalid Phone Number ')
                    return
                p=int(ph)
            except:
                root.bell()
                showerror('Error!','Invalid Phone Number')
                return

            cur.execute('select t_phone from travelers where t_phone=?',(p,))
            var=cur.fetchall()

            if len(var) !=0:
                root.destroy()
                self.Confirmation(p)
            else:
                root.bell()
                showerror('Not Found','No Booking Found')
                return
        Label(frame1,image=img).grid(row=0,column=0)
        Label(frame1,text='Online Bus Booking System',font='Arial 20 bold',bg='Light Blue',fg='red').grid(row=1,column=0)
        Label(frame1,text='Booking\'s Deatails',font='Arial 16 bold',bg='light green',fg='dark green').grid(row=2,column=0,pady=20)

        Label(frame2,text='Mobile No: ').grid(row=0,column=0,pady=30)
        go=Entry(frame2)
        go.grid(row=0,column=1,padx=(5,20),pady=30)
        Button(frame2,text='Status',bg='gainsboro',command=search).grid(row=0,column=2,padx=20,pady=30)
        Button(root,image=home,command=GotoHome).grid(row=2,column=0,pady=20)
        root.mainloop()

##############################################################################################################################
    def BookSeat(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        try:
            img=PhotoImage(file='.//resourses/Bus_for_project.png')
            home=PhotoImage(file='.//resourses/home.png')
        except:
            img=PhotoImage(file='.\\resourses\Bus_for_project.png')
            home=PhotoImage(file='.\\resourses\home.png')

        root.columnconfigure(0,weight=1)

        frame1=Frame(root)
        frame1.grid(row=0,column=0)
        frame2=Frame(root)
        frame2.grid(row=1,column=0)
        frame3=Frame(root)
        frame3.grid(row=2,column=0)
        frame4=Frame(root)
        frame4.grid(row=2,column=0)
        frame5=Frame(root)
        frame5.grid(row=3,column=0)
        frame6=Frame(root,relief="groove")
        frame6.grid(row=0,column=1,padx=(0,50))
        frame7=Frame(root,relief='groove',bd=3)
        frame7.grid(row=0,column=2)


        Label(frame1,image=img).grid(row=0,column=0)
        Label(frame1,text='Online Bus Booking System',font='Arial 20 bold',bg='Light Blue',fg='red').grid(row=1,column=0)
        Label(frame1,text='Enter Journey Details',font='Arial 16 bold',bg='light green',fg='dark green').grid(row=2,column=0,pady=20)
        def GotoHome():
            root.destroy()
            self.HomePage()


        def search():
            def book(op,available_seats):
                src_sid=int(sid[op])        #//
                des_sid=int(dest_sid[op])   #//
                print(src_sid)
                total_fare=int(var2[op][0][4]+dis[op])
                brd=int(var2[op][0][5])
                cap=var2[op][0][3]      #//

                def proceed():
                    try:
                        ph=phone.get()
                        if len(ph) != 10 :
                            root.bell()
                            showerror('Error!','Invalid Phone Number ')
                            return
                        p=int(ph)
                    except:
                        root.bell()
                        showerror('Error!','Invalid Phone Number')
                        return
                    try:
                        cur.execute("""insert into travelers(t_phone,t_source,t_destination,t_brd) values(?,?,?,?) """,(p,src,dest,brd))
                        #con.commit()
                    except:
                        root.bell()
                        showerror('Error!','Please Book tickets with different phone , This number is already Exist')
                        return

                    sid_i=src_sid
                    sid_f=des_sid
                    SeatMatrix=0
                    while sid_i < sid_f:
                        cur.execute('select SeatMatrix from seats where s_id=? and b_rd=?',(sid_i,brd))
                        s=int(cur.fetchall()[0][0])
                        SeatMatrix=int(SeatMatrix|s) #//
                        sid_i+=1

                    avl_seat_no=[]  #//

                    if cap==40:
                        counter=0
                        y=0
                        value=0
                        while y<8:
                            x=0
                            Label(root,text="Seat Matrix").grid(row=1,column=1,padx=(0,50))
                            while x<5:
                                fill=SeatMatrix&(2**value)
                                if fill==0:
                                    Label(frame6,text=value+1).grid(row=y+1,column=x,padx=(0,10))
                                    avl_seat_no.append(value+1)
                                else:
                                    Label(frame6,text=value+1,bg='red').grid(row=y+1,column=x,padx=(0,10))
                                x+=1
                                counter+=1
                                value+=1
                            y+=1
                            counter+=1

                    if cap==28:
                        counter=0
                        y=0
                        value=0
                        while y<7:
                            x=0
                            Label(root,text="Seat Matrix").grid(row=1,column=1,padx=(0,50))
                            while x<4:
                                fill=SeatMatrix&(2**value)
                                if fill==0:
                                    Label(frame6,text=value+1).grid(row=y+1,column=x,padx=(0,10))
                                    avl_seat_no.append(value+1)
                                else:
                                    Label(frame6,text=value+1,bg='red').grid(row=y+1,column=x,padx=(0,10))
                                x+=1
                                counter+=1
                                value+=1
                            y+=1
                            counter+=1


                    select=[]
                    def addmore(j):
                        if j+1 > available_seats:
                            root.bell()
                            showerror('','More seats are not available')
                            return

                        def done(kar):
                            a=1
                            cus_name=Name.get()
                            if len(cus_name) ==0 :
                                root.bell()
                                showerror('Error!','Name Field is Required')
                                return
                            try:
                                sno=int(seat_no.get())
                                if j==0:
                                    select.append(sno)
                                if sno in avl_seat_no:
                                    iiohu=0
                                else:
                                    root.bell()
                                    showerror('Error!','Seat Number is Not Available')
                                    return
                            except:
                                root.bell()
                                showerror('Error!','Invalid Seat Number')
                                return

                            cus_gender=gender.get()
                            if len(cus_gender) ==0 :
                                root.bell()
                                showerror('Error!','Select Your Gender ')
                                return

                            if kar==0:
                                if j!=0 :
                                    if sno in select:
                                        root.bell()
                                        showerror('Error!','You Already selected this seat')
                                        return
                                    else:
                                        select.append(sno)
                                cur.execute("""insert into t_details(t_name,t_gender,t_phonenumber,t_seat) values(?,?,?,?)""",(cus_name,cus_gender,p,sno))
                                showinfo('Confirmation','Added successfully')
                                #con.commit()

                            if kar==1:
                                count=j+1
                                fare=total_fare*count
                                ans=askyesno('Confirmation','Total Fare is %d , Do you want to proceed'%(fare,))

                                if ans:
                                    update_counter=[]
                                    cur.execute('select counter from seats where b_rd=? and s_id>=? and s_id<? ',(brd,src_sid,des_sid))
                                    v=cur.fetchall()
                                    for ucount in v:
                                        update_counter.append(int(ucount[0])-count)


                                    cur.execute(""" update travelers set num_seats=?,t_fare=?""",(count,fare))
                                    #con.commit()
                                    update_seat=SeatMatrix
                                    seat_mat=0
                                    for upd in select:
                                        update_seat=update_seat|(2**int(upd-1))
                                    s_src=int(src_sid)
                                    c=0
                                    while s_src < des_sid :
                                        cur.execute("""update seats set SeatMatrix=? ,counter=? where b_rd=? and s_id=? """,(update_seat,update_counter[c],brd,s_src))
                                        s_src+=1
                                        c+=1
                                    con.commit()

                                else:
                                    root.destroy()
                                    self.BookSeat()

                                root.destroy()
                                self.Confirmation()

                        Label(frame5,text='Name: ',font='Arial 13').grid(row=j,column=0,pady=(20,0))
                        Name=Entry(frame5)
                        Name.grid(row=j,column=1,padx=(0,30),pady=(20,0))
                        Label(frame5,text='Gender: ',font='Arial 13').grid(row=j,column=2,pady=(20,0))
                        gender=StringVar()
                        Radiobutton(frame5,text='Male',variable=gender,value='1').grid(row=j,column=3,pady=(20,0))
                        Radiobutton(frame5,text='Female',variable=gender,value='2').grid(row=j,column=4,padx=(0,20),pady=(20,0))
                        Label(frame5,text='Enter Seat no. : ',font='Arial 13').grid(row=j,column=5,pady=(20,0))
                        seat_no=Entry(frame5)
                        seat_no.grid(row=j,column=6,padx=(0,30),pady=(20,0))
                        Button(frame5,text=' Add ',command=lambda:done(0)).grid(row=j,column=7,pady=(20,0),padx=20)
                        Button(frame5,text='Add More Passanger',command=lambda:addmore(j+1)).grid(row=0,column=8,pady=(20,0))
                        Button(root,text='Done',command=lambda:done(1)).grid(row=4,column=0,pady=(20,0))

                    addmore(0)

                frame2.destroy()
                frame3.destroy()
                Label(root,text='              Fill Your Details              ',font='Arial 14 bold',fg='red',bg='light Blue').grid(row=1,column=0,pady=20)
                Button(root,image=home,command=GotoHome).grid(row=6,column=0,pady=30)
                Label(frame4,text='Enter Phone Number: ',font='Arial 13').grid(row=0,column=0)
                phone=Entry(frame4)
                phone.grid(row=0,column=1,padx=(0,20))
                Button(frame4,text='Proceed',command=proceed).grid(row=0,column=5,padx=(50,0))
        #############################################################
            src=source.get()
            if len(src) == 0:
                root.bell()
                showerror('Error!','Enter your Boarding')
                return
            dest=destination.get()
            if len(dest) == 0:
                root.bell()
                showerror('Error!','Enter your Destination')
                return
            d=Date.get()
            date=d.split("-")
            try:
                day=int(date[0])
                month=int(date[1])
                year=int(date[2])
                if len(date) != 3:
                    raise
                if year < 2022 or month > 12 or day > 31:
                    raise
            except:
                root.bell()
                showerror('Error!','Invalid Date ')
                return

            cur.execute('select rid,sid,s_name,distance from route  where s_name=? or s_name=? ',(src,dest))
            var=cur.fetchall()
            rid=[]
            sid=[]
            dest_sid=[]
            dis=[]
            temp=1
            for i in var:
                if temp >= len(var):
                    break
                if i[0]==var[temp][0]:
                    if i[2]==src:
                        rid.append(i[0])
                        sid.append(i[1])
                        dis.append((int(var[temp][3])-int(i[3])))
                        dest_sid.append(var[temp][1])
                temp+=1

            n=len(rid)
            var2=[]
            Available=[] #available seats
            i=0
            while i<n:
                cur.execute("""select name,type,company,capacity,lfare,brd from operator,bus,running,seats where opid=op_id and bid=b_id and r_id=? and r_date=? and brd=b_rd and s_id=?""",(rid[i],d,sid[i]))
                var2.append(cur.fetchall())
                try:
                    cur.execute("""select counter from  seats where b_rd=? and s_id>=? and s_id <? """,(var2[i][0][5],sid[i],dest_sid[i]))
                    temp_seat=(cur.fetchall())
                    a=var2[i][0][3]
                    for value  in  temp_seat:
                        if int(value[0])<int(a):
                            a=int(a)-(int(a)- int(value[0]))
                        Available.append(a)
                except:
                    kjkjkjkjkkj=0
                i+=1
            print(Available)
            Label(frame3,text='Operator',font='Arial 15 bold',fg='green').grid(row=0,column=0,padx=(0,100),pady=(20))
            Label(frame3,text='Bus Type',font='Arial 15 bold',fg='green').grid(row=0,column=1,padx=(0,100))
            Label(frame3,text='Company',font='Arial 15 bold',fg='green').grid(row=0,column=2)
            Label(frame3,text='Available Seats',font='Arial 15 bold',fg='green').grid(row=0,column=3,padx=(100,0))
            Label(frame3,text='Fare',font='Arial 15 bold',fg='green').grid(row=0,column=4,padx=(100,0))
            Label(frame3,text='   ',font='Arial 15 bold',fg='green').grid(row=0,column=5,padx=(100,0))

            l=len(var2)
            def list(i,k):
                if i >= l:
                    return

                if len(var2[i])!=0:
                    Label(frame3,text=var2[i][0][0],font='Arial 14').grid(row=i+1,column=0,padx=(0,100))
                    Label(frame3,text=var2[i][0][1],font='Arial 14').grid(row=i+1,column=1,padx=(0,100))
                    Label(frame3,text=var2[i][0][2],font='Arial 14').grid(row=i+1,column=2)
                    Label(frame3,text=Available[k],font='Arial 14').grid(row=i+1,column=3,padx=(100,0))
                    Label(frame3,text=var2[i][0][4]+dis[i],font='Arial 14').grid(row=i+1,column=4,padx=(100,0))
                    Label(frame3,text='    ',font='Arial 14').grid(row=i+1,column=5,padx=(100,0))
                    Button(frame3,text='Book',command=lambda:book(i,Available[k-1])).grid(row=i+1,column=6)
                    k+=1
                list(i+1,k)

            list(0,0)
        Label(frame2,text='From: ').grid(row=0,column=0)
        source=Entry(frame2)
        source.grid(row=0,column=1,padx=(0,30))
        Label(frame2,text='To: ').grid(row=0,column=2)
        destination=Entry(frame2)
        destination.grid(row=0,column=3,padx=(0,30))
        Label(frame2,text='Date: ').grid(row=0,column=4)
        Label(frame2,text='(dd-mm-yyyy)').grid(row=1,column=5,padx=(0,30))
        Date=Entry(frame2)
        Date.grid(row=0,column=5,padx=(0,30))
        Button(frame2,text='Search',bg='gainsboro',command=search).grid(row=0,column=6,padx=30)

        Button(frame2,image=home,command=GotoHome).grid(row=0,column=7)
        root.mainloop()

###############################################################################################################################
#****
    def HomePage(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        try:
            img=PhotoImage(file='.\\resourses\Bus_for_project.png')
        except:
            img=PhotoImage(file='.//resourses/Bus_for_project.png')

        root.columnconfigure(0,weight=3)
        root.columnconfigure(1,weight=4)
        root.columnconfigure(2,weight=3)

        Label(root,image=img).grid(row=0,column=1)
        Label(root,text='Online Bus Booking System',font='Arial 20 bold',bg='Light Blue',fg='Red').grid(row=1,column=1)

        def init():
            root.destroy()
            self.BookSeat()
        def status():
            root.destroy()
            self.BookingStatus()
        def add():
            root.destroy()
            self.OperatorLogin()

        Button(root,text='Seat Booking',font='Arial 14 bold',command=init).grid(row=2,column=0,pady=20)
        Button(root,text='Booking Status',font='Arial 14 bold',command=status).grid(row=2,column=1)
        Button(root,text='Add Bus Details',font='Arial 14 bold',command=add).grid(row=2,column=2)
        Label(root,text='Admins Only',font='Arial 12 bold',fg='Red').grid(row=3,column=2)
        root.mainloop()

##############################################################################################################################
#****
    def IntroPage(self):
        root=Tk()
        h,w=root.winfo_screenheight(),root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
        #root.config(background='White')

        try:
            img=PhotoImage(file='.\\resourses\Bus_for_project.png')
        except:
            img=PhotoImage(file='.//resourses/Bus_for_project.png')

        root.grid_columnconfigure(0, weight=1)

        Bus=Label(root,image=img).grid(row=0,column=0)
        label=Label(root,text="Online Bus Booking System",font='Arial 20 bold',bg='light blue',fg='Red')
        label.grid(row=1,column=0)

        Label(root,text='Name : Samarth Jain',fg='Blue',font='Arial 14').grid(row=3,column=0,pady=20)
        Label(root,text='Er : 211B267',fg='Blue',font='Arial 14').grid(row=4,column=0)
        Label(root,text='Mobile : 7225036054',fg='Blue',font='Arial 14').grid(row=5,column=0,pady=20)

        Label(root,text="Submitted To : Dr. Mahesh Kumar",font='Arial 16 bold',bg='light blue',fg='Red').grid(row=6,column=0)
        Label(root,text='Project Based Learning',fg='Red',font="Arial 13 bold").grid(row=7,column=0,pady=10)
        def fun(m=0):
            root.destroy()
            self.HomePage()

        root.bind('<KeyPress>',fun)
        root.mainloop()

##############################################################################################################################
book=python_bus()
book.HomePage()
