import os
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300 , bg = 'white', relief = 'groove')
canvas1.pack()

label1 = tk.Label(root, text='@Leandjb', bg = 'white')
label1.config(font=('helvetica', 12))
canvas1.create_window(50, 20, window=label1)

def upgradePIP ():
    os.system('start cmd /k python.exe -m pip install --upgrade pip') 
    
button1 = tk.Button(text='Actualizar PIP', command=upgradePIP, bg='orange', fg='black', font=('helvetica', 12, 'bold'), relief = 'flat')
canvas1.create_window(240, 80, window=button1)

def upgradeMatplot():
    os.system('start cmd /k pip install matplotlib') 
    
button1 = tk.Button(text='Matplotlib', command=upgradeMatplot, bg='orange', fg='black', font=('helvetica', 12, 'bold'), relief = 'flat')
canvas1.create_window(240, 120, window=button1)

def upgradePandas():
    os.system('start cmd /k pip install pandas') 
    
button1 = tk.Button(text='Pandas', command=upgradePandas, bg='orange', fg='black', font=('helvetica', 12, 'bold'), relief = 'flat')
canvas1.create_window(240, 160, window=button1)

def upgradeScipy():
    os.system('start cmd /k pip install scipy') 
    
button1 = tk.Button(text='Scipy', command=upgradeScipy, bg='orange', fg='black', font=('helvetica', 12, 'bold'), relief = 'flat')
canvas1.create_window(240, 200, window=button1)

root.mainloop()
