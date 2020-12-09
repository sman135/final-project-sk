"""
Spence's Cookie Clicker
Spencer Kolman
Computer science
"""
#Imports
import tkinter
import tkinter as tk
import sys
#Constants
root = tkinter.Tk()
image2 =Image.open()
image1 = Imageroot.PhotoImage(image2)
root.geometry("500x500+10+20")
root.title("Cookie Clicker Version 0.9")
root.maxsize(500, 500)
root.minsize(500, 500)
#Variables
clickValue = 1 #Amount of points per click
counter = tkinter.IntVar()
#Functions
def quit(): #Quits window
    root.quit()
def mainClick(event=None): #Adds clicks to total points
    counter.set(counter.get() + clickValue)
def buy2(): #Changes click value to 2
    global clickValue
    if counter.get() >= 50:
        clickValue = 2
        btn3.configure(bg = "green")
        btn3["state"] = "disabled"
        counter.set(counter.get() - 50)
def buy3(): #Changes click value to 3
    global clickValue
    if counter.get() >= 150:
        clickValue = 3
        btn4.configure(bg = "green")
        btn4["state"] = "disabled"
        counter.set(counter.get() - 150)
#Labels
lbl1 = tkinter.Label(root, text = "Click the button to gain points!", fg = "black", font = ("Arial", 16))
lbl2 = tkinter.Label(root, textvariable = counter) #Points displayed.
lbl3 = tkinter.Label(root, text = "Total points:", fg = "black", font = ("Arial", 9))
lbl4 = tkinter.Label(root, text = "Click value: 2", fg = "black", font = ("Arial", 7))
lbl5 = tkinter.Label(root, text = "50 points", fg = "black", font = ("Arial", 7))
lbl6 = tkinter.Label(root, text = "Click value: 3", fg = "black", font = ("Arial", 7))
lbl7 = tkinter.Label(root, text = "150 points", fg = "black", font = ("Arial", 7))
lbl1.place(x = 110, y = 25)
lbl2.place(x = 200, y = 55)
lbl3.place(x = 130, y = 55)
lbl4.place(x = 395, y = 205)
lbl5.place(x = 455, y = 225)
lbl6.place(x = 395, y = 255)
lbl7.place(x = 455, y = 275)
#Buttons
btn1 = tkinter.Button(root, text = "Click me!", command = mainClick, fg = "blue") #When clicked adds current point value to counter.
btn2 = tkinter.Button(root, text = "Quit", command = quit) #Quits window.
btn3 = tkinter.Button(root, text = "Buy", command = buy2)
btn4 = tkinter.Button(root, text = "Buy", command = buy3)
btn1.place(x = 225, y = 250)
btn2.place(x = 440, y = 470)
btn3.place(x = 440, y = 200)
btn4.place(x = 440, y = 250)

#Main code
root.mainloop() #Starts tkinter code.
