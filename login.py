from tkinter import*
from PIL import Image,ImageTk       #pip install pillow
from tkinter import ttk,messagebox
import os
import sqlite3
class login_Form :
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
        title_label = Label(frame1, text="Login Form", font=("Times New Roman", 20, "bold"), bg="white", fg="#303F9F")
        title_label.place(x=50, y=30)

        
        # Email
        email_label = Label(frame1, text="Email Address", font=("Times New Roman", 12), bg="white").place(x=50, y=140)
        self.email_entry = Entry(frame1, font=("Times New Roman", 12), bg="#f0f0f0")
        self.email_entry.place(x=50, y=170, width=200)
        
         # password
        password_lbl = Label(frame1, text="Password", font=("Times New Roman", 12), bg="white").place(x=50, y=220)
        self.password_entry = Entry(frame1, font=("Times New Roman", 12), bg="#f0f0f0")
        self.password_entry.place(x=50, y=250, width=200)
       
        register_label = Button(frame1, text="Register New Account", font=("Times New Roman", 10), fg="#B00857",bd=0,bg="white",cursor="hand2",command=self.register_page).place(x=50, y=280)
        forget_label = Button(frame1, text="Forget Password?", font=("Times New Roman", 10), fg="#B00857",bd=0,bg="white",cursor="hand2",command=self.forget_page).place(x=50, y=305)

        # Submit Button
        submit_button = Button(frame1, text="Login", font=("Times New Roman", 14), bg="#4CAF50", fg="white",cursor="hand2",command=self.login)
        submit_button.place(x=50, y=350,width=150)

    def register_page(self):
        self.root.destroy()
        os.system("python register.py")


    def reset(self):
        self.question_combobox.current(0)
        self.new_password_entry.delete(0,END)
        self.answer_entry.delete(0,END)
        self.password_entry.delete(0,END)
        self.email_entry.delete(0,END)


    def fgt_password(self):
       if self.question_combobox.get()=="Your first pet's name?" or self.answer_entry.get()=="" or self.new_password_entry.get() == "":
          messagebox.showerror("Error", "All fields are required",parent=self.root2)
       else:

          try:
               con=sqlite3.connect(database="cs50_final_project.db")
               cur = con.cursor()

               # Query to verify user credentials
               cur.execute("SELECT * FROM employee WHERE email=? and question=? and answer=?", (self.email_entry.get(),self.question_combobox.get(),self.answer_entry.get(),))
               row = cur.fetchone()

               if row is None:
                    messagebox.showerror("Error", "Please select the correct Queston / enter answer", parent=self.root2)
               else:
                cur.execute("update employee set password=? WHERE email=? ", (self.new_password_entry.get(),self.email_entry.get(),))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Your password has been reset, please login with new password",parent=self.root2)
                self.reset()
                self.root2.destroy()
          except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root2)




    def forget_page(self):
        if self.email_entry.get()=="":
            messagebox.showerror("Error", "Please enter the email address to reset your password", parent=self.root2)
        else:
            try:
                
                con=sqlite3.connect(database="cs50_final_project.db")
                cur = con.cursor()

               # Query to verify user credentials
                cur.execute("SELECT * FROM employee WHERE email=?", (self.email_entry.get(),))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Please enter the valid email address to reset your password", parent=self.root)
                
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget password")
                    self.root2.geometry("350x400+450+150")
                    self.root2.configure(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    title_label = Label(self.root2, text="Forget Password", font=("Times New Roman", 20, "bold"), bg="white", fg="#303F9F")
                    title_label.place(x=0, y=10,relwidth=1)

                    # Security Question
                    security_question = Label(self.root2, text="Security Question", font=("Times New Roman", 12), bg="white").place(x=80, y=100)
                    self.question_combobox = ttk.Combobox(self.root2, font=("Times New Roman", 12), state="readonly")
                    self.question_combobox["values"] = ["Your first pet's name?", "Your birthplace?", "Your favorite color?"]
                    self.question_combobox.place(x=80, y=130, width=200)
                    self.question_combobox.current(0)

                    # Security Answer
                    security_answer = Label(self.root2, text="Answer", font=("Times New Roman", 12), bg="white").place(x=80, y=160)
                    self.answer_entry = Entry(self.root2, font=("Times New Roman", 12), bg="#f0f0f0")
                    self.answer_entry.place(x=80, y=190, width=200)
        
                     # password
                    new_password = Label(self.root2, text="New Password", font=("Times New Roman", 12), bg="white").place(x=80, y=220)
                    self.new_password_entry = Entry(self.root2, font=("Times New Roman", 12), bg="#f0f0f0")
                    self.new_password_entry.place(x=80, y=250, width=200)
                    # Submit Button
                    sub_button = Button(self.root2, text="Reset Password", font=("Times New Roman", 14), bg="#4CAF50", fg="white",cursor="hand2",command=self.fgt_password)
                    sub_button.place(x=80, y=290,width=200)
                   
               
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)

        
            

    #login
    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # Check if fields are empty
        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            con=sqlite3.connect(database="cs50_final_project.db")
            cur = con.cursor()

            # Query to verify user credentials
            cur.execute("SELECT * FROM employee WHERE email=? AND password=?", (email, password))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)
                
            else:
                messagebox.showinfo("Success", f"Welcome {row[1]}", parent=self.root)
                self.root.destroy()
                os.system("python main.py")
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}", parent=self.root)

      



if __name__=="__main__":
    root=Tk()
    obj = login_Form(root)
    root.mainloop()