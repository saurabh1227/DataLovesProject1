# ==================================importing package=================================== 
import sqlite3
from tkinter import *
from tkinter import messagebox
import datetime
#====================================== global Variable========================================
#==================== various 48 background color==============================================
bg_cl=['#fc0303','#fc2403','#fc4503','#fc6703','#fc8003','#ff8100','#fcb503', '#fcc603','#fcdf03','#fcf003',
       '#e3fc03','#befc03',  '#a9fc03','#90fc03','#73fc03','#41fc03','#2dfc03','#07fc03','#03fc14','#03fc28',
       '#03fc41','#03fc56','#03fc77','#03fc98','#03fcbe','#03fcdb','#03fcf4','#03e3fc','#03bafc','#039dfc',
       '#0384fc','#0373fc','#0356fc','#033dfc','#0324fc','#2003fc','#5203fc','#8003fc','#a503fc','#c603fc','#df03fc',
       '#fc03f4','#fc03d2','#fc03b5','#fc0384','#fc035e','#fc0339','#fc0320']
#==================== various 48 foreground color==============================================
fg_cl=['#4d0000','#400a01','#3d1000','#421b01','#4f2800','#4a2500','#4f3902','#473801','#473f01','#474401',
       '#454d02','#283601','#223301','#244001','#1a3801','#114500','#0b3d01','#023d01','#013604','#014d0c',
       '#004712','#003010','#003318','#00331f','#013b2c','#002621','#003b39','#00272b','#002533','#00263d',
       '#00203d','#001836','#001745','#010f3d','#00062e','#060036','#13003d','#1d003b','#200030','#360145','#2b0130',
       '#3b0039','#38002f','#380028','#38001d','#400017','#42000e','#380007']
c_p=0
main_vv=True
menu_vv=True
adnt_vv=True
with_vv=True
animation=False

#=================================== function that return account type==================================
def account_type(n):  # A Global Funtion 
        if n==1:
            return('Saving Account')
        elif n==2:
            return('Current Account')
        elif n==3:
            return('Fixed for 1 year')
        elif n==4:
            return('Fixed for 2 year')
        elif n==5:
            return('Fixed for 3 year')
