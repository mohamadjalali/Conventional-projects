from tkinter import *
import sqlite3
import mysql.connector as mc

class DB():

    def __init__(self):
#         self.conn   = sqlite3.connect('mysq.db')
#         self.cursor = self.conn.cursor()
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS people
#                 (id INTEGER PRIMARY KEY, name TEXT, phone TEXT)''')
#         self.conn.commit()
        self.conn = mc.connect(
                host='localhost',
                user='root',
                passwd='',
                database='phone_gui'
        )

        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS people
            (id INT AUTO_INCREMENT PRIMARY KEY, name TEXT, phone TEXT)''')
        self.conn.commit()


    def helpp(self):
        help(mc)

    def show(self):
        self.cursor.execute('SELECT * FROM people')
        for row in self.cursor.fetchall():
            print(row)
    
    def insert(self):
        name1  = textin.get()
        phone1 = textinn.get()
        self.cursor.execute('''INSERT INTO people(name, phone)
                VALUES(%s,%s)''',(name1,phone1))
        self.conn.commit()
    
    def updateContact(self):
        nam = name.get()
        ph  = phone.get()
        self.cursor.execute('''UPDATE people SET
                        name=%s WHERE phone=%s''',(nam,ph))
        self.conn.commit()

    def det(self):
        dee=dell.get()
        self.cursor.execute('''DELETE FROM
                        people WHERE name=%s''',(dee,))
        self.conn.commit()

    def drop(self):
        self.cursor.execute("DROP table people")
        self.conn.commit()


g = DB()

root = Tk()
root.geometry('410x450')
root.title('DataBase using Sqlite3 and Tkinter')
root.configure(background='powder blue')


# Name Entry StringVar
textin  = StringVar()
# Phone Entry StringVar
textinn = StringVar()
# Update Name Entry StringVar
name    = StringVar()
# Provide phone No. Entry StringVar
phone   = StringVar()
# Delete Entry StringVar
dell    = StringVar()


# TODO MenuBar
menu=Menu(root)
root.config(menu=menu)

subm = Menu(menu)
menu.add_cascade(label='Help', menu=subm)
subm.add_command(label='Sqlite3 Docs', command=g.helpp)

 
# phone label
lab=Label(root,text='Name:', font=('none 13 bold'))
lab.place(x=0,y=0)
# phone label
lab1=Label(root,text='Phone:',font=('none 13 bold'))
lab1.place(x=0,y=40)

# name Entry
entname=Entry(root,width=20,font=('none 13 bold'), textvar=textin)
entname.place(x=80,y=0)
# phone Entry
entphone=Entry(root,width=20,font=('none 13 bold'), textvar=textinn)
entphone.place(x=80,y=40)

# Submin Button
but=Button(root,padx=2,pady=2,text='Submin',command=g.insert,font=('none 13 bold'))
but.place(x=80,y=100)
# Show Button
res=Button(root,padx=2,pady=2,text='Show',command=g.show,font=('none 13 bold'))
res.place(x=180,y=100)

# Update label
labuname=Label(root,text="Update Name :",font=('none 13 bold'))
labuname.place(x=0,y=200)

# Provide Phone No. label
labuphone=Label(root,text='Provide Phone No. :',font=('none 13 bold'))
labuphone.place(x=0,y=240)

# update name Entry
enttupadtename=Entry(root,width=20,font=('none 13 bold'),textvar=name)
enttupadtename.place(x=160,y=200)

# update phone Entry
entupdatephone=Entry(root,width=20,font=('none 13 bold'),textvar=phone)
entupdatephone.place(x=210,y=240)

# Update Button
buttupdate=Button(root,padx=2,pady=2,text='Update',command=g.updateContact,
    font=('none 13 bold'))
buttupdate.place(x=80,y=280)

# Delete label
labdelete=Label(root,text='Delete :', font=('none 13 bold'))
labdelete.place(x=0,y=340)

# Delete Name Entry
endelete=Entry(root,width=20,textvar=dell,font=('none 13 bold'))
endelete.place(x=90,y=340)

# Delete Button Entry
butdel=Button(root,padx=2,pady=2,text='Delete',command=g.det,font=('none 13 bold'))
butdel.place(x=90,y=380)

# Drop table Button
buttdrop=Button(root,padx=2,pady=2,text='Drop table',command=g.drop,
         font=('none 13 bold'))
buttdrop.place(x=180,y=380)



root.mainloop()
