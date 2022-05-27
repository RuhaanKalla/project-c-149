# -*- coding: utf-8 -*-
"""
Created on Tue May 24 16:45:43 2022

@author: dell
"""
from tkinter import*
import random
root = Tk()
root.title("Password Generator")
root.geometry("500x500")
root.configure(background = "lightpink")

label = Label(root,bg = "lightpink" , fg = "purple" , font = 25)

array_1d = ["a" , "b" , "c" , "d" , "e" , "f" , "g", "h" , "i" , "j" , "k" , "l", "m" , "o" , "p" , "q", "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z"]

def word():
    random_1 = random.randint(0 , 25)
    random_2 = random.randint(0 , 25)
    random_3 = random.randint(0 , 25)
    random_4 = random.randint(0 , 25)
    random_5 = random.randint(0 , 25)
    
    letter_1 = str(array_1d[random_1])
    letter_2 = str(array_1d[random_2])
    letter_3 = str(array_1d[random_3])
    letter_4 = str(array_1d[random_4])
    letter_5 = str(array_1d[random_5])
    
    label["text"] = letter_1 + letter_2 + letter_3 + letter_4 + letter_5
    
btn = Button(root , bg = "purple" , fg = "lightpink" , font = 25 , text = "generate" , command = word)    
btn.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)
label.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)

root.mainloop()  