# ===================================  -:-:- Close Account  window -:-:-================================
def close_ac(animation):
    def set_default_color():# it will reset the animation to default
            c_acnt.config(bg ='#c7ffff');l_1.config(bg ='#c7ffff',fg='#06088f')
            l_2.config(bg ='#c7ffff',fg='#06088f');bal.config(bg ='#c7ffff',fg='#06088f')
            a_c.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            chk.config(bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black')
            back.config(bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black')
            a_num.config(bg='white',fg='black')
            m_2.config(bg ='#c7ffff',fg='#06088f')
            m_2.place(x=340,y=80)                
    def switch_color(): # it will Activate the Animation
            if (a_var.get())==1:
                global c_p,with_vv
                if c_p==len(bg_cl):
                    c_p=0
                bg_c=bg_cl[c_p];fg_c=fg_cl[c_p]
                c_acnt.config(bg=bg_c);
                l_1.config(bg=bg_c,fg=fg_c);l_2.config(bg=bg_c,fg=fg_c);bal.config(bg=bg_c,fg=fg_c)
                a_c.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                chk.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                back.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                a_num.config(bg=fg_c,fg=bg_c)
                c_p+=1
                if with_vv:
                        m_2.place_forget()
                        with_vv=False
                else:
                        m_2.place(x=340,y=80)
                        m_2.config(bg=bg_c,fg='white')
                        with_vv=True       
                root.after(500,switch_color)     # it will invoke in every .25 second           
            else:
                root.after_cancel(switch_color)
                set_default_color()         
    def close():
        if ac_var.get()=='':
                messagebox.showerror("unable to get account number","Please Fill Your account number")
        else:
                cur=db.cursor()           
                cur.execute(f"select name,money from bank_management_system where Account_no={int(ac_var.get())}")
                row=cur.fetchone()
                if not row:
                    messagebox.showerror("Account Nor Exist ",f"{ac_var.get()} account number not available in our bank")
                else:
                        n=messagebox.askquestion("Confirm To Close Account",f"Are You Sure to Close Account  :  {ac_var.get()}",icon='warning')              
                        if n=='yes':
                                chk.place_forget()
                                a_num.config(state=DISABLED)
                                a_num.config(width=35)
                                bal.place(x=250,y=250)
                                db.execute(f"delete from bank_management_system where Account_no={int(ac_var.get())}")
                                db.commit()
                                db.total_changes
                                s=str(row[0])+' Your Account number : '+ac_var.get()+' has been Closed!!!'
                                bal_s.set(s)
                        else:
                                ac_var.set('')
    # ========================:-:-:-:-:- Close Window will Start from Here-:-:-:-:-:-:-==========================                          
    root.title('Close Account')# setting title 
    c_acnt=Frame(root,height='500',width='900',bg ='#c7ffff')
    c_acnt.place(x=0,y=0)
    ac_var=StringVar()
    bal_s=StringVar();a_var=IntVar()
    l_1=Label(c_acnt,text ='ROYAL BANK OF INDIA',cursor='Arrow',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman Bold', 28))
    l_1.place(x=250,y=20)
    m_2=Label(c_acnt,text ='''World's Biggest Bank''',cursor='Heart',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman Bold', 18))
    m_2.place(x=340,y=80)
    a_c=Checkbutton(c_acnt,text='Animation',variable=a_var, onvalue=1,bg='#c7ffff',fg='#06088f',font=("Arial Bold", 10),activebackground='#c7ffff',
                     activeforeground='red',command=switch_color)
    a_c.place(x=785,y=10)
    l_2=Label(c_acnt,text = 'Enter Account Number:',bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))
    l_2.place(x=60,y=180)
    a_num=Entry(c_acnt,textvariable=ac_var,bd = 1,font=("Times New Roman", 16),fg = '#06088f')
    a_num.place(x=320,y=180)
    chk=Button(c_acnt,text='Close Account',bd=1,font=("Times New Roman Bold",10),command=close,width='12',bg='red',fg='#c7ffff',
           activebackground='yellow',activeforeground='red')
    chk.place(x=600,y=180)
    bal=Label(c_acnt,textvariable=bal_s,bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))    
    back=Button(c_acnt,text='Back',font=("Arial Bold",12),width='10',bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black'
                ,command=(lambda: c_acnt.place_forget() or menu(a_var.get())))
    back.place(x=600,y=390)     
    if animation:            
            a_var.set(1)
            switch_color()
            animation=0

# ===================================  -:-:- Modified Account window -:-:-================================
def mod_window(animation):
    def set_default_color():
            mod_ac.config(bg ='#c7ffff');
            l_1.config(bg ='#c7ffff',fg='#06088f');l_2.config(bg ='#c7ffff',fg='#06088f')
            l_3.config(bg ='#c7ffff',fg='#06088f');l_4.config(bg ='#c7ffff',fg='#06088f')
            l_5.config(bg ='#c7ffff',fg='#06088f');l_6.config(bg ='#c7ffff',fg='#06088f')
            l_7.config(bg ='#c7ffff',fg='#06088f');l_8.config(bg ='#c7ffff',fg='#06088f')
            a_c.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            chk_1.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            chk_2.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            chk_3.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            chk_4.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            chk_5.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            chk_6.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            back.config(bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black')
            update.config(bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black')
            valid.config(bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black')
            name.config(bg='white',fg='black')
            dob.config(bg='white',fg='black')
            address.config(bg='white',fg='black')
            ac_no.config(bg='white',fg='black')
            phone_no.config(bg='white',fg='black')
            m_2.config(bg ='#c7ffff',fg='#06088f')
            m_2.place(x=340,y=60)
                
    def switch_color():
            if (a_var.get())==1:
                global c_p,with_vv
                if c_p==len(bg_cl):
                    c_p=0
                bg_c=bg_cl[c_p];fg_c=fg_cl[c_p]
                mod_ac.config(bg=bg_c);
                l_1.config(bg=bg_c,fg=fg_c);l_2.config(bg=bg_c,fg=fg_c);l_3.config(bg=bg_c,fg=fg_c);l_4.config(bg=bg_c,fg=fg_c)
                l_5.config(bg=bg_c,fg=fg_c);l_6.config(bg=bg_c,fg=fg_c);l_7.config(bg=bg_c,fg=fg_c);l_8.config(bg=bg_c,fg=fg_c)
                a_c.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                chk_1.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                chk_2.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                chk_3.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                chk_4.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                chk_5.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                chk_6.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                back.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                update.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                valid.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                name.config(bg=fg_c,fg=bg_c)
                dob.config(bg=fg_c,fg=bg_c)
                address.config(bg=fg_c,fg=bg_c)
                phone_no.config(bg=fg_c,fg=bg_c)
                ac_no.config(bg=fg_c,fg=bg_c)                
                c_p+=1
                if with_vv:
                        m_2.place_forget()
                        with_vv=False
                else:
                        m_2.place(x=340,y=60)
                        m_2.config(bg=bg_c,fg='white')
                        with_vv=True       
                root.after(500,switch_color)                
            else:
                root.after_cancel(switch_color)
                set_default_color()
    def checkdob():
            if mdob_var.get()=='':
                    return True
            else:
                    try:
                            datetime.datetime.strptime(mdob_var.get(),"%d/%m/%Y")
                    except ValueError:
                            return True
                    else:
                            return False
    def check_mob():
            if mphone_var.get()=='' or len(mphone_var.get())!=10:
                    return True
            else:
                    try:
                            int(mphone_var.get())
                    except ValueError:
                            return True
                    else:
                            return False                    
    def update():
        if confirm_var.get()==0:
                messagebox.showerror(" Please Agree","You can not update untill you agree")
        elif mname_var.get()=='':
                messagebox.showerror("Name is empty!!!","Please Fill your name !! ")
        elif checkdob():
                messagebox.showerror("Enter correct Date of Birth ","  Example- 01/01/2000 ")
        elif maddr_var.get()=='':
                messagebox.showerror("Address is Empty ","Please Fill Correct Address")
        elif check_mob():
                messagebox.showerror("Wrong Mobile Number!!","Please Fill Correct 10 Digit Mobile Number ")
        elif t_var.get()==0:
                messagebox.showerror("Type Of Account not Avilable !!","Please  Choose one of the Account Type!!")
        else:
                db.execute("update bank_management_system set name=?,date_of_birth=?,account_type=?,address=?,mobile_no=? where Account_no=?"
                ,(mname_var.get(),mdob_var.get(),account_type(t_var.get()),maddr_var.get(),mphone_var.get(),int(mac_var.get())))
                db.commit()
                db.total_changes                
                messagebox.showinfo("$$congratulation!!!", "Account Updated successfully")
                mod_ac.place_forget()
                mod_window(a_var.get())
    def activate_button():
        l_3.place(x=80,y=170)
        l_4.place(x=80,y=220)
        name.place(x=300,y=220)
        l_5.place(x=80,y=260)
        dob.place(x=300,y=260)
        l_6.place(x=80,y=300)
        address.place(x=300,y=300)
        l_7.place(x=80,y=340)
        phone_no.place(x=300,y=340)
        l_8.place(x=590,y=180)
        chk_1.place(x=580,y=220)
        chk_2.place(x=580,y=250)
        chk_3.place(x=580,y=280)
        chk_4.place(x=580,y=310)
        chk_5.place(x=580,y=340)
        chk_6.place(x=80,y=390)
        update.place(x=80,y=435)        
    def validate():        
        try:
                account_no=int(mac_var.get())
        except ValueError:
                messagebox.showerror("Account Not Readable","Please fill the correct account by using Digit ")
        else:
                cur=db.cursor()            
                cur.execute(f"select name from bank_management_system where Account_no={int(mac_var.get())}")
                row=cur.fetchone()
                if not row:
                    messagebox.showerror("Account Nor Exist ",f"{mac_var.get()} account number not available in our bank")
                else:
                        valid.place_forget()
                        ac_no.config(state=DISABLED,width=40)
                        activate_button()                                              
    #=====================-:-:-:-:-:-:- mod window will start from here -:-:-:-:-:-:-=====================    
    mod_ac=Frame(root,height='500',width='900',bg ='#c7ffff')
    mod_ac.place(x=0,y=0)    
    a_var=IntVar();confirm_var=IntVar();t_var=IntVar()
    mac_var=StringVar();mname_var=StringVar();maddr_var=StringVar()
    mdob_var=StringVar();mphone_var=StringVar()
    root.title('Modified the Account')# setting title
    l_1=Label(mod_ac,text ='ROYAL BANK OF INDIA',cursor='Arrow',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman Bold', 28))
    l_1.place(x=250,y=15)
    m_2=Label(mod_ac,text ='''World's Biggest Bank''',cursor='Heart',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman Bold', 18))
    m_2.place(x=340,y=60)
    a_c=Checkbutton(mod_ac,text='Animation',variable=a_var, onvalue=1,bg='#c7ffff',fg='#06088f',font=("Arial Bold", 10),activebackground='#c7ffff',
                     activeforeground='red',command=switch_color)
    a_c.place(x=785,y=10)    
    l_2=Label(mod_ac,text='Enter Your Account Number:',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 16))
    l_2.place(x=80,y=120)
    ac_no=Entry(mod_ac,bd=1,width='33',textvariable=mac_var,bg='White',font = ('Times New Roman', 16))
    ac_no.place(x=340,y=120)
    valid=Button(mod_ac,text='Validate',width='7',bg ='red',fg='white',font = ('Times New Roman', 10),command=validate,
           activebackground='red',activeforeground='yellow')
    valid.place(x=720,y=120)
    l_3=Label(mod_ac,text='Enter Modified Details:',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 16))    
    l_4=Label(mod_ac,text = 'Enter name:-',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 16))    
    name=Entry(mod_ac,bd = 1,textvariable=mname_var,font = ('Times New Roman', 14))    
    l_5=Label(mod_ac,text='Enter DOB dd/mm/yyyy:-',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 16))    
    dob=Entry(mod_ac,textvariable=mdob_var,bd=1,font = ('Times New Roman', 14)) 
    l_6=Label(mod_ac,text = 'Enter Address:-',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 16))    
    address=Entry(mod_ac,bd = 1,textvariable=maddr_var,font = ('Times New Roman', 14))    
    l_7=Label(mod_ac,text = 'Enter Phone no:-',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 16))    
    phone_no=Entry(mod_ac,textvariable=mphone_var,bd = 1,font = ('Times New Roman', 14))
    l_8=Label(mod_ac,text='Type of Account',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman Bold', 16))
    chk_1=Checkbutton(mod_ac,text='Saving Account:-',variable=t_var,onvalue=1,bg ='#c7ffff',fg='#06088f',
                      font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')    
    chk_2=Checkbutton(mod_ac,text='Current Account:-',variable=t_var,onvalue=2,bg ='#c7ffff',fg='#06088f',
                      font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')
    chk_3=Checkbutton(mod_ac,text='Fixed1(for 1 year):-',variable=t_var,onvalue=3,bg ='#c7ffff',fg='#06088f',
                      font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')
    chk_4=Checkbutton(mod_ac,text='Fixed2(for 2 year):-',variable=t_var,onvalue=4,bg ='#c7ffff',fg='#06088f',
                      font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')
    chk_5=Checkbutton(mod_ac,text='Fixed3(for 3 year):-',variable=t_var,onvalue=5,bg ='#c7ffff',fg='#06088f',
                      font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')
    chk_6=Checkbutton(mod_ac,text='Please confirm !  if you fill all information correctly !',variable=confirm_var,onvalue=1,
                      bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')
    update=Button(mod_ac,text='Update',bg ='red',fg='white',font = ('Times New Roman', 14),command=update,
                  width=15,activebackground='red',activeforeground='yellow')
    back=Button(mod_ac,text='back',width='10',bg ='red',fg='white',font = ('Times New Roman', 14),
                command=(lambda: mod_ac.place_forget() or menu(a_var.get())),
               activebackground='red',activeforeground='yellow')
    back.place(x=680,y=435)
    if animation:
            a_var.set(1)
            animation=0
            switch_color()
# ===================================  -:-:- All Account Holder List window -:-:-================================
def show_detail(animation):
    def set_default_color():
            s_det.config(bg ='#c7ffff');
            l_1.config(bg ='#c7ffff',fg='#06088f');l_2.config(bg ='#c7ffff',fg='#06088f');bal_1.config(bg ='#c7ffff',fg='#06088f')
            bal_2.config(bg ='#c7ffff',fg='#06088f');bal_3.config(bg ='#c7ffff',fg='#06088f');bal_4.config(bg ='#c7ffff',fg='#06088f')
            bal_5.config(bg ='#c7ffff',fg='#06088f');bal_6.config(bg ='#c7ffff',fg='#06088f');bal_7.config(bg ='#c7ffff',fg='#06088f')
            a_c.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            chk.config(bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black')
            back.config(bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black')
            a_num.config(bg='white',fg='black')
            m_2.config(bg ='#c7ffff',fg='#06088f')
            m_2.place(x=340,y=80)
                
    def switch_color():
            if (a_var.get())==1:
                global c_p,with_vv
                if c_p==len(bg_cl):
                    c_p=0
                bg_c=bg_cl[c_p];fg_c=fg_cl[c_p]
                s_det.config(bg=bg_c);
                l_1.config(bg=bg_c,fg=fg_c);l_2.config(bg=bg_c,fg=fg_c);bal_1.config(bg=bg_c,fg=fg_c)
                bal_2.config(bg=bg_c,fg=fg_c);bal_3.config(bg=bg_c,fg=fg_c);bal_4.config(bg=bg_c,fg=fg_c)
                bal_5.config(bg=bg_c,fg=fg_c);bal_6.config(bg=bg_c,fg=fg_c);bal_7.config(bg=bg_c,fg=fg_c)
                a_c.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                chk.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                back.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                a_num.config(bg=fg_c,fg=bg_c)
                c_p+=1
                if with_vv:
                        m_2.place_forget()
                        with_vv=False
                else:
                        m_2.place(x=340,y=80)
                        m_2.config(bg=bg_c,fg='white')
                        with_vv=True       
                root.after(500,switch_color)                
            else:
                root.after_cancel(switch_color)
                set_default_color()
    def show_detail():
            if ac_var.get()=='':
                    messagebox.showerror("unable to get account number","Please Fill Your account number")
            else:
                    cur=db.cursor()            
                    cur.execute(f"select * from bank_management_system where Account_no={int(ac_var.get())}")
                    row=cur.fetchone()
                    if not row:
                            messagebox.showerror("Account Nor Exist ",f"{ac_var.get()} account number not available in our bank")
                    else:            
                            chk.place_forget()
                            a_num.config(state=DISABLED)
                            a_num.config(width=35)                        
                            bv_1.set(f'Name:{str(row[1])}');bal_1.place(x=60,y=220)
                            bv_2.set(f'Gender:{str(row[2])}');bal_2.place(x=60,y=250)
                            bv_3.set(f'Date Of Birth:{str(row[3])}');bal_3.place(x=60,y=280)
                            bv_4.set(f'Account Type:{str(row[4])}');bal_4.place(x=60,y=310)
                            bv_5.set(f'Mobile No:{str(row[5])}');bal_5.place(x=60,y=340)
                            bv_6.set(f'Address:{str(row[6])}');bal_6.place(x=60,y=370)
                            bv_7.set(f'Balance:{str(row[7])}  $');bal_7.place(x=60,y=400)
                            
                            
    s_det=Frame(root,height='500',width='900',bg ='#c7ffff')
    s_det.place(x=0,y=0)
    a_var=IntVar()
    ac_var=StringVar()
    bv_1=StringVar();bv_2=StringVar();bv_3=StringVar();bv_4=StringVar();bv_5=StringVar();bv_6=StringVar();bv_7=StringVar()
    root.title('Detail Window') # setting title
    l_1=Label(s_det,text ='ROYAL BANK OF INDIA',cursor='Arrow',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman Bold', 28))
    l_1.place(x=250,y=20)
    m_2=Label(s_det,text ='''World's Biggest Bank''',cursor='Heart',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman Bold', 18))
    m_2.place(x=340,y=80)
    a_c=Checkbutton(s_det,text='Animation',variable=a_var, onvalue=1,bg='#c7ffff',fg='#06088f',font=("Arial Bold", 10),activebackground='#c7ffff',
                     activeforeground='red',command=switch_color)
    a_c.place(x=785,y=10)    
    l_2=Label(s_det,text = 'Enter Account Number:',bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))
    l_2.place(x=60,y=180)
    a_num=Entry(s_det,textvariable=ac_var,bd = 1,font=("Times New Roman", 16),fg = '#06088f')
    a_num.place(x=320,y=180)
    chk=Button(s_det,text='Show Detail',bd=1,font=("Times New Roman Bold",10),command=show_detail,
               width='12',bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='red')
    chk.place(x=600,y=180)
    bal_1=Label(s_det,textvariable=bv_1,bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))
    bal_2=Label(s_det,textvariable=bv_2,bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))
    bal_3=Label(s_det,textvariable=bv_3,bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))
    bal_4=Label(s_det,textvariable=bv_4,bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))
    bal_5=Label(s_det,textvariable=bv_5,bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))
    bal_6=Label(s_det,textvariable=bv_6,bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))
    bal_7=Label(s_det,textvariable=bv_7,bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))
    back=Button(s_det,text='Back',width='13',bg ='red',fg='white',font = ('Times New Roman', 14)
                ,command=(lambda: s_det.place_forget() or menu(a_var.get())),activebackground='red',activeforeground='yellow')
    back.place(x=680,y=435)
    if animation:
            a_var.set(1)
            animation=0
            switch_color()
# ===================================  -:-:- Balance Enquiry Window -:-:-================================
def check_bal(animation):
    def set_default_color():
            bal_en.config(bg ='#c7ffff');l_1.config(bg ='#c7ffff',fg='#06088f')
            l_2.config(bg ='#c7ffff',fg='#06088f');bal.config(bg ='#c7ffff',fg='#06088f')
            a_c.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            chk.config(bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black')
            back.config(bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black')
            a_num.config(bg='white',fg='black')
            m_2.config(bg ='#c7ffff',fg='#06088f')
            m_2.place(x=340,y=80)                
    def switch_color():
            if (a_var.get())==1:
                global c_p,with_vv
                if c_p==len(bg_cl):
                    c_p=0
                bg_c=bg_cl[c_p];fg_c=fg_cl[c_p]
                bal_en.config(bg=bg_c);l_1.config(bg=bg_c,fg=fg_c)
                l_2.config(bg=bg_c,fg=fg_c);bal.config(bg=bg_c,fg=fg_c)
                a_c.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                chk.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                back.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                a_num.config(bg=fg_c,fg=bg_c)
                c_p+=1
                if with_vv:
                        m_2.place_forget()
                        with_vv=False
                else:
                        m_2.place(x=340,y=80)
                        m_2.config(bg=bg_c,fg='white')
                        with_vv=True       
                root.after(500,switch_color)                
            else:
                root.after_cancel(switch_color)
                set_default_color()            
    def check():
        if ac_var.get()=='':
                messagebox.showerror("unable to get account number","Please Fill Your account number")
        else:
                cur=db.cursor()            
                cur.execute(f"select name,money from bank_management_system where Account_no={int(ac_var.get())}")
                row=cur.fetchone()
                if not row:
                    messagebox.showerror("Account Nor Exist ",f"{ac_var.get()} account number not available in our bank")
                else:            
                        chk.place_forget()
                        a_num.config(state=DISABLED)
                        a_num.config(width=35)
                        bal.place(x=250,y=250)                        
                        s=str(row[0])+' Your Balance is: '+str(row[1])+' $'
                        bal_s.set(s)            
    root.title('Balance Enquiry')# setting title 
    bal_en=Frame(root,height='500',width='900',bg ='#c7ffff')
    bal_en.place(x=0,y=0)
    ac_var=StringVar()
    bal_s=StringVar();a_var=IntVar()
    l_1=Label(bal_en,text ='ROYAL BANK OF INDIA',cursor='Arrow',bg ='#c7ffff',fg='#06088f',
              font = ('Times New Roman Bold', 28))
    l_1.place(x=250,y=20)
    m_2=Label(bal_en,text ='''World's Biggest Bank''',cursor='Heart',bg ='#c7ffff',fg='#06088f',
              font = ('Times New Roman Bold', 18))
    m_2.place(x=340,y=80)
    a_c=Checkbutton(bal_en,text='Animation',variable=a_var, onvalue=1,bg='#c7ffff',fg='#06088f',
                    font=("Arial Bold", 10),activebackground='#c7ffff',activeforeground='red',command=switch_color)
    a_c.place(x=785,y=10)
    l_2=Label(bal_en,text = 'Enter Account Number:',bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))
    l_2.place(x=60,y=180)
    a_num=Entry(bal_en,textvariable=ac_var,bd = 1,font=("Times New Roman", 16),fg = '#06088f')
    a_num.place(x=320,y=180)
    chk=Button(bal_en,text='Check Balance',bd=1,font=("Times New Roman Bold",10),command=check,
               width='12',bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='red')
    chk.place(x=600,y=180)
    bal=Label(bal_en,textvariable=bal_s,bg='#c7ffff',fg='#06088f',font=("Times New Roman", 16))    
    back=Button(bal_en,text='Back',font=("Arial Bold",12),width='10',bg='red',fg='#c7ffff',activebackground='yellow',
                activeforeground='black',command=(lambda: bal_en.place_forget() or menu(a_var.get())))
    back.place(x=600,y=390)     
    if animation:            
            a_var.set(1)
            switch_color()
            animation=0
# ===================================  -:-:- Withdraw Window -:-:-================================
def withdraw(animation):
    def set_default_color():
            dpst.config(bg='#c7ffff');
            name.config(fg='black',bg='white');pin.config(fg='black',bg='white');d_amnt.config(fg='black',bg='white')
            b_1.config(bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black')
            b_2.config(bg='red',fg='#c7ffff',activebackground='yellow',activeforeground='black')
            l_1.config(bg ='#c7ffff',fg='#06088f');l_2.config(bg ='#c7ffff',fg='#06088f')
            l_3.config(bg ='#c7ffff',fg='#06088f');l_4.config(bg ='#c7ffff',fg='#06088f');var_l.config(bg ='navy',fg='white')
            a_c.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            r_1.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            r_2.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            m_2.place(x=340,y=80)
            m_2.config(bg ='#c7ffff',fg='#06088f')
    def switch_color():
        if (a_var.get())==1:
                global c_p,with_vv
                if c_p==len(bg_cl):
                    c_p=0
                bg_c=bg_cl[c_p];fg_c=fg_cl[c_p]
                dpst.config(bg=bg_c);name.config(fg=bg_c,bg=fg_c)
                pin.config(fg=bg_c,bg=fg_c);d_amnt.config(fg=bg_c,bg=fg_c)
                b_1.config(bg=fg_c,fg=bg_c,activeforeground='white',activebackground=fg_c)
                b_2.config(bg=fg_c,fg=bg_c,activeforeground='white',activebackground=fg_c)
                l_1.config(bg=bg_c,fg=fg_c);l_2.config(bg=bg_c,fg=fg_c)
                l_3.config(bg=bg_c,fg=fg_c);l_4.config(bg=bg_c,fg=fg_c);var_l.config(bg='white',fg=fg_c)
                a_c.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='White')
                r_1.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                r_2.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                c_p+=1
                if with_vv:
                        m_2.place_forget()
                        with_vv=False
                else:
                        m_2.place(x=340,y=80)
                        m_2.config(bg=bg_c,fg='white')
                        with_vv=True                
                root.after(500,switch_color)                
        else:
                root.after_cancel(switch_color)
                set_default_color()
                
                
    def debit():
        if amnt_var.get()=='':
                messagebox.showerror("Ammount Not fill ","Please Fill Your Ammount")
        else:
                cur=db.cursor()            
                cur.execute(f"select money from bank_management_system where Account_no={int(pin.get())}")
                row=cur.fetchone()                
                if t_var.get()==1:
                        if int(amnt_var.get())<int(row[0]):
                                m=(str(int(row[0])-int(amnt_var.get())))
                                amnt_var.set('')
                                db.execute("update bank_management_system set money=? where Account_no=?",(m,pin.get()))
                                db.commit()
                                db.total_changes
                                messagebox.showinfo("Deposited successfully",f"Blance Left : {amnt_var.get()} in your account")
                                dpst.place_forget()                                
                                withdraw(a_var.get())
                        else:
                                messagebox.showerror("Ammount is too High",f"Your Current ammount is :{int(row[0])}")
                elif t_var.get()==2:                        
                        m=(int(row[0])+int(amnt_var.get()))
                        amnt_var.set('')                                      
                        db.execute("update bank_management_system set money=? where Account_no=?",(m,pin.get()))
                        db.commit()
                        db.total_changes
                        messagebox.showinfo("Creditted successfully",f"Blance Left : {m} in your account")
                        dpst.place_forget()                                
                        withdraw(a_var.get())                                                                                  
    def show_b():
            if t_var.get()==1:
                     b_1.place(x=105,y=410)
                     b_1.config(text='Deposite')
            elif t_var.get()==2:
                     b_1.place(x=105,y=410)
                     b_1.config(text='Credit')
    def varify_acnt():
            if pin.get()=='':
                    messagebox.showerror("Account Number not correct",'pleasen fill your account number not available in our bank')
                    return
            cur=db.cursor()            
            cur.execute(f"select name from bank_management_system where Account_no={int(pin.get())}")
            row=cur.fetchone()
            if not row:
                    messagebox.showerror("Account Nor Exist ",f"{pin.get()} account number not available in our bank")                    
            elif str(row[0])==name_var.get():            
                    name.config(state=DISABLED)
                    pin.config(state=DISABLED)
                    r_1.place(x=130,y=270)
                    r_2.place(x=400,y=270)
                    l_4.place(x=100,y=320)
                    d_amnt.place(x=360,y=320)
                    v_1.place_forget()
                    var_l.place(x=600,y=223)
            else:
                    if name_var.get()=='':
                            messagebox.showerror("Name not available"," Please Fill Your Appropriate Name")
                    else:
                            messagebox.showerror("Not Found"," Name does not matched with existing account number!")
            
    # ======================= Creating frame=========================
    dpst=Frame(root,height='500',width='900',bg ='#c7ffff')
    dpst.place(x=0,y=0)
    name_var=StringVar()
    acn_var=StringVar()
    amnt_var=StringVar()
    at_var=IntVar();t_var=IntVar();a_var=IntVar()
    root.title('Withdraw/Credit') #settung the title
    l_1=Label(dpst,text ='ROYAL BANK OF INDIA',cursor='Arrow',bg ='#c7ffff',fg='#06088f',
              font = ('Times New Roman Bold', 28))
    l_1.place(x=250,y=20)
    m_2=Label(dpst,text ='''World's Biggest Bank''',cursor='Heart',bg ='#c7ffff',fg='#06088f',
              font = ('Times New Roman Bold', 18))
    m_2.place(x=340,y=80)
    a_c=Checkbutton(dpst,text='Animation',variable=a_var, onvalue=1,bg='#c7ffff',fg='#06088f',
                    font=("Arial Bold", 10),activebackground='#c7ffff',activeforeground='red',command=switch_color)
    a_c.place(x=785,y=10)
    l_2=Label(dpst,text = 'Enter Account Holder Name:-',bg='#c7ffff',fg='#06088f',font=("Arial ", 14))
    l_2.place(x=100,y=150)
    name=Entry(dpst,textvariable=name_var,bd = 3,font=("Arial ", 14),fg = '#06088f')
    name.place(x=360,y=150)
    l_3=Label(dpst,text='Enter the Account no:-',bg='#c7ffff',fg='#06088f',font=("Arial ", 14))
    l_3.place(x=100,y=220)
    pin=Entry(dpst,textvariable=acn_var,bd=3,fg='#06088f',font=("Arial ", 14))
    pin.place(x=360,y=220)
    v_1=Button(dpst,text='Varify',font=("Arial Bold",8),command=varify_acnt,width='8',bg='black',
               fg='white',activebackground='white',activeforeground='black')
    v_1.place(x=600,y=221)
    r_1=Radiobutton(dpst,text='Deposite',variable=t_var,value=1,command=show_b,bg='#c7ffff',fg='#06088f',
                    font=("Arial Bold", 12),activebackground='#c7ffff',activeforeground='red')    
    r_2=Radiobutton(dpst,text='Credit',variable=t_var,value=2,command=show_b,bg='#c7ffff',
                    fg='#06088f',font=("Arial Bold", 12),activebackground='#c7ffff',activeforeground='red')    
    l_4=Label(dpst,text = 'Enter Amount:-',bg='#c7ffff',fg='#06088f',font=("Arial ", 14))    
    d_amnt=Entry(dpst,textvariable=amnt_var,bd = 3,font=("Arial ", 14),fg ='#06088f')    
    b_1=Button(dpst,font=("Arial Bold",12),command=debit,width='10',bg='red',fg='#c7ffff',
               activebackground='yellow',activeforeground='black')    
    b_2=Button(dpst,text='Back',font=("Arial Bold",12),width='10',bg='red',fg='#c7ffff',
               activebackground='yellow',activeforeground='black',command=(lambda: dpst.place_forget() or menu(a_var.get())))
    b_2.place(x=700,y=410)    
    var_l=Label(dpst,text='Verified',bg='navy',fg='white',font=("Arial Bold", 10))
    if animation:
            a_var.set(1)
            switch_color()
            animation=0
# ==============================  -:-:- Add New Account  Window  -:-:-==============================
def add_new_account(animation):   
    def set_default_color():
                add_acnt.config(bg='#c7ffff');m_2.config(bg='#c7ffff',fg='#06088f');m_2.place(x=340,y=65)
                amnt_e.config(fg='black',bg='white');phone_no.config(fg='black',bg='white')
                addr.config(fg='black',bg='white');dob.config(fg='black',bg='white')
                name.config(fg='black',bg='white')
                b_1.config(bg ='red',fg='white',activebackground='red',activeforeground='yellow')
                b_2.config(bg ='red',fg='white',activebackground='red',activeforeground='yellow')
                l_1.config(bg='#c7ffff',fg='#06088f');l_2.config(bg='#c7ffff',fg='#06088f')
                l_3.config(bg='#c7ffff',fg='#06088f');l_4.config(bg='#c7ffff',fg='#06088f')
                l_5.config(bg='#c7ffff',fg='#06088f');l_6.config(bg='#c7ffff',fg='#06088f')
                l_7.config(bg='#c7ffff',fg='#06088f');l_8.config(bg='#c7ffff',fg='#06088f')
                r_1.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
                r_2.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
                c_1.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
                c_2.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
                c_3.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
                c_4.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
                c_5.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
                c_6.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
                a_c.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            
    def switch_color():
        if (a_var.get())==1:
                global c_p,adnt_vv
                if c_p==len(bg_cl):
                    c_p=0
                bg_c=bg_cl[c_p];fg_c=fg_cl[c_p]
                add_acnt.config(bg=bg_c);
                amnt_e.config(fg=bg_c,bg=fg_c);phone_no.config(fg=bg_c,bg=fg_c);addr.config(fg=bg_c,bg=fg_c)
                dob.config(fg=bg_c,bg=fg_c);name.config(fg=bg_c,bg=fg_c)
                b_1.config(bg=fg_c,fg=bg_c,activeforeground='white',activebackground=fg_c)
                b_2.config(bg=fg_c,fg=bg_c,activeforeground='white',activebackground=fg_c)
                l_1.config(bg=bg_c,fg=fg_c);l_2.config(bg=bg_c,fg=fg_c);l_3.config(bg=bg_c,fg=fg_c)
                l_4.config(bg=bg_c,fg=fg_c);l_5.config(bg=bg_c,fg=fg_c);l_6.config(bg=bg_c,fg=fg_c)
                l_7.config(bg=bg_c,fg=fg_c);l_8.config(bg=bg_c,fg=fg_c)
                r_1.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                r_2.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                c_1.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                c_2.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                c_3.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                c_4.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                c_5.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                c_6.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                a_c.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                c_p+=1
                if adnt_vv:
                        m_2.place_forget()
                        adnt_vv=False
                else:
                        m_2.place(x=340,y=65)
                        m_2.config(bg=bg_c,fg='white')
                        adnt_vv=True                        
                root.after(500,switch_color)
        else:
                root.after_cancel(switch_color)
                set_default_color()
    def get_gender(n):
            if n==1:
                    return 'male'
            else:
                    return 'female'
    def vary_mob():
            if no_var.get()=='' or len(no_var.get())!=10:
                    return True
            else:
                    try:
                            int(no_var.get())
                    except ValueError:
                            return Tru
                    else:
                            return False
    def vary_dob():
            if db_var.get()=='':
                    return True
            else:
                    try:
                            datetime.datetime.strptime(db_var.get(),"%d/%m/%Y")
                    except ValueError:
                            return True
                    else:
                            return False
    def create_acnt():
        if c_var.get()==0:
                messagebox.showerror("Unable to Create New Account","Please Agree the Our Term and Conditon!!!")
        elif name_var.get()=='':
                messagebox.showerror("Unable to Create New Account","Please Fill Your Name!!")
        elif g_var.get()==0:
                messagebox.showerror("Unable to Create New Account","Please Select Your Gender!!")
        elif vary_dob():
                messagebox.showerror("Enter a Valid Date Of Birth","Example- 01/01/2000")
        elif address_var.get()=='':
                messagebox.showerror("Unable to Create New Account","Please Enter Address!!")
        elif vary_mob():
                messagebox.showerror("Wrong Mobile Number","Mobile Number Should Be 10 Digit!!")
        elif amnt_var.get()=='':
                messagebox.showerror("Unable to Create New Account","Please Enter Deposite Ammount!!")
        elif at_var.get()==0:
                messagebox.showerror("Unable to Create New Account","Please Select Account Type!!")
        else:            
                db.execute('insert into  bank_management_system (name,gender,date_of_birth,account_type,mobile_no,address,money) \
                                values (?,?,?,?,?,?,?)',
                          (name_var.get(),get_gender(g_var.get()),db_var.get(),account_type(at_var.get()),no_var.get(),address_var.get(),int(amnt_var.get())));
                db.commit()
                cursor=db.execute('select max(Account_no) from bank_management_system')
                ac_no=cursor.fetchone()[0]                
                
                messagebox.showinfo(f"Congratulation {name_var.get()}  !!!!", "Account Has Been Created successfully")
                messagebox.showinfo(f"Congratulation {name_var.get()}  !!!!", f"Your Account Number is : {ac_no}")
                add_acnt.place_forget()
                add_new_account(a_var.get())
    # ============ Declaration of Variables==================================
    at_var=IntVar();g_var=IntVar();name_var=StringVar();db_var=StringVar();a_var=IntVar()   
    address_var=StringVar();no_var=StringVar();amnt_var=StringVar();c_var=IntVar();
    # ======================= Creating Add New Account window===============
    root.title('add account')                    #setting title    
    add_acnt= Frame(root,height='500',width='900',bg ='#c7ffff')
    add_acnt.place(x=0,y=0)
    l_1=Label(add_acnt,text ='ROYAL BANK OF INDIA',cursor='Arrow',bg ='#c7ffff',
              fg='#06088f',font = ('Times New Roman Bold', 28))
    l_1.place(x=250,y=15)
    m_2=Label(add_acnt,text ='''World's Biggest Bank''',cursor='Heart',bg ='#c7ffff',
              fg='#06088f',font = ('Times New Roman Bold', 18))
    m_2.place(x=340,y=65)
    a_c=Checkbutton(add_acnt,text='Animation',variable=a_var, onvalue=1,bg='#c7ffff',fg='#06088f',font=("Arial Bold", 10),
                    activebackground='#c7ffff',activeforeground='red',command=switch_color)
    a_c.place(x=785,y=10)
    l_2=Label(add_acnt,text="""Enter Your Account Holder's Name:-""",bg ='#c7ffff',
              fg='#06088f',font = ('Times New Roman', 16))
    l_2.place(x=60,y=120)
    name=Entry(add_acnt,bd=1,textvariable=name_var,width='40',bg='White',font = ('Times New Roman', 16))
    name.place(x=410,y=120)
    l_3=Label(add_acnt,text='Gender:',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 16))
    l_3.place(x=60,y=170)
    r_1=Radiobutton(add_acnt,text='Male',variable=g_var, value=1,bg ='#c7ffff',fg='#06088f'
                    ,font = ('Times New Roman', 16),activebackground='#c7ffff',activeforeground='red')
    r_1.place(x=180,y=170)
    r_2=Radiobutton(add_acnt,text='Female',variable=g_var,value=2,bg ='#c7ffff',fg='#06088f',
                    font = ('Times New Roman', 16),activebackground='#c7ffff',activeforeground='red')
    r_2.place(x=300,y=170)
    l_4=Label(add_acnt,text = 'DOB (dd/mm/yyyy):-',bg ='#c7ffff',fg='#06088f',
              font = ('Times New Roman', 16))
    l_4.place(x=60,y=220)
    dob=Entry(add_acnt,textvariable=db_var,bd = 1,font = ('Times New Roman', 14))
    dob.place(x=300,y=220)
    l_5=Label(add_acnt,text='Enter Address:-',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 16))
    l_5.place(x=60,y=260)
    addr=Entry(add_acnt,textvariable=address_var,bd=1,font = ('Times New Roman', 14))
    addr.place(x=300,y=260)
    l_6=Label(add_acnt,text = 'Enter Phone no:-',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 16))
    l_6.place(x=60,y=300)
    phone_no=Entry(add_acnt,textvariable=no_var,bd = 1,font = ('Times New Roman', 14))
    phone_no.place(x=300,y=300)
    l_7=Label(add_acnt,text = 'Enter Amount to deposit:-',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 16))
    l_7.place(x=60,y=340)
    amnt_e=Entry(add_acnt,textvariable=amnt_var,bd = 1,font = ('Times New Roman', 14))
    amnt_e.place(x=300,y=340)
    l_8=Label(add_acnt,text='Type of Account',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman Bold', 16))
    l_8.place(x=600,y=180)
    c_1=Checkbutton(add_acnt,text='Saving Account:-',variable=at_var,onvalue=1,bg ='#c7ffff',fg='#06088f',
                    font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')
    c_1.place(x=580,y=220)
    c_2=Checkbutton(add_acnt,text='Current Account:-',variable=at_var,onvalue=2,bg ='#c7ffff',fg='#06088f',
                    font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')
    c_2.place(x=580,y=250)
    c_3=Checkbutton(add_acnt,text='Fixed1(for 1 year):-',variable=at_var,onvalue=3,bg ='#c7ffff',fg='#06088f',
                    font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')
    c_3.place(x=580,y=280)
    c_4=Checkbutton(add_acnt,text='Fixed2(for 2 year):-',variable=at_var,onvalue=4,bg ='#c7ffff',fg='#06088f',
                    font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')
    c_4.place(x=580,y=310)
    c_5=Checkbutton(add_acnt,text='Fixed3(for 3 year):-',variable=at_var,onvalue=5,bg ='#c7ffff',fg='#06088f',
                    font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')
    c_5.place(x=580,y=340)
    c_6=Checkbutton(add_acnt,text='Please confirm !  if you fill all information correctly',variable=c_var,onvalue=1,
                        bg ='#c7ffff',fg='#06088f',font = ('Times New Roman', 14),activebackground='#c7ffff',activeforeground='red')
    c_6.place(x=60,y=390)
    b_1=Button(add_acnt,text='Create account',bg ='red',fg='white',font = ('Times New Roman', 14),
               command=create_acnt,width=15,activebackground='red',activeforeground='yellow')
    b_1.place(x=65,y=435)
    b_2=Button(add_acnt,text='Back',width='13',bg ='red',fg='white',font = ('Times New Roman', 14),
               command=(lambda: add_acnt.place_forget() or menu(a_var.get())),activebackground='red',activeforeground='yellow')
    b_2.place(x=680,y=435)
    if animation:            
            a_var.set(1)
            switch_color()
            animation=0    
# ==============================  -:-:-Menu Window  -:-:-==============================
def menu(animation):
    #=========================== this will change automatic background color=============================
    def set_default_color():
            menu_f.config(bg='#c7ffff');m_1.config(bg ='#c7ffff',fg='#06088f');m_2.config(bg ='#c7ffff',fg='#06088f')
            back.config(bg ='red',fg='white',activebackground='yellow',activeforeground='red')
            b_1.config(bg ='red',fg='white',activebackground='yellow',activeforeground='red')
            b_2.config(bg ='red',fg='white',activebackground='yellow',activeforeground='red')
            b_3.config(bg ='red',fg='white',activebackground='yellow',activeforeground='red')
            b_4.config(bg ='red',fg='white',activebackground='yellow',activeforeground='red')
            b_5.config(bg ='red',fg='white',activebackground='yellow',activeforeground='red')
            b_6.config(bg ='red',fg='white',activebackground='yellow',activeforeground='red')
            a_c.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            m_2.place(x=340,y=85)            
    def switch_color():
            if (a_var.get())==1:
                    global c_p,menu_vv
                    if c_p==len(bg_cl):
                            c_p=0
                    bg_c=bg_cl[c_p]; fg_c=fg_cl[c_p]
                    menu_f.config(bg=bg_c);m_1.config(bg=bg_c,fg=fg_c);m_2.config(bg=bg_c,fg=fg_c)
                    back.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                    b_1.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                    b_2.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                    b_3.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                    b_4.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                    b_5.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                    b_6.config(bg=fg_c,fg=bg_c,activebackground=fg_c,activeforeground='white')
                    a_c.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                    c_p+=1
                    root.after(500,switch_color)
                    if menu_vv:
                            m_2.place_forget()
                            menu_vv=False
                    else:
                            m_2.place(x=340,y=85)
                            m_2.config(bg=bg_c,fg='white')
                            menu_vv=True                            
            else:
                    root.after_cancel(switch_color)
                    set_default_color()
    # ================================= Creating Menu Window====================================
    a_var=IntVar()
    root.title('menu')                #setting title
    menu_f= Frame(root,height='500',width='900',bg ='#c7ffff')
    menu_f.place(x=0,y=0)
    m_1=Label(menu_f,text ='ROYAL BANK OF INDIA',cursor='Heart',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman Bold', 28))
    m_1.place(x=250,y=30)
    m_2=Label(menu_f,text ='''World's Biggest Bank''',cursor='Heart',bg ='#c7ffff',fg='#06088f',font = ('Times New Roman Bold', 18))
    m_2.place(x=340,y=85)
    a_c=Checkbutton(menu_f,text='Animation',variable=a_var, onvalue=1,bg='#c7ffff',fg='#06088f',font=("Arial Bold", 10)
                    ,activebackground='#c7ffff',activeforeground='red',command=switch_color)
    a_c.place(x=785,y=10)
    b_1=Button(menu_f,text='NEW ACCOUNT',bd=8,bg ='red',fg='white',width=25,
                font = ('Times New Roman Bold', 16),activebackground='red',
                   activeforeground='yellow',command=(lambda: menu_f.place_forget() or add_new_account(a_var.get())))
    b_1.place(x=50,y=160)
    b_2=Button(menu_f,text='WITHDRAW/CREDIT',bd=8,bg ='red',fg='white',width=25,
                   font = ('Times New Roman Bold', 16),activebackground='red',
                   activeforeground='yellow',command=(lambda: menu_f.place_forget() or withdraw(a_var.get())))
    b_2.place(x=500,y=160)
    b_3=Button(menu_f,text='BALANCE ENQUIRY',bd=8,bg ='red',fg='white',width=25,
                   font = ('Times New Roman Bold', 16),activebackground='red',
                   activeforeground='yellow',command=(lambda: menu_f.place_forget() or check_bal(a_var.get())))
    b_3.place(x=50,y=250)
    b_4=Button(menu_f,text='SHOW DETAILS',bd=8,bg ='red',fg='white',width=25,
                   font = ('Times New Roman Bold', 16),activebackground='red',
                   activeforeground='yellow',command=(lambda: menu_f.place_forget() or show_detail(a_var.get())))
    b_4.place(x=500,y=250)
    b_5=Button(menu_f,text='CLOSE AN ACCOUNT',bd=8,bg ='red',fg='white',width=25,
                   font = ('Times New Roman Bold', 16),activebackground='red',
                   activeforeground='yellow',command=(lambda: menu_f.place_forget() or close_ac(a_var.get())))
    b_5.place(x=50,y=350)
    b_6=Button(menu_f,text='MODIFY AN ACCOUNT',bd=8,bg ='red',fg='white',width=25,
                   font = ('Times New Roman Bold', 16),activebackground='red',
                   activeforeground='yellow',command=(lambda: menu_f.place_forget() or mod_window(a_var.get())))
    b_6.place(x=500,y=350)
    back=Button(menu_f,text='Back',bd=5,bg ='red',fg='white',width=10,
                   font = ('Times New Roman Bold', 10),activebackground='red',
                   activeforeground='yellow',command=(lambda: menu_f.place_forget() or main_root(a_var.get())))
    back.place(x=735,y=430)
    if animation:
            a_var.set(1)
            animation=0
            switch_color()
            
    
#====================== -:-:- Main Home Window -:-:-======================

def main_root(animation):
    #======================this will change color automatically================
    def set_default_color():
            main_f.config(bg='#c7ffff')
            l4.place(x=380,y=250);l4.config(bg='#c7ffff',fg='#06088f')
            l1.config(bg='#c7ffff',fg='#06088f');l2.config(bg='#c7ffff',fg='#06088f')
            l3.config(bg='#c7ffff',fg='#06088f');txt.config(bg='#c7ffff',fg='#06088f')                   
            arw.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')
            a_c.config(bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',activeforeground='red')    
            
    def switch_color():
            if (a_var.get())==1:
                    global c_p,main_vv
                    if c_p==len(bg_cl):
                            c_p=0
                    bg_c=bg_cl[c_p]; fg_c=fg_cl[c_p]
                    main_f.config(bg=bg_c);l1.config(bg=bg_c,fg=fg_c);l2.config(bg=bg_c,fg=fg_c)
                    l3.config(bg=bg_c,fg=fg_c);txt.config(bg=bg_c,fg=fg_c)                   
                    arw.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                    a_c.config(bg=bg_c,fg=fg_c,activebackground=bg_c,activeforeground='white')
                    c_p+=1                  
                    root.after(500,switch_color)
                    if main_vv:
                            l4.place_forget()
                            main_vv=False
                    else:
                            l4.place(x=380,y=250)
                            l4.config(bg=bg_c,fg='white')
                            main_vv=True                            
            else:
                    
                    root.after_cancel(switch_color)
                    set_default_color()
                                   
    a_var=IntVar()
    root.title('home')                                               # setting title
    root.configure(bg='#c7ffff')                            # setting background color
    main_f=Frame(root,height='500',width='900',bg='#c7ffff')
    main_f.place(x=0,y=0)
    a_c=Checkbutton(main_f,text='Animation',variable=a_var, onvalue=1,bg='#c7ffff',fg='#06088f',font=("Arial Bold", 10)
                    ,activebackground='#c7ffff',activeforeground='red',command=switch_color)
    a_c.place(x=785,y=10)
    l1=Label(main_f,text = 'Welcome To The',bg='#c7ffff',
             fg='#06088f',font=("Times New Roman Bold", 28))
    l1.place(x=300,y=40)
    l2=Label(main_f,text = 'Royal Bank Of India',bg='#c7ffff',
             fg='#06088f',font=("Times New Roman Bold", 28))
    l2.place(x=270,y=100)
    l3=Label(main_f,text = 'Brought By Data Loves',bg='#c7ffff'
             ,fg='#06088f',font=("Times New Roman Bold", 14))
    l3.place(x=630,y=420)
    l4=Label(main_f,text = 'Press Arrow',bg='#c7ffff'
             ,fg='#06088f',font=("Times New Roman Bold", 18))
    l4.place(x=380,y=250)
    txt=Label(main_f,text = '''World's Biggest Bank''',bg='#c7ffff',
              fg='#06088f',font=("Times New Roman", 24))
    txt.place(x=300,y=170)
    arw=Button(main_f,text='➡',font=("Times New Roman Bold", 64),
               bd=0,bg='#c7ffff',fg='#06088f',activebackground='#c7ffff',
               activeforeground='red',command=(lambda: main_f.place_forget() or menu(a_var.get())))
    arw.place(x=370,y=275)
    if animation:
            a_var.set(1)
            animation=0
            switch_color()
# ============== -:-:-:- App Will Start From Here  -:-:-:- ==================
root = Tk()                                                         #main root 
root.iconbitmap('bank_logo.ico')                    # setting icon
root.resizable(0,0)                                            # this make window unresizable
root.geometry('900x500')                                # setting height and width of window
# =================== -:-:-:- connecting with database and creating table -:-:-:- ====================
db=sqlite3.connect('Bank_data_base.db')                        # this coonnect with databse with bmsdb.db file name
db.execute('''create table if not exists bank_management_system(
                                Account_no integer primary key autoincrement,
                                name text  char(30),
                                gender text char(15),
                                date_of_birth text not null,
                                account_type text char(30),
                                mobile_no text char(15),
                                address text char(50),
                                money real)''')
# ====================This will start home window=================
main_root(0)                                                      # this will open main home window function
#============================ -:-:- Starting loop  -:-:-  =================
root.mainloop()
#========================== Closing Database connection================
db.close()
#============================ This Application has been developed by Mohd Saddam ==============================
