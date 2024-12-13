from tkinter import*
from PIL import Image,ImageTk       #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class resultView :
    def __init__(self,root):
        self.root = root
        self.root.title("Academic Achievement Tracker")
        self.root.geometry("950x480+40+170")
        self.root.config(bg="#ebe9e1")
        self.root.focus_force()

        #title
        title = Label(self.root,text="View Students Results",font=("goudy old style",20,"bold"),bg="#40051b",fg="#ffffff").place(x=10,y=15,width=930,height=35)
     
        #search
        self.var_search=StringVar()
        self.var_id=""
        lbl_search = Label(self.root,text="Search By roll No.",font=("goudy old style",14,"bold"),bg="#ebe9e1").place(x=250, y=100)
        txt_search = Entry(self.root,textvariable=self.var_search,font=("goudy old style",14,"bold"),bg="#ebe9e1").place(x=425, y=100,width=150)
        btn_search = Button(self.root,text="Search",font=("goudy old style",12),bg="green",fg="#ebe9e1",cursor="hand2",command=self.search).place(x=576, y=100, width=65,height=25)
        btn_clear = Button(self.root,text="Clear",font=("goudy old style",12),bg="gray",fg="#ebe9e1",cursor="hand2",command=self.clear).place(x=645, y=100, width=65,height=25)
        #label

        lbl_roll = Label(self.root,text="Roll No.",font=("goudy old style",12,"bold"),bg="#ebe9e1", bd=2, relief=GROOVE).place(x=30, y=230,width=150,height=50)
        lbl_name = Label(self.root,text="Name",font=("goudy old style",12,"bold"), bg="#ebe9e1", bd=2,relief=GROOVE).place(x=180 , y=230, width=150,height=50)
        lbl_course = Label(self.root,text="Course",font=("goudy old style",12,"bold"), bg="#ebe9e1", bd=2,relief=GROOVE).place(x=330 , y=230, width=150,height=50)
        lbl_marks_ob = Label(self.root,text="Marks Obtained",font=("goudy old style",12, "bold") ,bg="#ebe9e1",bd=2,relief=GROOVE).place(x=480 , y=230, width=150,height=50)
        lbl_total_Marks = Label(self.root,text="Total Marks",font=("goudy old style",12,"bold"),bg="#ebe9e1",bd=2,relief=GROOVE).place(x=630 , y=230, width=150,height=50)
        lbl_per = Label(self.root,text="Percentage",font=("goudy old style",12,"bold"),bg="#ebe9e1", bd=2,relief=GROOVE).place(x=780, y=230, width=150,height=50)
        
        self.roll = Label(self.root,font=("goudy old style",12,"bold"),bg="#ebe9e1", bd=2, relief=GROOVE)
        self.roll.place(x=30, y=280,width=150,height=50)
        self.name = Label(self.root,font=("goudy old style",12,"bold"), bg="#ebe9e1", bd=2,relief=GROOVE)
        self.name.place(x=180 , y=280, width=150,height=50)
        self.course = Label(self.root,font=("goudy old style",12,"bold"), bg="#ebe9e1", bd=2,relief=GROOVE)
        self.course.place(x=330 , y=280, width=150,height=50)
        self.marks_ob = Label(self.root,font=("goudy old style",12, "bold") ,bg="#ebe9e1",bd=2,relief=GROOVE)
        self.marks_ob.place(x=480 , y=280, width=150,height=50)
        self.total_Marks = Label(self.root,font=("goudy old style",12,"bold"),bg="#ebe9e1",bd=2,relief=GROOVE)
        self.total_Marks.place(x=630 , y=280, width=150,height=50)
        self.per = Label(self.root,font=("goudy old style",12,"bold"),bg="#ebe9e1", bd=2,relief=GROOVE)
        self.per.place(x=780, y=280, width=150,height=50)
        
        #delete btn
        btn_delete = Button(self.root,text="Delete",font=("goudy old style",12,"bold"),bg="#280540",fg="white",cursor="hand2",command=self.delete).place(x=400, y=350, width=150,height=35)

#search

    def search(self):
      con=sqlite3.connect(database="project.db")
      cur=con.cursor()
      try:
              if self.var_search.get()=="":
                  messagebox.showerror("Error","Roll No. should be required",parent=self.root)
              else:
                  
                cur.execute(f"select * from result where roll=?",(self.var_search.get(),))
                row=cur.fetchone()
                if row!=None:
                  self.var_id=row[0]
                  self.roll.config(text=row[1])
                  self.name.config(text=row[2])
                  self.course.config(text=row[3])
                  self.marks_ob.config(text=row[4])
                  self.total_Marks.config(text=row[5])
                  self.per.config(text=row[6])
                else:
                 messagebox.showerror("Error","No record found",parent=self.root)
      except Exception as ex:
          messagebox.showerror("Error",f"Error due to {str(ex)}") 

    def clear(self):
        self.var_id=""
        self.roll.config(text=""),
        self.name.config(text=""),
        self.course.config(text=""),
        self.marks_ob.config(text=""),
        self.total_Marks.config(text=""),
        self.per.config(text=""),
        self.var_search.set(""),


# delete function
    def delete(self):
      con=sqlite3.connect(database="project.db")
      cur=con.cursor()
      try:
          if self.var_id=="":
              messagebox.showerror("Error","Search students results first", parent=self.root)
          else:
              cur.execute("select * from result where rid=?",(self.var_id,))
              row=cur.fetchone()
              if row==None:
                  messagebox.showerror("Error","Invalid student result", parent=self.root)
              else: 
                  op=messagebox.askyesno("Confirm", "Do you really want to delete?",parent=self.root)  
                  if op==True:
                      cur.execute("delete from result where rid=?",(self.var_id,))      
                      con.commit()     
                      messagebox.showinfo("Delete", "Result deleted", parent=self.root)
                      self.clear()
      except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}") 




if __name__=="__main__":
    root=Tk()
    obj = resultView(root)
    root.mainloop()