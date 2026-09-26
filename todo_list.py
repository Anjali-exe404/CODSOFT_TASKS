import tkinter as tk
from tkinter import messagebox
import json

FILE="tasks.json"

try:
    tasks=json.load(open(FILE))
except:
    tasks=[]

def save():
    json.dump(tasks,open(FILE,"w"),indent=4)

def show(data=None):
    box.delete(0,tk.END)
    for i,t in enumerate(data if data is not None else tasks):
        s="✓" if t.get("completed",False) else "○"
        box.insert(tk.END,f"{i+1}. {s} {t['title']} | {t['category']} | {t['priority']} | {t['due_date']}")

def add():
    if not entry.get().strip():
        messagebox.showwarning("Warning","Enter a task!")
        return
    tasks.append({"title":entry.get(),"category":cat.get(),"priority":pri.get(),
                  "due_date":date.get(),"completed":False})
    save(); show(); entry.delete(0,tk.END); date.delete(0,tk.END)

def complete():
    try:
        tasks[box.curselection()[0]]["completed"]=True
        save(); show()
    except:
        messagebox.showwarning("Warning","Select a task!")

def delete():
    try:
        tasks.pop(box.curselection()[0])
        save(); show()
    except:
        messagebox.showwarning("Warning","Select a task!")

def update():
    try:
        t=tasks[box.curselection()[0]]
        t.update(title=entry.get() or t["title"],category=cat.get(),
                 priority=pri.get(),due_date=date.get() or t["due_date"])
        save(); show()
    except:
        messagebox.showwarning("Warning","Select a task!")

def search():
    x=entry.get().lower()
    show([t for t in tasks if x in t["title"].lower() or
          x in t["category"].lower() or x in t["priority"].lower()])

def progress():
    total=len(tasks)
    done=sum(t.get("completed",False) for t in tasks)
    messagebox.showinfo("Progress",f"Total: {total}\nCompleted: {done}\n"
                         f"Pending: {total-done}\nProgress: {done*100//total if total else 0}%")

# WINDOW
win=tk.Tk()
win.title("Smart To-Do Manager")
win.geometry("650x550")
win.minsize(550,450)

tk.Label(win,text="SMART TO-DO MANAGER",font=("Arial",20,"bold")).pack(pady=10)

entry=tk.Entry(win,width=40)
entry.pack(pady=5)

cat=tk.StringVar(value="Study")
tk.OptionMenu(win,cat,"Study","Work","Personal","Other").pack()

pri=tk.StringVar(value="Medium")
tk.OptionMenu(win,pri,"High","Medium","Low").pack()

date=tk.Entry(win,width=40)
date.pack(pady=5)

f=tk.Frame(win)
f.pack(pady=8)

for i,(name,cmd) in enumerate([
    ("Add",add),("Update",update),("Complete",complete),("Delete",delete),
    ("Search",search),("Show All",show),("Progress",progress)]):
    tk.Button(f,text=name,width=10,command=cmd).grid(row=i//4,column=i%4,padx=3,pady=3)

box=tk.Listbox(win,width=90,height=15)
box.pack(padx=10,pady=10,fill="both",expand=True)

show()
win.mainloop()