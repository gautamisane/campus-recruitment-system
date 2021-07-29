#importing module
import campusRecruitmentDB
from tkinter import *
import time

#creating root window
root = Tk()
root.title('Campus Recruitment System')
p1 = PhotoImage(file = 'icons8-school-48.png')
root.iconphoto(False, p1)
root.geometry("400x400")

#clock
def clock():
    hr = time.strftime("%H")
    minute = time.strftime("%M")
    sec = time.strftime("%S")

    my_label = Label(root,text ="")
    my_label.grid(row=5,column=1)
    my_label.config(text="Time : " + hr + ":" + minute + ":" + sec)
    my_label.after(1000,clock)
clock()

def stdsubmit():
    val = (student_id.get(),sname.get(),email.get(),phone_no.get(),gender.get(),department.get(),ssc_percent.get(),ssc_board.get(),hsc_percent.get(),hsc_board.get(),degree_percent.get(),apti_percent.get(),work_exp.get(),placement_status.get(),salary.get(),company.get())
    campusRecruitmentDB.std_values(val)

    student_id.delete(0,END)
    sname.delete(0,END)
    email.delete(0,END)
    phone_no.delete(0,END)
    gender.delete(0,END)
    department.delete(0,END)
    ssc_percent.delete(0,END)
    ssc_board.delete(0,END)
    hsc_percent.delete(0,END)
    hsc_board.delete(0,END)
    degree_percent.delete(0,END)
    apti_percent.delete(0,END)
    work_exp.delete(0,END)
    placement_status.delete(0,END)
    salary.delete(0,END)
    company.delete(0,END)

def stdRegister():
    global student_id,sname,email,phone_no,gender,department
    global ssc_percent,ssc_board,hsc_percent,hsc_board,degree_percent
    global apti_percent,work_exp,placement_status,salary,company
    stdr=Toplevel(std1)
    stdr.geometry('500x500')
    stdr.title('Student Registration')
    p1 = PhotoImage(file = 'icons8-school-48.png')
    stdr.iconphoto(False, p1)

    #clock
    def clock():
        hr = time.strftime("%H")
        minute = time.strftime("%M")
        sec = time.strftime("%S")

        my_label = Label(stdr,text ="")
        my_label.place(x=10,y=470)
        my_label.config(text="Time : " + hr + ":" + minute + ":" + sec)
        my_label.after(1000,clock)
    clock()
    
    #creating text boxes
    student_id=Entry(stdr,width=50)
    student_id.grid(row=0,column=1,pady=(10,0))

    sname=Entry(stdr,width=50)
    sname.grid(row=1,column=1)

    email=Entry(stdr,width=50)
    email.grid(row=2,column=1)

    phone_no=Entry(stdr,width=50)
    phone_no.grid(row=3,column=1)

    gender = StringVar()
    gender.set("M")
    m=Radiobutton(stdr,text="Male",variable=gender,value = "M")
    m.grid(row=4,column=1)
    f=Radiobutton(stdr,text="Female",variable=gender,value = "F")
    f.grid(row=5,column=1)
    #gender=Entry(stdr,width=50)
    #gender.grid(row=4,column=1)

    department=Entry(stdr,width=50)
    department.grid(row=6,column=1)

    ssc_percent=Entry(stdr,width=50)
    ssc_percent.grid(row=7,column=1)

    ssc_board=Entry(stdr,width=50)
    ssc_board.grid(row=8,column=1)

    hsc_percent=Entry(stdr,width=50)
    hsc_percent.grid(row=9,column=1)

    hsc_board=Entry(stdr,width=50)
    hsc_board.grid(row=10,column=1)

    degree_percent=Entry(stdr,width=50)
    degree_percent.grid(row=11,column=1)

    apti_percent=Entry(stdr,width=50)
    apti_percent.grid(row=12,column=1)

    work_exp=Entry(stdr,width=50)
    work_exp.grid(row=13,column=1)

    placement_status=Entry(stdr,width=50)
    placement_status.grid(row=14,column=1)

    salary=Entry(stdr,width=50)
    salary.grid(row=15,column=1)

    company=Entry(stdr,width=50)
    company.grid(row=16,column=1)

    #creating textbox labels
    label1 = Label(stdr,text="Student ID")
    label1.grid(row=0,column=0,padx=50,pady=(10,0))

    label2 = Label(stdr,text="Name")
    label2.grid(row=1,column=0)

    label3 = Label(stdr,text="Email ID")
    label3.grid(row=2,column=0)

    label4 = Label(stdr,text="Contact No.")
    label4.grid(row=3,column=0)

    label5 = Label(stdr,text="Gender")
    label5.grid(row=4,column=0)

    label6 = Label(stdr,text="Department")
    label6.grid(row=6,column=0)

    label7 = Label(stdr,text="10th Percentage")
    label7.grid(row=7,column=0)

    label8 = Label(stdr,text="10th Board")
    label8.grid(row=8,column=0)

    label9 = Label(stdr,text="12th Percentage")
    label9.grid(row=9,column=0)

    label10 = Label(stdr,text="12th Board")
    label10.grid(row=10,column=0)

    label11 = Label(stdr,text="Degree Percentage")
    label11.grid(row=11,column=0)

    label12 = Label(stdr,text="Aptitude Percentage")
    label12.grid(row=12,column=0)

    label13 = Label(stdr,text="Work Experience")
    label13.grid(row=13,column=0)

    label14 = Label(stdr,text="Placement Status")
    label14.grid(row=14,column=0)

    label15 = Label(stdr,text="Salary(put 0 if NA)")
    label15.grid(row=15,column=0)

    label16 = Label(stdr,text="Company")
    label16.grid(row=16,column=0)
        
    submit_btn = Button(stdr,text="SUBMIT",width=50,command=stdsubmit)
    submit_btn.grid(row=17,column=0,columnspan=2,pady=20,padx=10)
    
