from tkinter import *
        
def display():
    #the card's string representation will be grabbed in here
    label2['text'] = "This is the card's string representation"

def clear():
    label2['text'] = ""


#GUI starts here
root = Tk()

topframe = Frame(root)
topframe.pack(side=TOP)

framerow1 = Frame(root)
framerow1.pack()

framerow2 = Frame(root)
framerow2.pack()

framerow21 = Frame(framerow2)
framerow21.pack()

framerow22 = Frame(framerow2)
framerow22.pack()

bottomframe= Frame(root)
bottomframe.pack(side=BOTTOM)

label = Label(topframe, text="Monopoly")
label.pack()

but1 = Button(framerow1, command = (lambda: display()), text="Crumlin")
but1.pack(side=LEFT)

but2 = Button(framerow1, command = (lambda: display()), text="Kimmage")
but2.pack(side=LEFT)

but3 = Button(framerow1, command = (lambda: display()), text="Bus")
but3.pack(side=LEFT)

but4 = Button(framerow1, command = (lambda: display()), text="Rathgar Road")
but4.pack(side=LEFT)

but5 = Button(framerow1, command = (lambda: display()), text="South Circular Road")
but5.pack(side=LEFT)

but6 = Button(framerow1, command = (lambda: display()), text="Rathmines Road")
but6.pack(side=LEFT)

but7 = Button(framerow21, command = (lambda: display()), text="Shrewsbury Road")
but7.pack(side=LEFT)

but8 = Button(framerow22, command = (lambda: display()), text="Dawson Street")
but8.pack(side=RIGHT)

label2 = Label(bottomframe, text="")
label2.pack(side=TOP)

but6 = Button(bottomframe, command = (lambda: clear()), text="Clear text")
but6.pack(side=BOTTOM)
    
root.mainloop()


"""prop = [("Crumblin: Colour:Brown, Cost:60, Rent:2, State:Unowned"), \
        ("Kimmage: Colour:Brown, Cost:60, Rent:4, State:Unowned"), \
        ("Bus: Cost:200, Rent:25, State:Unowned"), \
        ("Rathgar_Road: Colour:Lightblue, Cost:100, Rent:6, State:Unowned"), \
        ("South_Circular_Road: Colour:Lightblue, Cost:100, Rent:6, State:Unowned"),\
        ("Rathmines_Road: Colour:Lightblue, Cost:120, Rent:8, State:Unowned")]
for item in prop:
    board.addpiece(item)"""


