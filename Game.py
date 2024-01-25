import tkinter as tk                    
from tkinter import ttk
import time

root = tk.Tk()
root.title("TextBox RPG") 
tabControl = ttk.Notebook(root)

def SelectJob(Job):
    global SelectedJob
    if SelectedJobLabel['text'] == "\n\nIdle\n\n":
        SelectedJobLabel['text'] = Job['text']
        SelectedJob = Job
        SelectedJob['state'] = "disabled"
        StartJobButton['state'] = "enabled"
    else:
        SelectedJob['state'] = "enabled"
        SelectedJob = Job
        SelectedJobLabel['text'] = Job['text']
        SelectedJob['state'] = "disabled"
        

def StartJob():
    while True:
        if pb['value'] < 80:
            StartJobButton['state'] = "disabled"
            pb['value'] += 20
            root.update_idletasks()
            time.sleep(1)
        else:
            StartJobButton['state'] = "enabled"
            pb['value'] = 0
            root.update_idletasks()
            break


SelectedJobLabel = ttk.Label(root, text = "\n\nIdle\n\n")
SelectedJobLabel.grid(column=0,row=0,columnspan=2)
# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

StartJobButton = ttk.Button(root, text = "Start Job", command = StartJob)
StartJobButton['state'] = "disabled"
StartJobButton.grid(column=0, row=2, columnspan=2)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Stats')
tabControl.add(tab2, text ='Farming')
tabControl.add(tab3, text ='Mining')
tabControl.add(tab4, text ='Magic')
tabControl.add(tab5, text ='Adventure')
tabControl.add(tab6, text ='Bag')

tabControl.grid(columnspan = 2, pady = 15)

ttk.Label(tab1, 
      text ="Level = ").grid(column = 2, 
                        row = 0,
                        rowspan = 3,
                        padx = 30,
                        pady = 30)

Farm1 = ttk.Button(tab2, text="Plow Dirt", command = lambda: SelectJob(Farm1))
Farm1.grid(column = 0, row = 0, padx = 5, pady = 5)
Farm2 = ttk.Button(tab2, text="Plant Seeds", command= lambda: SelectJob(Farm2))
Farm2.grid(column = 1, row = 0, padx = 5, pady = 5)
Farm3 = ttk.Button(tab2, text="Harvest Crops", command= lambda: SelectJob(Farm3))
Farm3.grid(column = 2, row = 0, padx = 5, pady = 5)

Mine1 = ttk.Button(tab3, text="Swing Pickaxe", command= lambda: SelectJob(Mine1))
Mine1.grid(column = 0, row = 0, padx = 5, pady = 5)

Magic1 = ttk.Button(tab4, text="\n\n      Work at Library      \n\n", command= lambda: SelectJob(Magic1))
Magic1.grid(column = 0, row = 0, rowspan = 3, padx = 5)
Magic2 = ttk.Button(tab4, text="\n\n     Spy on Lessons      \n\n", command= lambda: SelectJob(Magic2))
Magic2.grid(column = 1, row = 0, rowspan = 3, padx = 5)
Magic3 = ttk.Button(tab4, text="\n\n          Steal Books          \n\n", command= lambda: SelectJob(Magic3))
Magic3.grid(column = 2, row = 0, rowspan = 3, padx = 5, pady = 5)
#Magic4 = ttk.Button(tab4, text="         Read Books         ", command= lambda: SelectJob(Magic4))
#Magic4.grid(column = 0, row = 1, padx = 5, pady = 5)
#Magic5 = ttk.Button(tab4, text="Learn Magic Symbols", command= lambda: SelectJob(Magic5))
#Magic5.grid(column = 1, row = 1, padx = 5, pady = 5)
#Magic6 = ttk.Button(tab4, text="    Steal Magic Books    ", command= lambda: SelectJob(Magic6))
#Magic6.grid(column = 2, row = 1, padx = 5, pady = 5)
#Magic7 = ttk.Button(tab4, text="   Read Magic Books   ", command= lambda: SelectJob(Magic7))
#Magic7.grid(column = 0, row = 2, padx = 5, pady = 5)
#Magic8 = ttk.Button(tab4, text="           Meditate           ", command= lambda: SelectJob(Magic8))
#Magic8.grid(column = 1, row = 2, padx = 5, pady = 5)
#Magic9 = ttk.Button(tab4, text="       Practice Magic       ", command= lambda: SelectJob(Magic9))
#Magic9.grid(column = 2, row = 2, padx = 5, pady = 5)
              


root.mainloop() 
