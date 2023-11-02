from tkinter import *

from tkinter import ttk
root = Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")


#input box creation here
frame1=Frame(root)
frame1.pack()
titlelabel= Label(frame1,text="Tic Tac Toe",font=("Arial",30),bg="yellow")
titlelabel.pack()


frame2=Frame(root)
frame2.pack()
turn='X'
def play(event):
    global  turn
    button=event.widget
    if turn == "X":
    #button text change
      button['text'] = "X"
      turn = "O"
    else:
        button['text'] = "O"
        turn = "X"



    #we create grid or button
#tic toc board

#first row
button1=Button(frame2,text="" ,width=4,height=2,font=("Arial",35),bg='yellowgreen',relief=RAISED,borderwidth=5)
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)

button1=Button(frame2,text="",width=4,height=2,font=("Arial",35),bg='yellowgreen',relief=RAISED,borderwidth=5)
button1.grid(row=0,column=1)
button1.bind("<Button-1>",play)

button1=Button(frame2,text="",width=4,height=2,font=("Arial",35),bg='yellowgreen',relief=RAISED,borderwidth=5)
button1.grid(row=0,column=2)
button1.bind("<Button-1>",play)

frame3=Frame(root)
frame3.pack()
#second row
button1=Button(frame3,text="" ,width=4,height=2,font=("Arial",35),bg='yellowgreen',relief=RAISED,borderwidth=5)
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)

button1=Button(frame3,text="",width=4,height=2,font=("Arial",35),bg='yellowgreen',relief=RAISED,borderwidth=5)
button1.grid(row=0,column=1)
button1.bind("<Button-1>",play)

button1=Button(frame3,text="",width=4,height=2,font=("Arial",35),bg='yellowgreen',relief=RAISED,borderwidth=5)
button1.grid(row=0,column=2)
button1.bind("<Button-1>",play)
frame4=Frame(root)
frame4.pack()


#third row
button1=Button(frame4,text="" ,width=4,height=2,font=("Arial",35),bg='yellowgreen',relief=RAISED,borderwidth=5 )
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)
button1=Button(frame4,text="",width=4,height=2,font=("Arial",35),bg='yellowgreen',relief=RAISED,borderwidth=5)
button1.grid(row=0,column=1)
button1.bind("<Button-1>",play)
button1=Button(frame4,text="",width=4,height=2,font=("Arial",35),bg='yellowgreen',relief=RAISED,borderwidth=5)
button1.grid(row=0,column=2)
button1.bind("<Button-1>",play)
##titlelabel= Label(frame1,text="Tic Tac Toe",font=("Arial",30),bg="yellow")
##titlelabel.pack()


root.mainloop()