def stdView():
        val = enter_sid.get()
        result = campusRecruitmentDB.std_view(val)

        enter_std1=Label(stdp,text ="Student ID:" + str(result[0]))
        enter_std1.grid(row=3,column=0,columnspan=2,pady=(20,0))
        enter_std2=Label(stdp,text ="Name:" + str(result[1]))
        enter_std2.grid(row=4,column=0,columnspan=2)
        enter_std3=Label(stdp,text ="Email ID:" + str(result[2]))
        enter_std3.grid(row=5,column=0,columnspan=2)
        enter_std4=Label(stdp,text ="Contact No:" + str(result[3]))
        enter_std4.grid(row=6,column=0,columnspan=2)
        enter_std5=Label(stdp,text ="Gender:" + str(result[4]))
        enter_std5.grid(row=7,column=0,columnspan=2)
        enter_std6=Label(stdp,text ="Department:" + str(result[5]))
        enter_std6.grid(row=8,column=0,columnspan=2)
        enter_std7=Label(stdp,text ="10th Percentage:" + str(result[6]))
        enter_std7.grid(row=9,column=0,columnspan=2)
        enter_std8=Label(stdp,text ="10th Board:" + str(result[7]))
        enter_std8.grid(row=10,column=0,columnspan=2)
        enter_std9=Label(stdp,text ="12th Percentage:" + str(result[8]))
        enter_std9.grid(row=11,column=0,columnspan=2)
        enter_std10=Label(stdp,text ="12th Board:" + str(result[9]))
        enter_std10.grid(row=12,column=0,columnspan=2)
        enter_std11=Label(stdp,text ="Degree Percentage:" + str(result[10]))
        enter_std11.grid(row=13,column=0,columnspan=2)
        enter_std12=Label(stdp,text ="Aptitude Percentage:" + str(result[11]))
        enter_std12.grid(row=14,column=0,columnspan=2)
        enter_std13=Label(stdp,text ="Work Experience:" + str(result[12]))
        enter_std13.grid(row=15,column=0,columnspan=2)
        enter_std14=Label(stdp,text ="Placement Status:" + str(result[13]))
        enter_std14.grid(row=16,column=0,columnspan=2)
        enter_std15=Label(stdp,text ="Salary:" + str(result[14]))
        enter_std15.grid(row=17,column=0,columnspan=2)
        enter_std16=Label(stdp,text ="Company:" + str(result[15]))
        enter_std16.grid(row=18,column=0,columnspan=2)
        
        enter_sid.delete(0, END)
        
