import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import Menu

win = tk.Tk()
win.title("Python GUI")

# We are creating a container frame to hold all other widgets # 1
monty = ttk.LabelFrame(win, text=' Monty Python ')
monty.grid(column=0, row=0)
aLabel = ttk.Label(monty, text="A Label")

# Modified Button Click Function

def clickMe():
    action.configure(text='Hello ' + name.get()+ ' ' +
        numberChosen.get())

action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

# Button Entry
ttk.Label(win, text="Enter a name:").grid(column=0, row=0, sticky='W')
name = tk.StringVar()

nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky=tk.W)
nameEntered.focus()

# Combobox Button
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()

numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 3, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state
='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Toggle", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)


scrolW = 38
scrolH = 3
scr    = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH,
        wrap=tk.WORD)

scr.grid(column=0, columnspan=3, sticky='WE')

# First, we change our Radiobutton global variables into a list.
colors = ["Blue", "Gold", "Red"]

# Radiobutton Callback # 5
def radCall():
    radSel      =  radVar.get()
    if   radSel == 1: win.configure(background=colors[0])
    elif radSel == 2: win.configure(background=colors[1])
    elif radSel == 3: win.configure(background=colors[2])


# create three Radiobuttons
radVar = tk.IntVar()
radVar.set(99)

for col in range(3):
    curRad = 'red' + str(col)
    curRad = tk.Radiobutton(win, text=colors[col],
        variable=radVar, value=col+1, command=radCall)
    curRad.grid(column=col, row=9, sticky=tk.W)


#  Using a scrolled Text control


# Create a contaier to hold labels
labelsFrame = ttk.LabelFrame(win, text=' Labels in  a Frame ')
labelsFrame.grid(column=1, row=10, padx=20, pady=40) 
 
 
# # # # # # # Place labels into the container elements
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=1, row=0)
ttk.Label(labelsFrame, text="Label3").grid(column=2, row=0)

# menuBar
menuBar = Menu(win)
win.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit")

win.mainloop()
