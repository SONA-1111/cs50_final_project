from tkinter import*
from PIL import Image,ImageTk       #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class TotalCourse :
    def __init__(self,root):
        self.root = root
        self.root.title("Academic Achievement Tracker")
        self.root.geometry("950x480+40+170")
        self.root.config(bg="#ebe9e1")
        self.root.focus_force()

        #title
        title = Label(self.root,text="Course Details",font=("goudy old style",20,"bold"),bg="#40051b",fg="#ffffff").place(x=10,y=15,width=930,height=35)
        
        #variables
        self.var_course=StringVar()
        self.var_duration = StringVar()
        self.var_charges=StringVar()

        #widgets
        lbl_courseName = Label(self.root,text="Course Name",font=("goudy old style",12,"bold"),bg="#ebe9e1").place(x=10, y=60)
        lbl_duration = Label(self.root,text="Duration",font=("goudy old style",12,"bold"),bg="#ebe9e1").place(x=10 , y=100)
        lbl_charges = Label(self.root,text="Charges",font=("goudy old style",12,"bold"),bg="#ebe9e1").place(x=10 , y=140)
        lbl_description = Label(self.root,text="Description",font=("goudy old style",12,"bold"),bg="#ebe9e1").place(x=10 , y=180)
         
        #entry field
        
        self.txt_courseName = Entry(self.root,textvariable=self.var_course,font=("goudy old style",12,"bold"),bg="#ebe9e1")
        self.txt_courseName.place(x=140, y=60, width=160)
        txt_duration = Entry(self.root,textvariable=self.var_duration,font=("goudy old style",12,"bold"),bg="#ebe9e1").place(x=140 , y=100 , width=160)
        txt_charges = Entry(self.root,textvariable=self.var_charges,font=("goudy old style",12,"bold"),bg="#ebe9e1").place(x=140 , y=140 , width=160)
        self.txt_description = Text(self.root,font=("goudy old style",12,"bold"),bg="#ebe9e1")
        self.txt_description.place(x=140 , y=180, width=300, height=120)

        #btn
        self.btn_add = Button(self.root,text="Save",font=("goudy old style",12,"bold"),bg="green",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150, y=400, width=70,height=40)
        self.btn_update = Button(self.root,text="Update",font=("goudy old style",12,"bold"),bg="#280540",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=225, y=400, width=70,height=40)
        self.btn_delete = Button(self.root,text="Delete",font=("goudy old style",12,"bold"),bg="#400525",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=300, y=400, width=70,height=40)
        self.btn_clear = Button(self.root,text="Clear",font=("goudy old style",12,"bold"),bg="#062936",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=375, y=400, width=70,height=40)

        #search
        #variabel
        self.var_search=StringVar()
        lbl_search_courseName = Label(self.root,text="Course Name",font=("goudy old style",12,"bold"),bg="#ebe9e1").place(x=500, y=60)
        txt_search_courseName = Entry(self.root,textvariable=self.var_search,font=("goudy old style",12),bg="#ebe9e1").place(x=620, y=60, width=140)
        btn_search = Button(self.root,text="search",font=("goudy old style",12),bg="#062936",fg="white",cursor="hand2",command=self.search).place(x=760, y=60, width=60,height=22)
        #content
        self.c_frame = Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=500,y=100,width=445,height=340)

        scrolly = Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx = Scrollbar(self.c_frame,orient=HORIZONTAL)

        self.courseTabel = ttk.Treeview(self.c_frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        
        scrollx.config(command=self.courseTabel.xview)
        scrolly.config(command=self.courseTabel.yview)

        self.courseTabel.heading("cid",text="ID")
        self.courseTabel.heading("name",text="Name")
        self.courseTabel.heading("duration",text="Duration")
        self.courseTabel.heading("charges",text="Charges")
        self.courseTabel.heading("description",text="Description")
        self.courseTabel["show"]='headings'
        self.courseTabel.column("cid",width=50)
        self.courseTabel.column("name",width=100)
        self.courseTabel.column("duration",width=100)
        self.courseTabel.column("charges",width=100)
        self.courseTabel.column("description",width=150)
        self.courseTabel.pack(fill=BOTH,expand=1)
        self.courseTabel.bind("<ButtonRelease-1>",self.get_data)
        self.show()


 #clear function
    def clear(self):
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)
# delete function
    def delete(self):
      con=sqlite3.connect(database="cs50_final_project.db")
      cur=con.cursor()
      try:
          if self.var_course.get()=="":
              messagebox.showerror("Error","Course Name should be required", parent=self.root)
          else:
              cur.execute("select * from course where name=?",(self.var_course.get(),))
              row=cur.fetchone()
              if row==None:
                  messagebox.showerror("Error","Please select course from the list", parent=self.root)
              else: 
                  op=messagebox.askyesno("Confirm", "Do you really want to delete?",parent=self.root)  
                  if op==True:
                      cur.execute("delete from course where name=?",(self.var_course.get(),))      
                      con.commit()     
                      messagebox.showinfo("Delete", "Course deleted", parent=self.root)
                      self.clear()
      except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 
#------------------------------------#
    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        r = self.courseTabel.focus()
        content = self.courseTabel.item(r)
        row=content["values"]
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])




    def add(self):
      con=sqlite3.connect(database="cs50_final_project.db")
      cur=con.cursor()
      try:
          if self.var_course.get()=="":
              messagebox.showerror("Error","Course Name should be required", parent=self.root)
          else:
              cur.execute("select * from course where name=?",(self.var_course.get(),))
              row=cur.fetchone()
              if row!=None:
                  messagebox.showerror("Error","Course Name already availabel", parent=self.root)
              else:
                  cur.execute("insert into course (name,duration,charges,description)values(?,?,?,?)",(
                      self.var_course.get(),
                      self.var_duration.get(),
                      self.var_charges.get(),
                      self.txt_description.get("1.0",END).strip(),
                  ))
                  con.commit()
                  messagebox.showinfo("Success","Course Added",parent=self.root)
                  self.show()
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}")   

#update function


    def update(self):
      con=sqlite3.connect(database="cs50_final_project.db")
      cur=con.cursor()
      try:
          if self.var_course.get()=="":
              messagebox.showerror("Error","Course Name should be required", parent=self.root)
          else:
              cur.execute("select * from course where name=?",(self.var_course.get(),))
              row=cur.fetchone()
              if row==None:
                  messagebox.showerror("Error","select course from list", parent=self.root)
              else:
                  cur.execute("UPDATE course set duration=?, charges=?, description=? where name=?",(
                      
                      self.var_duration.get(),
                      self.var_charges.get(),
                      self.txt_description.get("1.0",END),
                      self.var_course.get(),
                  ))
                  con.commit()
                  messagebox.showinfo("Success","Course updated",parent=self.root)
                  self.show()
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}")   







#show function

    def show(self):
      con=sqlite3.connect(database="cs50_final_project.db")
      cur=con.cursor()
      try:
              cur.execute("select * from course ")
              rows=cur.fetchall()
              self.courseTabel.delete(*self.courseTabel.get_children())
              for row in rows:
                  self.courseTabel.insert('',END,values=row)
              
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}") 
#search
    def search(self):
      con=sqlite3.connect(database="cs50_final_project.db")
      cur=con.cursor()
      try:
              cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
              rows=cur.fetchall()
              self.courseTabel.delete(*self.courseTabel.get_children())
              for row in rows:
                  self.courseTabel.insert('',END,values=row)
              
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}") 

if __name__=="__main__":
    root=Tk()
    obj = TotalCourse(root)
    root.mainloop()