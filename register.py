from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import os
import sqlite3
class RegistrationForm:
    def __init__(self, root):
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
        left=Label(self.root,image=self.left,bg="white").place(x=20,y=100,height=500,width=300)
        
         #register frame
        frame1=Frame(self.root,bg="white")
        frame1.place(x=300,y=100,width=700,height=500)
        
        # Title Label
        title_label = Label(frame1, text="Registration Form", font=("Times New Roman", 20, "bold"), bg="white", fg="#303F9F")
        title_label.place(x=50, y=30)
        
        
        # First Name
        first_name_label = Label(frame1, text="First Name", font=("Times New Roman", 12), bg="white").place(x=50, y=100)
        self.first_name_entry = Entry(frame1, font=("Times New Roman", 12), bg="#f0f0f0")
        self.first_name_entry.place(x=50, y=130, width=200)

        # Last Name
        last_name_label = Label(frame1, text="Last Name", font=("Times New Roman", 12), bg="white").place(x=370, y=100)
        self.last_name_entry = Entry(frame1, font=("Times New Roman", 12), bg="#f0f0f0")
        self.last_name_entry.place(x=370, y=130, width=200)

        # Contact Number
        contact_label = Label(frame1, text="Contact No.", font=("Times New Roman", 12), bg="white").place(x=50, y=170)
        self.contact_entry = Entry(frame1, font=("Times New Roman", 12), bg="#f0f0f0")
        self.contact_entry.place(x=50, y=200, width=200)

        # Email
        email_label = Label(frame1, text="Email", font=("Times New Roman", 12), bg="white").place(x=370, y=170)
        self.email_entry = Entry(frame1, font=("Times New Roman", 12), bg="#f0f0f0")
        self.email_entry.place(x=370, y=200, width=200)

        # Security Question
        security_question_label = Label(frame1, text="Security Question", font=("Times New Roman", 12), bg="white").place(x=50, y=240)
        self.security_question_combobox = ttk.Combobox(frame1, font=("Times New Roman", 12), state="readonly")
        self.security_question_combobox["values"] = ["Your first pet's name?", "Your birthplace?", "Your favorite color?"]
        self.security_question_combobox.place(x=50, y=270, width=200)
        self.security_question_combobox.current(0)

        # Security Answer
        security_answer_label = Label(frame1, text="Answer", font=("Times New Roman", 12), bg="white").place(x=370, y=240)
        self.security_answer_entry = Entry(frame1, font=("Times New Roman", 12), bg="#f0f0f0")
        self.security_answer_entry.place(x=370, y=270, width=200)
        

        # password
        password_name_label = Label(frame1, text="Password", font=("Times New Roman", 12), bg="white").place(x=50, y=310)
        self.password_name_entry = Entry(frame1, font=("Times New Roman", 12), bg="#f0f0f0")
        self.password_name_entry.place(x=50, y=340, width=200)

        # confirm password
        confirm_password_label = Label(frame1, text="Confirm Password", font=("Times New Roman", 12), bg="white").place(x=370, y=310)
        self.confirm_password_entry = Entry(frame1, font=("Times New Roman", 12), bg="#f0f0f0")
        self.confirm_password_entry.place(x=370, y=340, width=200)


       # Submit Button
        submit_button = Button(frame1, text="Submit", font=("Times New Roman", 14), bg="#4CAF50", fg="white",cursor="hand2", command=self.submit)
        submit_button.place(x=50, y=420,width=100)
        login_button = Button(frame1, text="Login", font=("Times New Roman", 14), bg="#303F9F", fg="white",cursor="hand2",command=self.login_page)
        login_button.place(x=170, y=420,width=100)



    def login_page(self):
        self.root.destroy()
        os.system("python login.py")


# Submit Function
    def submit(self):

        if self.first_name_entry.get() == "" or self.last_name_entry.get() == "" or self.email_entry.get() == "" or self.password_name_entry.get() == "" or self.confirm_password_entry.get() == "" or self.security_answer_entry.get() == "":
           messagebox.showerror("Error", "All fields are required",parent=self.root)
        elif self.password_name_entry.get() != self.confirm_password_entry.get():
            messagebox.showerror("Error", "Passwords do not match",parent=self.root)
        else:            
            try:
                con=sqlite3.connect(database="project.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.email_entry.get(),))
                row=cur.fetchone()
                if row!=None:
                     messagebox.showerror("Error", "User already exist",parent=self.root)
                else:
                    cur.execute("INSERT INTO employee (f_name, l_name,contact, email, question, answer, password) VALUES (?, ?, ?, ?, ?,?,?)",
                    (self.first_name_entry.get(), 
                    self.last_name_entry.get(),
                    self.contact_entry.get(), 
                    self.email_entry.get(),
                    self.security_question_combobox.get(),
                    self.security_answer_entry.get(), 
                    self.password_name_entry.get() 
                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Registration Success",parent=self.root)
                    self.clear()
                    self.login_page()
            except Exception as e:
                messagebox.showerror("Error", f"Error occurred: {e}",parent=self.root)

# Clear Fields Function
    def clear(self):
        self.first_name_entry.delete(0,END)
        self.last_name_entry.delete(0,END)
        self.email_entry.delete(0,END)
        self.contact_entry.delete(0,END)
        self.password_name_entry.delete(0,END)  
        self.confirm_password_entry.delete(0,END)
        self.security_question_combobox.delete(0,END)
        self.security_answer_entry.delete(0)
       

# Main Application
if __name__ == "__main__":
    root = Tk()
    app = RegistrationForm(root)
    root.mainloop()
