import sqlite3
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
class app:
    def __init__(self,root):
        self.wim()
        self.login()

    def wim(self):                                                      #window screen
        self.w= root.winfo_screenwidth()
        self.h= root.winfo_screenheight()
        root.geometry("%dx%d" % (self.w,self.h))
        root.configure(bg="white")
        root.wm_state('zoomed')

    #--------------------------------------------#destroying function#-------------------------------------------
    
    def logoutd(self):
        self.fnew.destroy()
        self.login()
    
    
    def canceld(self):
        self.fnew.destroy()
        self.fstrt.destroy()

    #--------------------------------------------#destroying function#-------------------------------------------
    
    #def scrchdel(self):
    #    self.escrh.delete("end")
        
    #-----------------------------------------------#login function#-------------------------------------------
    
    def login(self):
        self.flg=Frame(root,width=self.w,height=self.h,bg="white")
        self.flg.place(x=0,y=0)
        self.flgg=Frame(self.flg,width=self.w,height=60,bg="black")
        self.flgg.place(x=0,y=70)
        self.ltit=Label(self.flg,text="Mxcel",fg="black",font=("December Reaper",25),bg="white")
        self.ltit.place(x=43,y=20)
        self.lsuph=Label(self.flg,text="Admin Login",fg="white",bg="black",font=("Arial Black",10))
        self.lsuph.place(x=50,y=87)
        self.lsup=Label(self.flg,text="| Supplier",fg="grey",bg="white")
        self.lsup.place(x=120,y=30)
        
        self.lg=PhotoImage(file="login page.png")
        self.lgb=PhotoImage(file="lgbox.png")
        self.lgin=PhotoImage(file="login.png")
        self.des1=PhotoImage(file="des1.png")
        self.des2=PhotoImage(file="des2 .png")
        
        self.ldes1=Label(self.flg,image=self.des1,bg="white")
        self.ldes1.place(x=-20,y=620)
        
        self.ldes2=Label(self.flg,image=self.des2,bg="white")
        self.ldes2.place(x=900,y=280)

        self.llg=Label(self.flg,image=self.lg,bg="white")
        self.llg.place(x=470,y=190)
        
        self.llgb1=Label(self.flg,image=self.lgb,bg="#f3f3f3")
        self.llgb1.place(x=535,y=400)
        self.llgb2=Label(self.flg,image=self.lgb,bg="#f3f3f3")
        self.llgb2.place(x=535,y=470)
        
        self.len=Label(self.flg,text="Enter Admin Id",fg="grey",font=("Calibri",10,"italic"))
        self.len.place(x=547,y=380)
        self.een=Entry(self.flg,width=22,bg="white",bd=0,fg="teal",font=("Calibri",12,"italic"))
        self.een.place(x=555,y=413)
        self.een.focus_set()

        self.lp=Label(self.flg,text="Admin Password",fg="grey",font=("Calibri",10,"italic"))
        self.lp.place(x=547,y=450)
        self.een=Entry(self.flg,width=22,bg="white",bd=0,fg="teal",font=("Calibri",12,"italic"),show="*")
        self.een.place(x=555,y=483)

        self.blg=Button(self.flg,image=self.lgin,bg="#f3f3f3",bd=0,command=self.startupscreen)
        self.blg.place(x=595,y=520)

    #--------------------------------------------#login function#-------------------------------------------
    
    #--------------------------------------------#Top Screen for New supplier function#-------------------------------------------

    def strttpscrnnew(self):
        self.fstrt=Frame(root,width=200,height=30,bg="black")
        self.fstrt.place(x=165,y=88)                                               #Top screen for New
        self.lne=Label(self.fstrt,text=">",fg="white",bg="black",font=10).place(x=0,y=0)
        self.lne=Label(self.fstrt,text="New Supplier",fg="cyan",bg="black",font=("Arial Black",10)).place(x=20,y=0)
        
    #--------------------------------------------#Top Screen for New supplier function#-------------------------------------------
    
    #--------------------------------------------#Save function#-------------------------------------------
    def save_fun(self):             
        self.id=self.esupid.get()
        self.name=self.esupname.get()
        self.cname=self.econname.get()
        self.dnost=self.eaddress.get()
        self.area=self.ecity.get()
        self.dis=self.edis.get()
        self.pin=self.epin.get()
        self.lm=self.elam.get()
        self.phno1=self.eph1.get()
        self.phno2=self.eph2.get()
        self.email=self.eemails.get()
        self.gstno=self.egs.get()
        self.actv=self.var.get()
        
        '''
        if(self.cname==""):
            self.econname.configure(highlightbackground="red")
            self.v_cname=Label(self.new_frame,image=self.alert_img,text="Enter Contact name ",fg="red",compound="left").place(x=360,y=80)
            
        else:
            self.en_cn_name.configure(highlightbackground="black")
            self.v_cname=Label(self.new_frame,text="                                                        ",fg="red").place(x=360,y=82)    
        if(self.name==""):
            self.en_name.configure(highlightbackground="red")
            self.v_name=Label(self.new_frame,image=self.alert_img,text="Enter Name",fg="red",compound="left").place(x=70,y=80)
            
        else:
            self.en_name.configure(highlightbackground="black")
            self.v_name=Label(self.new_frame,text="                                   ",fg="red").place(x=70,y=82)
        if((self.en_drno_st=="")or(self.area=="")or(self.dis=="")or(self.lm=="")or(self.pin=="")):
            self.v_address=Label(self.new_frame,image=self.alert_img,text="Fill all the Address Fields",fg="red",compound="left").place(x=90,y=140)
            
        else:
            self.v_address=Label(self.new_frame,text="                                                    ",fg="red").place(x=90,y=142)
        

        


        '''
        if((self.id=="")or(self.name=="")or(self.cname=="")or(self.dnost=="") or (self.area=="") or (self.dis=="") or (self.pin=="") or (self.lm=="") or (self.phno1=="") or (self.phno2=="") or (self.email=="") or (self.gstno=="") or (self.actv=="")):
            self.msg_em=Label(self.new_frame, text="                                                     ",font=('50'),fg="red").place(x=200,y=580)
            self.msg_em=Label(self.new_frame, text="Please fill all the fields.....",font=('50'),fg="red").place(x=200,y=580)
        else:
            try:
                conn = sqlite3.connect('app.db')
                cursor=conn.cursor()
                sql="INSERT INTO Supplier(Sup_ID,Sup_Name,Sup_cname,Sup_drno_st,Sup_area,Sup_tlk_dist,Sup_pincode,Sup_Landmark,Sup_Phone1,Sup_Phone2,Sup_email_ID,Sup_gstin_no,Sup_inactive) Values ("+'"'+str(self.id)+'",'+'"'+self.name+'",'+'"'+self.cname+'",'+'"'+self.dnost+'",'+'"'+self.area+'",'+'"'+self.dis+'",'+'"'+str(self.pin)+'",'+'"'+self.lm+'",'+'"'+str(self.phno1)+'",'+'"'+str(self.phno2)+'",'+'"'+self.email+'",'+'"'+str(self.gstno)+'",'+'"'+str(self.actv)+'"'+")"
                print(sql)
                cursor.execute(sql)
                conn.commit()
                self.instruction =Label(self.fnew, text='New Supplier Added')
                self.instruction.config(font=("Arial black",20))
                self.instruction.place(relx=0.5, rely=0.5, anchor=CENTER)
                self.fnew.destroy()
                self.startupscreen()
            except sqlite3.Error as err:
                print("{}".format("Supplier Allready Exist"))
                self.msg_ee=Label(self.fnew, text="                                                     ",font=('20'),fg="red").place(x=200,y=580)
                self.msg_ee=Label(self.fnew, text="Customer Already Exists....",font=("Arial black",20),fg="Cyan")
                self.msg_ee.place(x=0,y=0)
                conn.rollback()
            cursor.close()
            conn.close()    
    
    #--------------------------------------------#Save function#-------------------------------------------

    #--------------------------------------------#Middle Screen New supplier function#-------------------------------------------
    
    def new(self):                                                          #New supplier screen
        self.strttpscrnnew()
        self.fnew=Frame(root,width=1000,height=550,bg="white")
        self.fnew.place(x=350,y=150)
        self.box=PhotoImage(file="box.png")
        self.adbox=PhotoImage(file="addressbox.png")
        self.boxs=PhotoImage(file="boxs.png")
        self.dt=datetime.datetime.now()
        self.a=self.dt.replace(microsecond=0)
        self.lsupid=Label(self.fnew,text="Supplier ID",font=("Arial black",10),bg="white")
        self.lsupid.place(x=10,y=10)
        self.lsupidp=Label(self.fnew,image=self.box,bg="white")
        self.lsupidp.place(x=0,y=35)
        #self.lid=Label(self.fnew,text="sup"+str(self.a),font=("calibri",12,"italic"),bg="white",fg="teal")
        #self.lid.place(x=30,y=40)
        self.esupid=Entry(self.fnew,width=20,bd=0,font=("calibri",12,"italic"),bg="white",fg="teal")
        self.esupid.place(x=30,y=43)
        self.esupid.insert(0,"sup"+str(self.a))
        self.esupid.config(state="readonly")
        self.lsupname=Label(self.fnew,text="Supplier Name",font=("Arial black",10),bg="white")
        self.lsupname.place(x=300,y=10)
        self.lsupnamep=Label(self.fnew,image=self.box,bg="white")
        self.lsupnamep.place(x=290,y=35)
        self.esupname=Entry(self.fnew,width=30,bd=0,bg="white",fg="teal")
        self.esupname.place(x=310,y=45)
        self.esupname.focus_set()
        self.lconname=Label(self.fnew,text="Contact Person Name",font=("Arial black",10),bg="white")
        self.lconname.place(x=600,y=10)
        self.lconnamep=Label(self.fnew,image=self.box,bg="white")
        self.lconnamep.place(x=590,y=35)
        self.econname=Entry(self.fnew,width=30,bd=0,bg="white",fg="teal")
        self.econname.place(x=610,y=45)
        self.laddress=Label(self.fnew,text="Address Details :",font=("Arial black",10),bg="white")
        self.laddress.place(x=10,y=100)
        self.laddres=Label(self.fnew,image=self.adbox,bg="white")
        self.laddres.place(x=3,y=130)
        self.eaddress=Entry(self.fnew,width=100,bd=0,bg="white",fg="teal")
        self.eaddress.place(x=20,y=140)
        self.laddrc=Label(self.fnew,text="(Address)",fg="grey",bg="white")
        self.laddrc.place(x=5,y=165)
        
        self.lcity=Label(self.fnew,image=self.boxs,bg="white")
        self.lcity.place(x=5,y=185)
        self.ecity=Entry(self.fnew,width=20,bd=0,bg="white",fg="teal")
        self.ecity.place(x=16,y=195)
        self.lcitys=Label(self.fnew,text="(City)",fg="grey",bg="white")
        self.lcitys.place(x=5,y=220)
        
        self.ldis=Label(self.fnew,image=self.boxs,bg="white")
        self.ldis.place(x=165,y=185)
        self.edis=Entry(self.fnew,width=20,bd=0,bg="white",fg="teal")
        self.edis.place(x=175,y=195)
        self.ldist=Label(self.fnew,text="(District)",fg="grey",bg="white")
        self.ldist.place(x=165,y=220)
        
        self.lpin=Label(self.fnew,image=self.boxs,bg="white")
        self.lpin.place(x=325,y=185)
        self.epin=Entry(self.fnew,width=20,bd=0,bg="white",fg="teal")
        self.epin.place(x=338,y=195)
        self.lpinc=Label(self.fnew,text="(Pincode)",fg="grey",bg="white")
        self.lpinc.place(x=325,y=220)
        
        
        self.llam=Label(self.fnew,image=self.boxs,bg="white")
        self.llam.place(x=484,y=185)
        self.elam=Entry(self.fnew,width=20,bd=0,bg="white",fg="teal")
        self.elam.place(x=495,y=195)
        self.llama=Label(self.fnew,text="(Landmark)",fg="grey",bg="white")
        self.llama.place(x=484,y=220)

        self.lcnt=Label(self.fnew,text="Contact Details :",font=("Arial black",10),bg="white")
        self.lcnt.place(x=10,y=250)

        self.lph1=Label(self.fnew,image=self.boxs,bg="white")
        self.lph1.place(x=10,y=280)
        self.eph1=Entry(self.fnew,width=20,bd=0,bg="white",fg="teal")
        self.eph1.place(x=20,y=290)
        self.lpho1=Label(self.fnew,text="(Phone Number 1)",fg="grey",bg="white")
        self.lpho1.place(x=10,y=315)
        
        self.lph2=Label(self.fnew,image=self.boxs,bg="white")
        self.lph2.place(x=200,y=280)
        self.eph2=Entry(self.fnew,width=20,bd=0,bg="white",fg="teal")
        self.eph2.place(x=210,y=290)
        self.lpho2=Label(self.fnew,text="(Phone Number 2)",fg="grey",bg="white")
        self.lpho2.place(x=200,y=315)
        
        self.lem=Label(self.fnew,text="Email ID ",font=("Arial black",10),bg="white")
        self.lem.place(x=10,y=355)
        self.leml=Label(self.fnew,image=self.box,bg="white")
        self.leml.place(x=70,y=350)
        self.eemails=Entry(self.fnew,width=32,bg="white",bd=0,fg="teal")
        self.eemails.place(x=90,y=360)
        self.lema=Label(self.fnew,text="(eg. john_185@gmail.com)",fg="grey",bg="white")
        self.lema.place(x=75,y=385)

        self.lgs=Label(self.fnew,text="GST bill NO ",font=("Arial black",10),bg="white")
        self.lgs.place(x=10,y=420)
        self.lgst=Label(self.fnew,image=self.box,bg="white")
        self.lgst.place(x=100,y=410)
        self.egs=Entry(self.fnew,width=25,bg="white",bd=0,fg="teal")
        self.egs.place(x=120,y=420)

        self.var = IntVar()
        self.lgs=Label(self.fnew,text="Supplier Active : ",font=("Arial black",10),bg="white")
        self.lgs.place(x=350,y=415)
        self.r1_yes = Radiobutton(self.fnew, text="Yes", variable=self.var, value=1,font=("Arial black",8),cursor="hand2",bg="white")
        self.r1_yes.place(x=490,y=415)
        self.r2_no = Radiobutton(self.fnew, text="No", variable=self.var, value=0,font=("Arial black",8),cursor="hand2",state="disabled",bg="white")
        self.r2_no.place(x=550,y=415)
        self.r1_yes.select()

        self.sb=PhotoImage(file="save.png")
        self.cb=PhotoImage(file="cancel.png")
        self.bsb=Button(self.fnew,image=self.sb,bg="white",bd=0,command=self.save_fun)
        self.bsb.place(x=280,y=480)
        self.bcb=Button(self.fnew,image=self.cb,bg="white",bd=0,command=self.canceld)
        self.bcb.place(x=380,y=480)

    #--------------------------------------------#Middle Screen New supplier function#-------------------------------------------
    


    #--------------------------------------------#Search box function#-------------------------------------------
    
    def scrchbox(self):
        self.fsrchb=Frame(root,width=400,height=35,bg="black")
        self.fsrchb.place(x=1000,y=82)
        self.srch=PhotoImage(file="sch.png")
        self.srchb=PhotoImage(file="searchbox.png")
        self.lsrchb=Label(self.fsrchb,image=self.srchb,bg="black")
        self.lsrchb.place(x=0,y=0)
        self.bsch=Button(self.fsrchb,image=self.srch,bd=0)
        self.bsch.place(x=302,y=3)
        self.escrh=Entry(self.fsrchb,width=35,border=0,font=("Calibri",12,"italic"),fg="grey")
        self.escrh.place(x=10,y=7)
        self.escrh.insert(0,"  Search table by City")
        
    #--------------------------------------------#Search box function#-------------------------------------------
        
    #--------------------------------------------#Supplier Home Screen function#-------------------------------------------
    
    def startupscreen(self):                                                                    #Startup Screen
        self.flg.destroy()
        self.logout()
        self.fstup=Frame(root,width=self.w,height=60,bg="black")
        self.fstup.place(x=0,y=70)
        self.ltit=Label(root,text="Mxcel",fg="black",font=("December Reaper",25),bg="white")
        self.ltit.place(x=43,y=20)
        self.lsuph=Button(root,text="Supplier Home",fg="white",bg="black",bd=0,font=("Arial Black",10),activebackground="black",activeforeground="white",command=self.canceld)
        self.lsuph.place(x=50,y=85)
        self.lsup=Label(root,text="| Supplier",fg="grey",bg="white")
        self.lsup.place(x=120,y=30)
        self.nb1=PhotoImage(file="new button.png")
        self.eb1=PhotoImage(file="edit button.png")
        self.db1=PhotoImage(file="delete button.png")
        self.ser1=PhotoImage(file="ser.png")
        
        self.fmid=Frame(root,width=300,height=600,bg="white")
        self.fmid.place(x=0,y=130)
        self.bnew=Button(self.fmid,image=self.nb1,bg="white",bd=0,command=self.new)
        self.bnew.place(x=-5,y=70)
        self.bedit=Button(self.fmid,image=self.eb1,bg="white",bd=0)
        self.bedit.place(x=-5,y=130)
        self.bdel=Button(self.fmid,bg="white",image=self.db1,bd=0)
        self.bdel.place(x=-5,y=190)
        self.bser1=Label(self.fmid,bg="white",image=self.ser1)
        self.bser1.place(x=-7,y=520)
        self.bckline = Canvas(self.fmid, width=5, height=1000,bd=0,highlightthickness=0,bg="white")
        self.bckline.place(x=220,y=0)
        self.bckline.create_line(0, 600, 0, 0, fill="black")
        self.scrchbox()
        

    #--------------------------------------------#Supplier Home Screen function#-------------------------------------------

    #--------------------------------------------#Logout function#-------------------------------------------
    
    def logout(self):
        self.flgout=Frame(root,width=120,height=60,bg="white")
        self.flgout.place(x=1230,y=3)
        self.lgout=PhotoImage(file="lgout.png")
        self.pro=PhotoImage(file="pro.png")
        self.lgo=Button(self.flgout,image=self.lgout,bd=0,bg="white",activebackground="white",command=self.logoutd)
        self.lgo.place(x=30,y=6)
        self.lpro=Label(self.flgout,image=self.pro,bd=0,bg="white")
        self.lpro.place(x=0,y=0)
        self.lpr=Label(self.flgout,text="Profile",fg="grey",font=("Calibri",9,"italic"),bg="white")
        self.lpr.place(x=-1,y=38)

    #--------------------------------------------#Logout function#-------------------------------------------


root=Tk()
root.title("Supplier")
sup=app(root)
root.mainloop()