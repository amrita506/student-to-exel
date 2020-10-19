a = True #other buttons not clicked
import pandas as pd
from tkinter import *
root_menu = Tk()
root_menu.title("Welcome")
def main():
    if a == True:
        root_menu.destroy()
        root_main = Tk()
        root_main.title("student details to exel")

        label_student = Label(root_main, text = "Enter the student name: ")
        label_student.grid(row = 0, column = 0 )
        entry_student = Entry(root_main)
        entry_student.grid(row = 0, column = 1)

        label_maths = Label(root_main, text = "Enter the maths marks: ")
        label_maths.grid(row = 1, column = 0 )
        entry_maths = Entry(root_main)
        entry_maths.grid(row = 1, column = 1 )

        label_science = Label(root_main, text = "Enter the science marks: ")
        label_science.grid(row = 2, column = 0 )
        entry_science = Entry(root_main)
        entry_science.grid(row = 2, column = 1 )

        label_english = Label(root_main, text = "Enter the english marks: ")
        label_english.grid(row = 3, column = 0 )
        entry_english = Entry(root_main)
        entry_english.grid(row = 3, column = 1 )

        label_social = Label(root_main, text = "Enter the social marks: ")
        label_social.grid(row = 4, column = 0 )
        entry_social = Entry(root_main)
        entry_social.grid(row = 4, column = 1 )

        def enter():
            data[entry_student.get()] = [entry_maths.get(),entry_science.get(),entry_english.get(),entry_social.get()]
            df = pd.DataFrame(data)
            df.to_excel (r'/home/shikhar/Desktop/jupyter/pandas_data.xlsx', index = False, header=True)
            entry_student.delete(0, END)
            entry_maths.delete(0, END)
            entry_science.delete(0, END)
            entry_english.delete(0, END)
            entry_social.delete(0, END)
        add =  Button(root_main, text = "Enter", command = enter)
        add.grid(row = 5, column = 1)
        root_main.mainloop()
entry_directory = Entry(root_menu,width = 50)
if entry_directory.get != "":
    def directory():
        a = True
        directory = entry_directory.get() 
        button_main = Button(root_menu,text = "Continue=>",command = main)
        button_main.grid(row = 1, column = 3)
        entry_directory.get()
label_directory = Label(root_menu, text = "Enter the path for saving the file")
button_directory = Button(root_menu,text = "ENTER",command = directory)
entry_directory = Entry(root_menu,width = 50)
label_directory.grid(row = 0,column = 0)
entry_directory.grid(row = 0, column = 1,columnspan = 4)
button_directory.grid(row = 1, column = 2)
entry_directory.insert(0,"for help go to the link mentioned and read help.txt : https://bit.ly/3jc3iww")

def clear():
    entry_directory.delete(0, END)

clear_directory =Button(root_menu, text = "clear", command = clear)
clear_directory.grid(row = 1, column = 0)
root_menu.mainloop()
