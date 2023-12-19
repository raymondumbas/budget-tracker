import tkinter as tk
#Tutorial Site: https://realpython.com/python-gui-tkinter/

window = tk.Tk() #instance of Tk class

greeting = tk.Label(text="Hello, Tkinter") #label to add text
greeting.pack() #one way to add widget to window
#width/height measured in "text units"

#Label: displays text
label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)

#Button: clickable button
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
#Entry: clickable entry
entry = tk.Entry(fg="yellow", bg="blue", width=50)
'''
Retrieving text with .get()
Deleting text with .delete()
- entry.delete(0, 4) : delete indices 0 to 4
- entry.delete(0, tk.END)
Inserting text with .insert()
-  entry.insert(0, "Python") : inster Python at index 0
'''

#Text = multiline text, larger than Entry
text_box = tk.Text()
'''
text_box.get("1.0", "1.5")
- indices are range: 
1.0 = first line 0th index, 
1.5 = first line 5th index

get includes newline characters
'''

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

button.pack()

#fill y : responsive
#side LEFT
frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT)

#fill both
#expand
frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

#place
#not used very often (not responsive)
'''
frame = tk.Frame(master=window, width=150, height=150)
frame.pack()

label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
label1.place(x=0, y=0)
'''


window.mainloop()
'''
Event loop
- listens for events (button click/key press)
- blocks any code that comes after until you close the window
'''
