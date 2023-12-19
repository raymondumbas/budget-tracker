import tkinter as tk
root = tk.Tk()
root.title("Budget Tracker")
currFrame = tk.Frame()

def show_frame(curr,next):
    curr.pack_forget()
    next.pack()
    currFrame = next




frame1 = tk.Frame(root, width=200, height=100, bg="lightblue")
frame1.pack();
frame2 = tk.Frame(root, width=200, height=100, bg="lightgreen")
button_frame2 = tk.Button(root, text="Show Frame 2", command=lambda: show_frame(frame1, frame2))
button_frame2.pack(pady=10)



root.mainloop()