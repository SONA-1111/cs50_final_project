from tkinter import*
from PIL import Image,ImageTk       #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class forget_page :
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("1350x700+0+0")
        #  Background Color
        self.root.configure(bg="white")


        #bg image
        self.bg=ImageTk.PhotoImage(file="images/bg.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relheight=1,relwidth=1)
        
        #left  image
        self.left=ImageTk.PhotoImage(file="images/login.jpg")
        left=Label(self.root,image=self.left,bg="white").place(x=50,y=100,height=500,width=400)
        
         #login frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=400,y=100,width=500,height=500)
        
        # Title Label
        title_label = Label(frame1, text="Forget Password", font=("Times New Roman", 20, "bold"), bg="white", fg="#303F9F")
        title_label.place(x=50, y=30)

        # Security Question
        security_question_label = Label(frame1, text="Security Question", font=("Times New Roman", 12), bg="white").place(x=50, y=140)
        self.security_question_combobox = ttk.Combobox(frame1, font=("Times New Roman", 12), state="readonly")
        self.security_question_combobox["values"] = ["Your first pet's name?", "Your birthplace?", "Your favorite color?"]
        self.security_question_combobox.place(x=50, y=170, width=200)
        self.security_question_combobox.current(0)

        # Security Answer
        security_answer_label = Label(frame1, text="Answer", font=("Times New Roman", 12), bg="white").place(x=50, y=210)
        self.security_answer_entry = Entry(frame1, font=("Times New Roman", 12), bg="#f0f0f0")
        self.security_answer_entry.place(x=50, y=240, width=200)
        
         # password
        new_password = Label(frame1, text="New Password", font=("Times New Roman", 12), bg="white").place(x=50, y=270)
        self.password_entry = Entry(frame1, font=("Times New Roman", 12), bg="#f0f0f0")
        self.password_entry.place(x=50, y=300, width=200)


        # Submit Button
        submit_button = Button(frame1, text="Change Password", font=("Times New Roman", 14), bg="#4CAF50", fg="white")
        submit_button.place(x=50, y=340,width=150)





if __name__=="__main__":
    root=Tk()
    obj = forget_page(root)
    root.mainloop()