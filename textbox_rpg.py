import tkinter as tk                    
from tkinter import ttk
import time
  
root = tk.Tk()
root.title("TextBox RPG")
tabControl = ttk.Notebook(root)

Level = 1
Exp = 0

def update_progress_label():
    return f"Current Progress: {pb['value']}%"


def progress():
    while True:
        if pb['value'] < 80:
            start_button['state'] = "disabled"
            pb['value'] += 20
            value_label['text'] = update_progress_label()
            root.update_idletasks()
            time.sleep(1)
        else:
            start_button['state'] = "enabled"
            pb['value'] = 0
            value_label['text'] = update_progress_label()
            root.update_idletasks()
            break


def stop():
    pb.stop()
    value_label['text'] = update_progress_label()


# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)

# label
value_label = ttk.Label(root, text=update_progress_label())
value_label.grid(column=0, row=1, columnspan=2)

# start button
start_button = ttk.Button(
    root,
    text='Progress',
    command=progress
)
start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)

stop_button = ttk.Button(
    root,
    text='Stop',
    command=stop
)
stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
  
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
  
tabControl.add(tab1, text ='Stats')
tabControl.add(tab2, text ='Farming')
#if Level == 5:
#    tabControl.add(tab3, text ='Mining')
tabControl.grid(columnspan = 2, pady = 15)
  
ttk.Label(tab1, 
          text ="This is where stats would be displayed").grid(column = 2, 
                            row = 0,
                            rowspan = 3,
                            padx = 30,
                            pady = 30)  
ttk.Label(tab2,
          text ="This tab would start farming").grid(column = 2,
                            row = 0, 
                            rowspan = 3,
                            padx = 30,
                            pady = 30)
#ttk.Label(tab3,
#          text ="This tab would start mining").grid(column = 0,
#                                    row = 0, 
#                                    padx = 30,
#                                    pady = 30) 

  
root.mainloop()  
