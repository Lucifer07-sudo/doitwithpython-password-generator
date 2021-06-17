# importing the tkinter module
from tkinter import *

# importing the pyperclip module to use it to copy our generated 
# password to clipboard
import pyperclip

from tkinter import messagebox

# random module will be used in generating the random password
import random

# initializing the tkinter
root = Tk()
root.title("Password Generator")
root['bg']="black"

# setting the width and height of the gui
root.geometry("400x400")    # x is small case here

#making windows non-resizeable
root.resizable(0,0)

# declaring a variable of string type and this variable will be 
# used to store the password generated
passstr = StringVar()

# declaring a variable of integer type which will be used to 
# store the length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)


# function to generate the password
def generate():
    # storing the keys in a list which will be used to generate 
    # the password 
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']
    pass2 = [' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    # declaring the empty string
    password = ""

    # loop to generate the random password of the length entered           
    # by the user
    try:
        password=password+random.choice(pass2)
        random.shuffle(password)
        for x in range(passlen.get()-1):
            password=password+random.choice(pass1)
        passstr.set(password)
    except:
        messagebox.showerror("Error", "Enter a number you stupid human!")

    



    

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# Creating a text label widget
Label(root, text="Password Generator Application \nby @doitwithpython", font="calibri 20 bold",bg='black',fg='green').pack()

# Creating a text label widget
Label(root, text="Enter password length",font="calibri 15 bold",bg='black',fg='green').pack(pady=3)

# Creating a entry widget to take password length entered by the 
# user

Entry(root, textvariable=passlen, width=30, font="calibri 15 bold").pack(pady=3)

# button to call the generate function
Button(root, text="Generate Password",font="calibri 15 bold", bg='cyan',fg='purple',command=generate).pack(pady=7)

#delete entry content


# entry widget to show the generated password
Entry(root, textvariable=passstr, width=30, font="calibri 15 bold").pack(pady=3)

# button to call the copytoclipboard function
Button(root, text="Copy to clipboard",font="calibri 15 bold",bg='cyan',fg='purple', command=copytoclipboard).pack()

# mainloop() is an infinite loop used to run the application when 
# it's in ready state 
root.mainloop()
