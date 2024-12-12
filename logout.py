from tkinter import*
from PIL import Image,ImageTk
class CourseLogout :
    def __init__(self,root):
        self.root = root
        self.root.title("Academic Achievement Tracker")
        self.root.geometry("950x480+40+170")
        self.root.config(bg="white")





if __name__=="__main__":
    root=Tk()
    obj = CourseLogout(root)
    root.mainloop()