import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from firebase import firebase
import datetime
import json

def read_data():
    with open('data.json','r') as f:
        data = json.load(f)
    return data['url']


def add():
    def submit():
        name=name_text.get()
        a1=c1.get()
        a2=c2.get()
        a3=c3.get()
        a4=c4.get()
        if name==''or a1==''or a2=='' or a3=='' or a4=='':
            messagebox.showinfo('訊息','訂單錯誤')
        else:
            if a1=='白湯大蒜叉燒拉麵: 240':
                a1='白湯大蒜叉燒拉麵'
                p1='240'
            if a1=='醬油魚介叉燒拉麵: 240':
                a1='醬油魚介叉燒拉麵'
                p1='240'
            if a1=='麻辣辣椒叉燒拉麵: 240':
                a1='麻辣辣椒叉燒拉麵'
                p1='240'
            if a1=='月限定拉麵: 300':
                a1='月限定拉麵'
                p1='300'
            now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
            time=str(now.strftime('%Y,%m,%d %H:%M:%S'))
            
            url = read_data()
            fdb = firebase.FirebaseApplication(url, None) 
            fdb.put('/點餐紀錄/'+name,time,{'拉麵':a1, '叉燒':a2, '麵的口感':a3, '湯的鹹度':a4, '款項':p1})
            messagebox.showinfo('訊息','成功送出訂單')
            wnd.destroy()
    
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("拉麵")

    namet = tk.Label(wnd,text='姓名')
    namet.pack()
    name_text = tk.Entry(wnd)
    name_text.pack()

    gendert = tk.Label(wnd,text='款項')
    gendert.pack()
    n = tk.StringVar()
    c1 = ttk.Combobox(wnd, width = 17, textvariable = n)
    c1['values'] = ('白湯大蒜叉燒拉麵: 240', '醬油魚介叉燒拉麵: 240', '麻辣辣椒叉燒拉麵: 240', '月限定拉麵: 300')
    c1.pack()

    mt = tk.Label(wnd,text='叉燒')
    mt.pack()
    n2 = tk.StringVar()
    c2 = ttk.Combobox(wnd, width = 17, textvariable = n2)
    c2['values'] = ('五花叉燒', '梅花叉燒')
    c2.pack()


    nt = tk.Label(wnd,text='麵的口感')
    nt.pack()
    n3 = tk.StringVar()
    c3 = ttk.Combobox(wnd, width = 17, textvariable = n3)
    c3['values'] = ('軟', '中', '硬')
    c3.pack()
    
    soup = tk.Label(wnd,text='湯的鹹度')
    soup.pack()
    n4 = tk.StringVar()
    c4 = ttk.Combobox(wnd, width = 17, textvariable = n4)
    c4['values'] = ('輕', '適中', '重鹹')
    c4.pack()

    button = tk.Button(wnd,text="送出訂單",underline=-1,command=submit)
    button.pack()
    close = tk.Button(wnd,text="關閉點餐頁面",underline=-1,command=wnd.destroy)
    close.place(relx=0.5,rely=0.8,anchor="n")

    wnd.mainloop()