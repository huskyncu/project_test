import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import order
import record

wnd = tk.Tk()
wnd.geometry("400x400")
wnd.title("拉麵點餐機")

button = tk.Button(wnd,text="點餐",underline=-1,command=order.add)
button.place(relx=0.5,rely=0.2,anchor='n')
button = tk.Button(wnd,text="使用者點餐紀錄",underline=-1,command=record.query)
button.place(relx=0.5,rely=0.4,anchor='n')

close = tk.Button(wnd,text="關閉",underline=-1,command=wnd.destroy)
close.place(relx=0.5,rely=0.8,anchor="n")

wnd.mainloop()