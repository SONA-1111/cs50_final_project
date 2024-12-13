from tkinter import*
from PIL import Image,ImageTk       #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class studentClass :
    def __init__(self,root):
        self.root = root
        self.root.title("Academic Achievement Tracker")
        self.root.geometry("950x480+40+170")
        self.root.config(bg="#ebe9e1")
        self.root.focus_force()

        #title
        title = Label(self.root,text="Students Details",font=("goudy old style",20,"bold"),bg="#40051b",fg="#ffffff").place(x=10,y=15,width=930,height=35)
        
        #variables
        self.var_roll=StringVar()
        self.var_name = StringVar()
        self.var_email=StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact=StringVar()
        self.var_course=StringVar()
        self.var_a_date = StringVar()
        self.var_state=StringVar()
        self.var_city = StringVar()
        self.var_pin=StringVar()

        #widgets
        #colum1
        lbl_roll = Label(self.root,text="Roll No.",font=("goudy old style",10),bg="#ebe9e1").place(x=10, y=60)
        lbl_name = Label(self.root,text="Name",font=("goudy old style",10), bg="#ebe9e1").place(x=10 , y=100)
        lbl_email = Label(self.root,text="Email",font=("goudy old style",10), bg="#ebe9e1").place(x=10 , y=140)
        lbl_gender = Label(self.root,text="Gender",font=("goudy old style",10), bg="#ebe9e1").place(x=10 , y=180)
        lbl_state = Label(self.root,text="State",font=("goudy old style",10), bg="#ebe9e1").place(x=10 , y=220)
        
        lbl_address = Label(self.root,text="Address",font=("goudy old style",10), bg="#ebe9e1").place(x=10 , y=260)

         
        #entry field
        
        self.txt_roll = Entry(self.root,textvariable=self.var_roll,font=("goudy old style",12),bg="#ebe9e1")
        self.txt_roll.place(x=75, y=60, width=140)
        txt_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",10), bg="#ebe9e1").place(x=75 , y=100 , width=140)
        txt_email = Entry(self.root,textvariable=self.var_email,font=("goudy old style",10), bg="#ebe9e1").place(x=75 , y=140 , width=140)
        txt_state = Entry(self.root,textvariable=self.var_state,font=("goudy old style",10), bg="#ebe9e1").place(x=75 , y=220 , width=80)
        self.txt_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),font=("goudy old style",10), state='readonly',justify=CENTER)
        self.txt_gender.place(x=75 , y=180 , width=140)
        self.txt_gender.current(0)
        

        #column 2
        lbl_dob = Label(self.root,text="D.O.B",font=("goudy old style",10),bg="#ebe9e1").place(x=230, y=60)
        lbl_contact = Label(self.root,text="Contact",font=("goudy old style",10), bg="#ebe9e1").place(x=230 , y=100)
        lbl_addmission = Label(self.root,text="Addmission",font=("goudy old style",10), bg="#ebe9e1").place(x=230 , y=140)
        lbl_course = Label(self.root,text="Course",font=("goudy old style",10), bg="#ebe9e1").place(x=230 , y=180)
        lbl_city = Label(self.root,text="City",font=("goudy old style",10), bg="#ebe9e1").place(x=165 , y=220)
        lbl_pin = Label(self.root,text="Pin",font=("goudy old style",10), bg="#ebe9e1").place(x=295, y=220)
        
        
        #entry field
        self.course_list =[]
        #function call to update the list
        self.fetch_course()

        txt_dob = Entry(self.root,textvariable=self.var_dob,font=("goudy old style",10),bg="#ebe9e1").place(x=305, y=60, width=140)
        txt_contact = Entry(self.root,textvariable=self.var_contact,font=("goudy old style",10), bg="#ebe9e1").place(x=305 , y=100 , width=140)
        txt_addmission = Entry(self.root,textvariable=self.var_a_date,font=("goudy old style",10), bg="#ebe9e1").place(x=305 , y=140 , width=140)
        self.txt_course = ttk.Combobox(self.root,textvariable=self.var_course,values=self.course_list,font=("goudy old style",10), state='readonly',justify=CENTER)
        self.txt_course.place(x=305 , y=180 , width=140)
        self.txt_course.set("Select")
        txt_city = Entry(self.root,textvariable=self.var_city,font=("goudy old style",10), bg="#ebe9e1").place(x=205 , y=220 , width=80)
        txt_pin = Entry(self.root,textvariable=self.var_pin,font=("goudy old style",10), bg="#ebe9e1").place(x=330 , y=220 , width=80)


        self.txt_address = Text(self.root,font=("goudy old style",10), bg="#ebe9e1")
        self.txt_address.place(x=75 , y=260, width=300, height=100)

        #btn
        self.btn_add = Button(self.root,text="Save",font=("goudy old style",12),bg="green",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150, y=400, width=70,height=40)
        self.btn_update = Button(self.root,text="Update",font=("goudy old style",12),bg="#280540",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=225, y=400, width=70,height=40)
        self.btn_delete = Button(self.root,text="Delete",font=("goudy old style",12),bg="#400525",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=300, y=400, width=70,height=40)
        self.btn_clear = Button(self.root,text="Clear",font=("goudy old style",12),bg="#062936",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=375, y=400, width=70,height=40)

        #search
        #variabel
        self.var_search=StringVar()
        lbl_search_roll = Label(self.root,text="Roll No.",font=("goudy old style",12,"bold"),bg="#ebe9e1").place(x=500, y=60)
        txt_search_roll = Entry(self.root,textvariable=self.var_search,font=("goudy old style",12),bg="#ebe9e1").place(x=620, y=60, width=140)
        btn_search = Button(self.root,text="search",font=("goudy old style",12),bg="#062936",fg="white",cursor="hand2",command=self.search).place(x=760, y=60, width=60,height=22)
        #content
        self.c_frame = Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=500,y=100,width=445,height=340)

        scrolly = Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx = Scrollbar(self.c_frame,orient=HORIZONTAL)

        self.courseTabel = ttk.Treeview(self.c_frame,columns=("roll","name","email","gender","dob","contact","admission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.courseTabel.xview)
        scrolly.config(command=self.courseTabel.yview)

        self.courseTabel.heading("roll",text="Roll No")
        self.courseTabel.heading("name",text="Name")
        self.courseTabel.heading("email",text="Email")
        self.courseTabel.heading("gender",text="Gender")
        self.courseTabel.heading("dob",text="DOB")
        self.courseTabel.heading("contact",text="Contact")
        self.courseTabel.heading("admission",text="Admission")
        self.courseTabel.heading("course",text="Course")
        self.courseTabel.heading("state",text="State")
        self.courseTabel.heading("city",text="City")
        self.courseTabel.heading("pin",text="PIN")
        self.courseTabel.heading("address",text="Address")

        self.courseTabel["show"]='headings'

        self.courseTabel.column("roll",width=100)
        self.courseTabel.column("name",width=100)
        self.courseTabel.column("email",width=100)
        self.courseTabel.column("gender",width=100)
        self.courseTabel.column("dob",width=100)
        self.courseTabel.column("contact",width=100)
        self.courseTabel.column("admission",width=100)
        self.courseTabel.column("course",width=100)
        self.courseTabel.column("state",width=100)
        self.courseTabel.column("city",width=150)
        self.courseTabel.column("pin",width=100)
        self.courseTabel.column("address",width=100)


        self.courseTabel.pack(fill=BOTH,expand=1)
        self.courseTabel.bind("<ButtonRelease-1>",self.get_data)
        self.show()
 

 #clear function
    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("Select"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0",END),
        self.txt_roll.config(state=NORMAL) 
        self.var_search.set("")
        
# delete function
    def delete(self):
      con=sqlite3.connect(database="project.db")
      cur=con.cursor()
      try:
          if self.var_roll.get()=="":
              messagebox.showerror("Error","Roll Number should be required", parent=self.root)
          else:
              cur.execute("select * from student where roll=?",(self.var_roll.get(),))
              row=cur.fetchone()
              if row==None:
                  messagebox.showerror("Error","Please select student from the list", parent=self.root)
              else: 
                  op=messagebox.askyesno("Confirm", "Do you really want to delete?",parent=self.root)  
                  if op==True:
                      cur.execute("delete from student where roll=?",(self.var_roll.get(),))      
                      con.commit()     
                      messagebox.showinfo("Delete", "Student deleted", parent=self.root)
                      self.clear()
      except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 


#------------------------------------#
    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r = self.courseTabel.focus()
        content = self.courseTabel.item(r)
        row=content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0",END),
        self.txt_address.insert(END,row[11]),  
        


#add function

    def add(self):
      con=sqlite3.connect(database="project.db")
      cur=con.cursor()
      try:
          if self.var_roll.get()=="":
              messagebox.showerror("Error","Roll Number should be required", parent=self.root)
          else:
              cur.execute("select * from student where roll=?",(self.var_roll.get(),))
              row=cur.fetchone()
              if row!=None:
                  messagebox.showerror("Error","Roll Number already availabel", parent=self.root)
              else:
                  cur.execute("insert into student (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address)values(?,?,?,?,?,?,?,?,?,?,?,?)",(
                      self.var_roll.get(),
                      self.var_name.get(),
                      self.var_email.get(),
                      self.var_gender.get(),
                      self.var_dob.get(),
                      self.var_contact.get(),
                      self.var_a_date.get(),
                      self.var_course.get(),
                      self.var_state.get(),
                      self.var_city.get(),
                      self.var_pin.get(),
                      self.txt_address.get("1.0",END).strip(),
                  ))
                  con.commit()
                  messagebox.showinfo("Success","Student Added",parent=self.root)
                  self.show()
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}")   

#update function


    def update(self):
      con=sqlite3.connect(database="project.db")
      cur=con.cursor()
      try:
          if self.var_roll.get()=="":
              messagebox.showerror("Error","Roll No. should be required", parent=self.root)
          else:
              cur.execute("select * from student where roll=?",(self.var_roll.get(),))
              row=cur.fetchone()
              if row==None:
                  messagebox.showerror("Error","Select student from list", parent=self.root)
              else:
                  cur.execute("UPDATE student set name=?, email=?, gender=?, dob=?, contact=?, admission=?,course=?, state=?, city=?, pin=?, address=? where roll=?",(

                    self.var_name.get(),
                    self.var_email.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_contact.get(),
                    self.var_a_date.get(),
                    self.var_course.get(),
                    self.var_state.get(),
                    self.var_city.get(),
                    self.var_pin.get(),
                    self.txt_address.get("1.0",END).strip(),
                    self.var_roll.get(),
                  ))
                  con.commit()
                  messagebox.showinfo("Success","Student updated",parent=self.root)
                  self.show()
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}")   







#show function

    def show(self):
      con=sqlite3.connect(database="project.db")
      cur=con.cursor()
      try:
              cur.execute("select * from student ")
              rows=cur.fetchall()
              self.courseTabel.delete(*self.courseTabel.get_children())
              for row in rows:
                  self.courseTabel.insert('',END,values=row)
              
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}") 

#fetch course

    def fetch_course(self):
      con=sqlite3.connect(database="project.db")
      cur=con.cursor()
      try:
        cur.execute("select name from course ")
        rows=cur.fetchall()
        if len(rows)>0:
            for row in rows:
              self.course_list.append(row[0])
              
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}") 

#search

    def search(self):
      con=sqlite3.connect(database="project.db")
      cur=con.cursor()
      try:
              cur.execute(f"select * from student where roll=?",(self.var_search.get(),))
              row=cur.fetchone()
              if row!=None:
                 self.courseTabel.delete(*self.courseTabel.get_children())
                 self.courseTabel.insert('',END,values=row)
              else:
                 messagebox.showerror("Error","No record found",parent=self.root)
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}") 

if __name__=="__main__":
    root=Tk()
    obj = studentClass(root)
    root.mainloop()