import tkinter as tk
def show_frame1():
    frame1.pack()
    frame2.pack_forget()

def show_frame2():
    frame2.pack()
    frame1.pack_forget()

# Create the main window
root = tk.Tk()
root.title("Switch Frames Example")

# Create Frame 1
frame1 = tk.Frame(root, width=200, height=100, bg="lightblue")
label1 = tk.Label(frame1, text="Frame 1", font=("Helvetica", 16))
label1.pack(pady=20)

# Create Frame 2
frame2 = tk.Frame(root, width=200, height=100, bg="lightgreen")
label2 = tk.Label(frame2, text="Frame 2", font=("Helvetica", 16))
label2.pack(pady=20)

# Create buttons to switch between frames
button_frame1 = tk.Button(root, text="Show Frame 1", command=show_frame1)
button_frame1.pack(pady=10)

button_frame2 = tk.Button(root, text="Show Frame 2", command=show_frame2)
button_frame2.pack(pady=10)

# Initially show Frame 1
show_frame1()

# Start the main loop
root.mainloop()
