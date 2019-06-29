import os
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 480, height = 360 , bg = 'white', relief = 'groove')
canvas1.pack()

label1 = tk.Label(root, text='@Leandjb', bg = 'white')
label1.config(font=('helvetica', 10))
canvas1.create_window(450, 350, window=label1)

def upgradePIP ():
    os.system('start cmd /k python.exe -m pip install --upgrade pip') 
    
button1 = tk.Button(text='ActualizarPIP', command=upgradePIP, bg='orange', fg='black', font=('helvetica', 12, 'bold'), relief = 'flat')
canvas1.create_window(240, 180, window=button1)

root.mainloop()
