import tkinter as tk

root = tk.Tk()
root.title("Budget Tracker")
currFrame = tk.Frame()

def show_frame(curr,next):
    curr.pack_forget()
    next.pack()
    currFrame = next





root.mainloop()