def stdDelete():
    val = enter_sid.get()
    campusRecruitmentDB.std_del(val)

    enter_sid.delete(0, END)
           
def stdLogin():
    global enter_sid,stdp    
    stdp=Toplevel(std1)
    stdp.geometry('500x500')
    stdp.title('Student Profile')
    p1 = PhotoImage(file = 'icons8-school-48.png')
    stdp.iconphoto(False, p1)

    #clock
    def clock():
        hr = time.strftime("%H")
        minute = time.strftime("%M")
        sec = time.strftime("%S")

        my_label = Label(stdp,text ="")
        my_label.place(x=10,y=470)
        my_label.config(text="Time : " + hr + ":" + minute + ":" + sec)
        my_label.after(1000,clock)
    clock()

    #creating textbox
    enter_sid=Entry(stdp,width=50)
    enter_sid.grid(row=0,column=1,pady=10)

    #creating label
    label11 = Label(stdp,text="Enter Student ID")
    label11.grid(row=0,column=0,padx=(50,20))

    #creating buttons
    stdp1 = Button(stdp,text="VIEW PROFILE",height=1,width=60,command=stdView)
    stdp1.grid(row=1,column=0,columnspan=2,padx=30)
    stdpd = Button(stdp,text="DELETE PROFILE",height=1,width=60,command=stdDelete)
    stdpd.grid(row=2,column=0,columnspan=2)
    
def submitApp():
    val = (job_id.get(),jname.get(),adcname.get(),jsalary.get(),min_aptiPercent.get(),min_bePercent.get(),min_workexp.get())
    campusRecruitmentDB.app_values(val)

    job_id.delete(0, END)
    jname.delete(0, END)
    adcname.delete(0, END)
    jsalary.delete(0, END)
    min_aptiPercent.delete(0, END)
    min_bePercent.delete(0, END)

def adView():
    val = enter_jid.get()
    result = campusRecruitmentDB.ad_view(val)
    enter_ad1=Label(ad,text ="Job ID: " + str(result[0]))
    enter_ad1.grid(row=14,column=0,columnspan=2,pady=(10,0))
    enter_ad2=Label(ad,text ="Job Position: " + str(result[1]))
    enter_ad2.grid(row=15,column=0,columnspan=2)
    enter_ad3=Label(ad,text ="Company: " + str(result[2]))
    enter_ad3.grid(row=16,column=0,columnspan=2)
    enter_ad4=Label(ad,text ="Salary: " + str(result[3]))
    enter_ad4.grid(row=17,column=0,columnspan=2)
    enter_ad5=Label(ad,text ="Cut Off Aptitude % : " + str(result[4]))
    enter_ad5.grid(row=18,column=0,columnspan=2)
    enter_ad6=Label(ad,text ="Cut Off Degree % : " + str(result[5]))
    enter_ad6.grid(row=19,column=0,columnspan=2)
    enter_ad7=Label(ad,text ="Work Experience Required: " + str(result[6]))
    enter_ad7.grid(row=20,column=0,columnspan=2)

    enter_jid.delete(0, END)
    
def adDelete():
    val = enter_jid.get()
    campusRecruitmentDB.ad_del(val)

    enter_jid.delete(0, END)
    
def comRegister():
    val = (company_id.get(),cname.get(),addr.get())
    campusRecruitmentDB.com_values(val)

    company_id.delete(0, END)
    cname.delete(0, END)
    addr.delete(0, END)

def comView():
    val = enter_cid.get()
    result = campusRecruitmentDB.com_view(val)
    
    enter_com1=Label(com,text ="Company ID:" + str(result[0]))
    enter_com1.grid(row=10,column=0,columnspan=2,pady=(20,0))
    enter_com2=Label(com,text ="Name:" + str(result[1]))
    enter_com2.grid(row=11,column=0,columnspan=2)
    enter_com3=Label(com,text ="Address:" + str(result[2]))
    enter_com3.grid(row=12,column=0,columnspan=2)

    enter_cid.delete(0, END)
        
