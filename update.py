import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect("database.db")
c=conn.cursor()

class Application:
    def __init__(self,master):
        self.master=master

        # Heading label
        self.heading=Label(master,text=" Update Appointment",fg="steelblue",font=(" arial 40 bold"))
        self.heading.place(x=150,y=0)

        self.name=Label(master,text="Enter patient's name ",font=("arial 18 bold"))
        self.name.place(x=0,y=60)

        self.namenet=Entry(master,width=30)
        self.namenet.place(x=280,y=62)

        self.search=Button(master,text="Search",width=12,height=2,bg="steelblue",command=self.search_db)
        self.search.place(x=350,y=100)

        self.show = Button(self.master, text="Show details", width=20, height=2, bg="lightblue", command=self.show_info)
        self.show.place(x=650, y=100)


    def show_info(self):
        sql4="select * from appointmentnew"
        p=c.execute(sql4)
        self.valnew=str()
        for r in p:
            valnew=r
            self.box = Text(self.master, width=82, height=30,)
            self.box.place(x=520, y=180)
            self.valnew = " name: " + str(r[0]) + " age: " + str(r[1]) + " gender: " + str(r[2]) + " phone: " + str(
                                r[3]) + " location: " + str(r[4]) + " time: " + str(r[5]) + "\n" +self.valnew
            self.box.insert(END,self.valnew
                            )


    def search_db(self):
        self.input=self.namenet.get()
        #sql part
        sql="select * from appointmentnew where name LIKE ?"
        self.r=c.execute(sql,(self.input,))
        for self.row in self.r:
            self.name1=self.row[0]
            self.age=self.row[1]
            self.gender=self.row[2]
            self.phone=self.row[3]
            self.location=self.row[4]
            self.time=self.row[5]


        self.uname=Label(self.master,text="Patient's Name",font=("arial 18 bold"))
        self.uname.place(x=0,y=140)

        self.uage = Label(self.master, text="Age", font=("arial 18 bold"))
        self.uage.place(x=0, y=180)

        self.ugender = Label(self.master, text="Gender", font=("arial 18 bold"))
        self.ugender.place(x=0, y=220)

        self.uphone = Label(self.master, text="Phone_no", font=("arial 18 bold"))
        self.uphone.place(x=0, y=260)

        self.ulocation = Label(self.master, text="Location", font=("arial 18 bold"))
        self.ulocation.place(x=0, y=300)

        self.utime = Label(self.master, text="Appointment Time", font=("arial 18 bold"))
        self.utime.place(x=0, y=340)

        self.ent1=Entry(self.master,width=30)
        self.ent1.place(x=300,y=140)
        self.ent1.insert(END,str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=180)
        self.ent2.insert(END,str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=220)
        self.ent3.insert(END,str(self.gender))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=260)
        self.ent4.insert(END,str(self.phone))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=300)
        self.ent5.insert(END,str(self.location))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=340)
        self.ent6.insert(END,str(self.time))


        self.update=Button(self.master,text="Update",width=20,height=2,bg="lightblue",command=self.update_db)
        self.update.place(x=400,y=380)

        self.delete=Button(self.master,text="Delete",width=20,height=2,bg="red",command=self.delete_db)
        self.delete.place(x=250,y=380)



    def delete_db(self):
        sql4=" delete from appointmentnew where name like ?"
        c.execute(sql4,(self.namenet.get(),))
        conn.commit()
        messagebox.showinfo("Success","Successfully deleted")

    def update_db(self):
        self.val1=self.ent1.get()
        self.val2=self.ent2.get()
        self.val3=self.ent3.get()
        self.val4=self.ent4.get()
        self.val5=self.ent5.get()
        self.val6=self.ent6.get()
        sql3=" update appointmentnew set Name=?,Age=?,Gender=?,Phone=?,Location=?,Time=? where name like ?"
        c.execute(sql3,(self.val1,self.val2,self.val3,self.val4,self.val5,self.val6,self.namenet.get()))
        conn.commit()
        messagebox.showinfo("Success","Successfully updated")
root=Tk()
b=Application(root)
root.geometry("1200x720+0+0")
root.resizable(False,False)
root.mainloop()
