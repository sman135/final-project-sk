#Imports
import tkinter
import sys
import time
#Constants
root = tkinter.Tk()
root.geometry('500x500+10+20')
root.title('Spence\'s Cookie Clicker Version 1.0')
root.maxsize(500, 500)
root.minsize(500, 500)
root.config(bg = 'Wheat')
#Variables
clickValue = 1 #Amount of points per click
counter = tkinter.IntVar()
prestigeLevel = 0
#Functions
def quit(): #Quits window
    root.quit()
def mainClick(event=None): #Adds clicks to total points
    counter.set(counter.get() + clickValue)
def buy2(): #Changes click value to 2
    global clickValue
    if counter.get() >= 50:
        clickValue *= 2
        btn3.configure(bg = 'Wheat')
        btn3['state'] = 'disabled'
        counter.set(counter.get() - 50)
def buy3(): #Changes click value to 3
    global clickValue
    if counter.get() >= 150:
        clickValue *= 3
        btn4.configure(bg = 'Wheat')
        btn4['state'] = 'disabled'
        counter.set(counter.get() - 150)
def prestige(): #Resets cookies to 0 but default click is increased by 5
    global clickValue
    global prestigeLevel
    if counter.get() >= 250:
        prestigeLevel += 1
        clickValue = 0
        clickValue += 5 * prestigeLevel
        btn5.configure(bg = 'Wheat')
        counter.set(0)
        btn3['state'] = 'normal'
        btn4['state'] = 'normal'
#Labels
lbl1 = tkinter.Label(root, text = 'Click the button to get cookies!', fg = 'black', font = ('Arial', 16), bg='Wheat')
lbl2 = tkinter.Label(root, textvariable = counter, bg = 'Wheat') #Points displayed.
lbl3 = tkinter.Label(root, text = 'Total cookies:', fg = 'black', font = ('Arial', 11), bg = 'Wheat')
lbl4 = tkinter.Label(root, text = 'Click value X2', fg = 'black', font = ('Arial', 9), bg = 'Wheat')
lbl5 = tkinter.Label(root, text = '50 points', fg = 'black', font = ('Arial', 9), bg = 'Wheat')
lbl6 = tkinter.Label(root, text = 'Click value X3', fg = 'black', font = ('Arial', 9), bg = 'Wheat')
lbl7 = tkinter.Label(root, text = '150 points', fg = 'black', font = ('Arial', 9), bg = 'Wheat')
lbl8 = tkinter.Label(root, text = 'Prestige \n(Cookies reset to 0\n but default click\n increased by 5)', fg = 'black', font = ('Arial', 9), bg = 'Wheat')
lbl9 = tkinter.Label(root, text = '250 points', fg = 'black', font = ('Arial', 9), bg = 'Wheat')
lbl1.place(x = 140, y = 25)
lbl2.place(x = 270, y = 53)
lbl3.place(x = 200, y = 55)
lbl4.place(x = 380, y = 205)
lbl5.place(x = 450, y = 225)
lbl6.place(x = 380, y = 255)
lbl7.place(x = 450, y = 275)
lbl8.place(x = 360, y = 290)
lbl9.place(x = 450, y = 325)
#Buttons
btn1 = tkinter.Button(root, text = 'Click me!', command = mainClick, fg = 'blue', highlightbackground = 'Wheat') #When clicked adds current point value to counter.
btn2 = tkinter.Button(root, text = 'Quit', command = quit, highlightbackground = 'Wheat') #Quits window.
btn3 = tkinter.Button(root, text = 'Buy', command = buy2, highlightbackground = 'Wheat')
btn4 = tkinter.Button(root, text = 'Buy', command = buy3, highlightbackground = 'Wheat')
btn5 = tkinter.Button(root, text = 'Buy', command = prestige, highlightbackground = 'Wheat')
btn1.place(x = 225, y = 250)
btn2.place(x = 440, y = 470)
btn3.place(x = 440, y = 200)
btn4.place(x = 440, y = 250)
btn5.place(x = 440, y = 300)
#Shapes (resembles chocolate chips)
choco1=tkinter.Label(root, text = 'choco', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco1.place(x = 100, y = 100)
choco2=tkinter.Label(root, text = 'choco', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco2.place(x = 150, y = 200)
choco3=tkinter.Label(root, text = 'choco', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco3.place(x = 90, y = 400)
choco4=tkinter.Label(root, text = 'choco', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco4.place(x = 300, y = 300)
choco5=tkinter.Label(root, text = 'choco', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco5.place(x = 350, y = 375)
choco6=tkinter.Label(root, text = 'choco', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco6.place(x = 375, y = 150)
choco7=tkinter.Label(root, text = 'cho', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco7.place(x = 385, y = 140)
choco8=tkinter.Label(root, text = 'cho', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco8.place(x = 110, y = 90)
choco9=tkinter.Label(root, text = 'cho', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco9.place(x = 160, y = 190)
choco10=tkinter.Label(root, text = 'cho', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco10.place(x = 100, y = 390)
choco11=tkinter.Label(root, text = 'cho', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco11.place(x = 310, y = 290)
choco12=tkinter.Label(root, text = 'cho', fg = 'SaddleBrown', font = ('Arial', 16), bg='SaddleBrown')
choco12.place(x = 360, y = 365)
#Main code
root.mainloop() #Starts tkinter code.
