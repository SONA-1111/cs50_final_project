from tkinter import*
from PIL import Image,ImageTk       #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class CourseResult :
    def __init__(self,root):
        self.root = root
        self.root.title("Academic Achievement Tracker")
        self.root.geometry("950x480+40+170")
        self.root.config(bg="#ebe9e1")
        self.root.focus_force()

        #title
        title = Label(self.root,text="Add Students Results",font=("goudy old style",20,"bold"),bg="#40051b",fg="#ffffff").place(x=10,y=15,width=930,height=50)
        

        #widgets
        #variabels
        self.var_roll =StringVar()
        self.var_name =StringVar()
        self.var_course =StringVar()
        self.var_marks =StringVar()
        self.var_total_marks =StringVar()
        self.roll_list = []
        self.fetch_roll()
        lbl_select = Label(self.root,text="Select Student",font=("goudy old style",12,"bold"),bg="#ebe9e1").place(x=50, y=100)
        lbl_name = Label(self.root,text="Name",font=("goudy old style",12,"bold"), bg="#ebe9e1").place(x=50 , y=160)
        lbl_course = Label(self.root,text="Course",font=("goudy old style",12,"bold"), bg="#ebe9e1").place(x=50 , y=220)
        lbl_marks_ob = Label(self.root,text="Marks Obtained",font=("goudy old style",12,"bold"), bg="#ebe9e1").place(x=50 , y=280)
        lbl_totalMarks = Label(self.root,text="Total Marks",font=("goudy old style",12,"bold"), bg="#ebe9e1").place(x=50 , y=340)

        self.txt_student = ttk.Combobox(self.root,textvariable=self.var_roll,values=self.roll_list,font=("goudy old style",10), state='readonly',justify=CENTER)
        self.txt_student.place(x=190 , y=100 , width=120, height=28)
        self.txt_student.set("Select")

        btn_search = Button(self.root,text="search",font=("goudy old style",12),bg="green",fg="white",cursor="hand2",command=self.search).place(x=320, y=100, width=65,height=28)

        txt_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",12),bg="white",state="readonly").place(x=190, y=160, width=200 , height=28)
        txt_course = Entry(self.root,textvariable=self.var_course,font=("goudy old style",12),bg="white",state='readonly').place(x=190, y=220, width=200 , height=28)
        txt_mark_ob = Entry(self.root,textvariable=self.var_marks,font=("goudy old style",12),bg="white").place(x=190, y=280, width=200 , height=28)
        txt_tatal_marks = Entry(self.root,textvariable=self.var_total_marks,font=("goudy old style",12),bg="white").place(x=190, y=340, width=200 , height=28)
        
        #btn
        btn_add = Button(self.root,text="Submit",font=("goudy old style",14),bg="green",fg="white",activebackground="lightgreen",cursor="hand2",command=self.add).place(x= 200, y=420, width=80, height=35)
        btn_clear = Button(self.root,text="Clear",font=("goudy old style",14),bg="#062936",fg="white",activebackground="lightgray",cursor="hand2",command=self.clear).place(x=300 , y=420, width=80, height=35)
         
        #image

        self.bg_img=Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((480,350),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root,image=self.bg_img).place(x=450,y=100,width=480,height=350)
        
#fetch course

    def fetch_roll(self):
      con=sqlite3.connect(database="project.db")
      cur=con.cursor()
      try:
        cur.execute("select roll from student ")
        rows=cur.fetchall()
        if len(rows)>0:
            for row in rows:
              self.roll_list.append(row[0])
              
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}") 

#search

    def search(self):
      con=sqlite3.connect(database="project.db")
      cur=con.cursor()
      try:
              cur.execute(f"select name,course from student where roll=?",(self.var_roll.get(),))
              row=cur.fetchone()
              if row!=None:
                 self.var_name.set(row[0])
                 self.var_course.set(row[1])
              else:
                 messagebox.showerror("Error","No record found",parent=self.root)
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}") 

#add function

    def add(self):
      con=sqlite3.connect(database="project.db")
      cur=con.cursor()
      try:
          if self.var_name.get()=="":
              messagebox.showerror("Error","please first search student record", parent=self.root)
          else:
              cur.execute("select * from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get(),))
              row=cur.fetchone()
              if row!=None:
                  messagebox.showerror("Error","Result already availabel", parent=self.root)
              else:
                  per=(int(self.var_marks.get())*100)/int(self.var_total_marks.get())
                  cur.execute("insert into result(roll,name,course,marks_ob,total_marks,per)values(?,?,?,?,?,?)",(
                      self.var_roll.get(),
                      self.var_name.get(),
                      self.var_course.get(),
                      self.var_marks.get(),
                      self.var_total_marks.get(),
                      str(per)

                  ))
                  con.commit()
                  messagebox.showinfo("Success","Result Added",parent=self.root)
                  
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}")   


    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks.set(""),
        self.var_total_marks.set(""),

if __name__=="__main__":
    root=Tk()
    obj = CourseResult(root)
    root.mainloop()