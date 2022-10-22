from tkinter import *
from tkinter import ttk
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    mi = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime('%d')
    moth = time.strftime('%m')
    year = time.strftime("%y")
    day = time.strftime("%a")

    lb_hr.config(text=hr)
    lb_mi.config(text=mi)
    lb_sec.config(text=sec)
    lb_am.config(text=am)
    lb_hr1.config(text=date)
    lb_mi1.config(text=moth)
    lb_sec1.config(text=year)
    lb_am1.config(text=day)
    #lb_date.config(text=date)
    #lb_moth.config(text=moth)
    #lb_year.config(text=year)
    #lb_day.config(text=day)
    lb_hr.after(200,date_time)

a = Tk()
a.config(bg="Black")
a.title("*******!!! DIGITAL CLOCK !!!*********")
a.geometry("1000x600")
a.resizable(False,False)
lb = Label(a,text="K.P CLOCK",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb.place(x=200,y=5,height=120,width=600)
#--------------------------------------------------1
lb_hr = Label(a,text="00",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_hr.place(x=24,y=130,height=140,width=220)

lb_mi = Label(a,text="00",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_mi.place(x=268,y=130,height=140,width=220)

lb_sec = Label(a,text="00",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_sec.place(x=512,y=130,height=140,width=220)

lb_am = Label(a,text="00",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_am.place(x=756,y=130,height=140,width=220)
#--------------------------------------------------2
lb_1 = Label(a,text="HOUR",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_1.place(x=24,y=290,height=57.5,width=220)

lb_2 = Label(a,text="MIN",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_2.place(x=268,y=290,height=57.5,width=220)

lb_3 = Label(a,text="SEC",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_3.place(x=512,y=290,height=57.5,width=220)

lb_4 = Label(a,text="AM/PM",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_4.place(x=756,y=290,height=57.5,width=220)
#--------------------------------------------------
lb_hr1 = Label(a,text="00",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_hr1.place(x=24,y=377.5,height=140,width=220)

lb_mi1 = Label(a,text="00",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_mi1.place(x=268,y=377.5,height=140,width=220)

lb_sec1 = Label(a,text="00",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_sec1.place(x=512,y=377.5,height=140,width=220)

lb_am1 = Label(a,text="00",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_am1.place(x=756,y=377.5,height=140,width=220)
#--------------------------------------------------4
lb_5 = Label(a,text="DATE",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_5.place(x=24,y=537.5,height=57.5,width=220)

lb_6 = Label(a,text="MON",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_6.place(x=268,y=537.5,height=57.5,width=220)

lb_7 = Label(a,text="YEAR",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_7.place(x=512,y=537.5,height=57.5,width=220)

lb_8 = Label(a,text="DAY",font=("Time New Roman",60,"bold"),bg="Aqua",fg="Black")
lb_8.place(x=756,y=537.5,height=57.5,width=220)


date_time()
a.mainloop()