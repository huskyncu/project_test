import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from firebase import firebase
import json
# pip install json

def read_data():
    with open('data.json','r') as f:
        data = json.load(f)
    return data['url']

def query():
    def submit():
        try:
            name=name_text.get()
            
            url = read_data()
            fdb = firebase.FirebaseApplication(url, None) 
            result=fdb.get('/點餐紀錄',name)

            columns = ('時間','拉麵', '叉燒', '麵的口感', '湯的鹹度', '款項')
            headers =('時間','拉麵', '叉燒', '麵的口感', '湯的鹹度', '款項')
            widthes = (150,120,80,80,80,80)
            tv = ttk.Treeview(wnd, show="headings",height=10 ,columns=columns)
            for (column, header, width) in zip(columns, headers, widthes):
                tv.column(column, width=width, anchor="w")
                tv.heading(column, text=header, anchor="w")
            def inser_data():
                """插入数据"""
                contacts=[]
                contacts.append(tuple([time,a1,a2,a3,a4,a5]))
                for i, v in enumerate(contacts):
                    print(i,v)
                    tv.insert('', i,values=v)
                tv.place(relx=0.5,rely=0.35,anchor= 'n')
            r = [(k,v) for k,v in result.items()]
            for i,v in r:
                time=i
                r2=fdb.get('/點餐紀錄/'+name,time)
                a1=r2['拉麵']
                a2=r2['叉燒']
                a3=r2['麵的口感']
                a4=r2['湯的鹹度']
                a5=r2['款項']
                inser_data()
        except:
            messagebox.showinfo('訊息','查無此人')
            
    wnd = tk.Tk()
    wnd.geometry("900x800")
    wnd.title("訂單查詢")

    namet = tk.Label(wnd,text='姓名')
    namet.pack()
    name_text = tk.Entry(wnd)
    name_text.pack()
    
    button = tk.Button(wnd,text="查詢訂單",underline=-1,command=submit)
    button.place(relx=0.5,rely=0.7,anchor="n")
    close = tk.Button(wnd,text="關閉",underline=-1,command=wnd.destroy)
    close.place(relx=0.5,rely=0.8,anchor="n")
    
    wnd.mainloop()