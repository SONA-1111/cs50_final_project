from tkinter import*
from PIL import Image,ImageTk
from course import TotalCourse
from result import CourseResult
from student import studentClass
from view import resultView
from tkinter import messagebox
import sqlite3
import os
class StuManagement :
    def __init__(self,root):
        self.root = root
        self.root.title("Academic Achievement Tracker")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #icons
        self.logo_dash=ImageTk.PhotoImage(file="images/logo.ico")
        #title
        title = Label(self.root,text="Academic Achievement Tracker",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#40051b",fg="#ffffff").place(x=0,y=0,relwidth=1,height=50)
        #menu
        A_frames = LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="#ffffff")
        A_frames.place(x=25,y=70,width=980,height=80)

        btn_course = Button(A_frames,text="Course",font=("times new roman",14,"bold"),bg="#40051b",fg="#ffffff",cursor="hand2", command=self.add_course).place(x=20,y=5,width=115,height=40)
        btn_student = Button(A_frames,text="Student",font=("times new roman",14,"bold"),bg="#40051b",fg="#ffffff",cursor="hand2", command=self.add_student).place(x=225,y=5,width=115,height=40)
        btn_result = Button(A_frames,text="Result",font=("times new roman",14,"bold"),bg="#40051b",fg="#ffffff",cursor="hand2", command=self.add_result).place(x=435,y=5,width=115,height=40)
        btn_view = Button(A_frames,text="View Result",font=("times new roman",15,"bold"),bg="#40051b",fg="#ffffff",cursor="hand2", command=self.total_view).place(x=645,y=5,width=115,height=40)
        btn_logout = Button(A_frames,text="Logout",font=("times new roman",14,"bold"),bg="#40051b",fg="#ffffff",cursor="hand2",command=self.logout).place(x=850,y=5,width=115,height=40)
        #btn_exit = Button(A_frames,text="Exit",font=("times new roman",14,"bold"),bg="#0b5377",fg="#ffffff",cursor="hand2").place(x=1100,y=5,width=100,height=40)
        
        #content window
        self.bg_img=Image.open("images/students.jpg")
        self.bg_img = self.bg_img.resize((750,350),Image.LANCZOS)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root,image=self.bg_img).place(x=120,y=200,width=750,height=350)
        
        #update details
        self.lbl_course = Label(self.root,text="Total Courses\n[0]",font=("times new roman",15),bg="#280540",fg="white",bd=10,relief=RIDGE)
        self.lbl_course.place(x=150,y=530,width=200,height=100)

        self.lbl_student = Label(self.root,text="Total Students\n[0]",font=("times new roman",15),bg="#400525",fg="white",bd=10,relief=RIDGE)
        self.lbl_student.place(x=400,y=530,width=200,height=100)

        self.lbl_result = Label(self.root,text="Total Results\n[0]",font=("times new roman",15),bg="#062936",fg="white",bd=10,relief=RIDGE)
        self.lbl_result.place(x=650,y=530,width=200,height=100)


        
        #footer
        footer = Label(self.root,text="Academic Achievement Tracker",font=("goudy old style",12),bg="#262626",fg="#ffffff").pack(side=BOTTOM,fill=X)
        self.update_details()
        
       
       #details
    def update_details(self):
        con=sqlite3.connect(database="project.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course ")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Course : {str(len(cr))}") 
            # self.lbl_course.after(200,self.update_details)  

            cur.execute("select * from student ")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students : {str(len(cr))}")
            # self.lbl_student.after(200,self.update_details)      

            cur.execute("select * from result ")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results : {str(len(cr))}")

            self.lbl_course.after(200,self.update_details) 

        except Exception as ex:
           messagebox.showerror("Error",f"Error due to {str(ex)}")      
       
       
       #cousrse
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = TotalCourse(self.new_win)

    #result
    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = CourseResult(self.new_win)

    #student
    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    #view
    def total_view(self):
        self.new_win=Toplevel(self.root)
        self.new_obj = resultView(self.new_win)

   #logout 
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?" , parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")


if __name__=="__main__":
    root=Tk()
    obj = StuManagement(root)
    root.mainloop()