'''def comUpdate():
    editor = Tk()
    editor.title('Update Company Profile')
    #p2 = PhotoImage(file = 'icons8-school-48.png')
    #editor.iconphoto(False, p1)
    editor.geometry("400x400")

    #clock
    def clock():
        hr = time.strftime("%H")
        minute = time.strftime("%M")
        sec = time.strftime("%S")

        my_label = Label(editor,text ="")
        my_label.grid(row=6,column=0,columnspan=2,pady=200)
        my_label.config(text="Time : " + hr + ":" + minute + ":" + sec)
        my_label.after(1000,clock)
    clock()

    #update function
    def update():
        val = enter_cid.get()
        campusRecruitmentDB.com_update(str(val),str(cname1),str(addr1))
        company_id1.delete(0, END)
        cname1.delete(0, END)
        addr1.delete(0, END)
        
    
    #creating textboxes
    company_id1=Entry(editor,width=50)
    company_id1.grid(row=0,column=1,pady=(20,0))
    
    
    cname1=Entry(editor,width=50)
    cname1.grid(row=1,column=1)

    addr1=Entry(editor,width=50)
    addr1.grid(row=3,column=1)

    #creating labels for textboxes
    label1 = Label(editor,text="Company ID")
    label1.grid(row=0,column=0,pady=(20,0))

    label2 = Label(editor,text="Name")
    label2.grid(row=1,column=0)

    label3 = Label(editor,text="Address")
    label3.grid(row=3,column=0)

    #creating save button
    comu = Button(editor,text="SAVE CHANGES",height=1,width=50,command=update)
    comu.grid(row=5,column=0,columnspan=2,pady=30)

    val = enter_cid.get()
    result = campusRecruitmentDB.com_view(val)
    enter_cid.delete(0, END)

    #filling text boxes
    company_id1.insert(0,result[0])
    cname1.insert(0,result[1])
    addr1.insert(0,result[2])'''
    
def comDelete():
    val = enter_cid.get()
    campusRecruitmentDB.com_del(val)

    enter_cid.delete(0, END)
    
#Student Homepage
def openStudent():
    global std1
    std1=Toplevel()
    std1.geometry('400x400')
    std1.title('Student Homepage')
    p1 = PhotoImage(file = 'icons8-school-48.png')
    std1.iconphoto(False, p1)

    #clock
    def clock():
        hr = time.strftime("%H")
        minute = time.strftime("%M")
        sec = time.strftime("%S")

        my_label = Label(std1,text ="")
        my_label.grid(row=5,column=1,pady=160)
        my_label.config(text="Time : " + hr + ":" + minute + ":" + sec)
        my_label.after(1000,clock)
    clock()

    #creating buttons for student homepage
    stdr = Button(std1,text="REGISTER",height=2,width=20,command=stdRegister)
    stdr.grid(row=0,column=1,padx=120,pady=60)
    stdp = Button(std1,text="LOGIN",height=2,width=20,command=stdLogin)
    stdp.grid(row=1,column=1)
    
student = Button(root,text="STUDENT",height=2,width=20,command=openStudent)
student.grid(row=0,column=1,padx=120,pady=60)

