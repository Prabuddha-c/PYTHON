#Digital Clock using Python

from tkinter import*
import datetime

def date_time():
    time=datetime.datetime.now()
    hr=time.strftime('%I')
    mi=time.strftime('%M')
    sc=time.strftime('%S')
    ap=time.strftime('%p')
    lab_hr.config(text=hr)
    lab_min.config(text=mi)
    lab_sec.config(text=sc)
    lab_ampm.config(text=ap)
    lab_hr.after(200,date_time)

clock=Tk()
clock.title("Digital Clock")
clock.geometry("1000x250")
clock.config(bg='light blue')

lab_hr=Label(clock,text='00',font=('Time New Roman',60,'bold'),bg='red',fg='white')
lab_hr.place(x=120,y=50,height=110,width=100)
lab_hr_txt=Label(clock,text='Hour',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_hr_txt.place(x=120,y=190,height=40,width=100)

lab_min=Label(clock,text='00',font=('Time New Roman',60,'bold'),bg='red',fg='white')
lab_min.place(x=340,y=50,height=110,width=100)
lab_min_txt=Label(clock,text='Min',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_min_txt.place(x=340,y=190,height=40,width=100)

lab_sec=Label(clock,text='00',font=('Time New Roman',60,'bold'),bg='red',fg='white')
lab_sec.place(x=560,y=50,height=110,width=100)
lab_sec_txt=Label(clock,text='Sec',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_sec_txt.place(x=560,y=190,height=40,width=100)

lab_ampm=Label(clock,text='00',font=('Time New Roman',50,'bold'),bg='red',fg='white')
lab_ampm.place(x=780,y=50,height=110,width=100)
lab_ampm_txt=Label(clock,text='AM/PM',font=('Time New Roman',20,'bold'),bg='red',fg='white')
lab_ampm_txt.place(x=780,y=190,height=40,width=100)

date_time()

clock.mainloop()