#Admin Homepage
def openAdmin():
    global job_id,jname,adcname,jsalary,min_aptiPercent,min_bePercent,min_workexp,enter_jid,ad
    ad=Toplevel()
    ad.geometry('500x500')
    ad.title('Admin Homepage')
    p1 = PhotoImage(file = 'icons8-school-48.png')
    ad.iconphoto(False, p1)

    #clock
    def clock():
        hr = time.strftime("%H")
        minute = time.strftime("%M")
        sec = time.strftime("%S")

        my_label = Label(ad,text ="")
        my_label.place(x=10,y=470)
        my_label.config(text="Time : " + hr + ":" + minute + ":" + sec)
        my_label.after(1000,clock)
    clock()

    #creating textboxes
    job_id=Entry(ad,width=50)
    job_id.grid(row=0,column=1,pady=(10,0))

    jname=Entry(ad,width=50)
    jname.grid(row=1,column=1)

    adcname=Entry(ad,width=50)
    adcname.grid(row=2,column=1)

    jsalary=Entry(ad,width=50)
    jsalary.grid(row=3,column=1)

    min_aptiPercent=Entry(ad,width=50)
    min_aptiPercent.grid(row=4,column=1)
    
    min_bePercent=Entry(ad,width=50)
    min_bePercent.grid(row=5,column=1)

    min_workexp = StringVar()
    min_workexp.set("Yes")
    yes=Radiobutton(ad,text="Yes",variable=min_workexp,value = "Yes")
    yes.grid(row=6,column=1,pady=(10,0))
    no=Radiobutton(ad,text="No",variable=min_workexp,value = "No")
    no.grid(row=7,column=1)

    enter_jid=Entry(ad,width=50)
    enter_jid.grid(row=9,column=1)

    #creating labels for textboxes
    label1 = Label(ad,text="Job ID")
    label1.grid(row=0,column=0,padx=50,pady=(10,0))

    label2 = Label(ad,text="Job Position")
    label2.grid(row=1,column=0,padx=50)

    label3 = Label(ad,text="Company")
    label3.grid(row=2,column=0)

    label4 = Label(ad,text="Salary")
    label4.grid(row=3,column=0)

    label5 = Label(ad,text="Cutoff Aptitude %")
    label5.grid(row=4,column=0)

    label6 = Label(ad,text="Cutoff Degree %")
    label6.grid(row=5,column=0)

    label7 = Label(ad,text="Work Experience Required")
    label7.grid(row=6,column=0,pady=(10,0))

    label7 = Label(ad,text="Enter Job ID")
    label7.grid(row=9,column=0,pady=10)

    #creating buttons
    adr = Button(ad,text="SUBMIT",height=1,width=50,command=submitApp)
    adr.grid(row=8,column=0,columnspan=2)

    adv = Button(ad,text="VIEW POST",height=1,width=50,command=adView)
    adv.grid(row=10,column=0,columnspan=2)

    #adu = Button(ad,text="UPDATE POST",height=1,width=50,command=adUpdate)
    #adu.grid(row=11,column=0,columnspan=2)

    add = Button(ad,text="DELETE POST",height=1,width=50,command=adDelete)
    add.grid(row=12,column=0,columnspan=2)

admin = Button(root,text="ADMIN",height=2,width=20,command=openAdmin)
admin.grid(row=1,column=1)

#Company Homepage
def openCompany():
    global company_id,cname,addr,enter_cid,com
    com=Toplevel()
    com.geometry('500x500')
    com.title('Company Homepage')
    p1 = PhotoImage(file = 'icons8-school-48.png')
    com.iconphoto(False, p1)

    def clock():
        hr = time.strftime("%H")
        minute = time.strftime("%M")
        sec = time.strftime("%S")

        my_label = Label(com,text ="")
        my_label.place(x=10,y=470)
        my_label.config(text="Time : " + hr + ":" + minute + ":" + sec)
        my_label.after(1000,clock)
    clock()

    #creating textboxes
    company_id=Entry(com,width=50)
    company_id.grid(row=0,column=1,pady=(10,0))
    
    cname=Entry(com,width=50)
    cname.grid(row=1,column=1)

    addr=Entry(com,width=50)
    addr.grid(row=3,column=1)

    enter_cid=Entry(com,width=50)
    enter_cid.grid(row=6,column=1)

    #creating labels for textboxes
    label1 = Label(com,text="Company ID")
    label1.grid(row=0,column=0,padx=50,pady=(10,0))

    label2 = Label(com,text="Name")
    label2.grid(row=1,column=0)

    label3 = Label(com,text="Address")
    label3.grid(row=3,column=0)

    label4 = Label(com,text="Enter Company ID")
    label4.grid(row=6,column=0,pady=20)

    #creating buttons
    comr = Button(com,text="REGISTER",height=1,width=50,command=comRegister)
    comr.grid(row=5,column=0,columnspan=2,pady=10)

    comd = Button(com,text="VIEW",height=1,width=50,command=comView)
    comd.grid(row=7,column=0,columnspan=2)

    #comu = Button(com,text="UPDATE",height=1,width=50,command=comUpdate)
    #comu.grid(row=8,column=0,columnspan=2)

    comv = Button(com,text="DELETE",height=1,width=50,command=comDelete)
    comv.grid(row=9,column=0,columnspan=2)

Com = Button(root,text="COMPANY",height=2,width=20,command=openCompany)
Com.grid(row=3,column=1,pady=60)





