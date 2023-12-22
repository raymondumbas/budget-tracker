import tkinter as tk
currFrame = 0

def main():
    root = tk.Tk()
    root.title("Budget Tracker")
    
    #Navigation Bar Frame
    navbar = tk.Frame(root, width=1000, height=50, bg="lightblue")
    navbar.pack();
    navNewEntry = tk.Button(master = navbar, text="New Entry", command=showNewEntry)
    navNewEntry.pack(side=tk.LEFT,padx=5)
    navList = tk.Button(master = navbar, text="Transactions", command=showList)
    navList.pack(side=tk.LEFT,padx=5)
    navSummary = tk.Button(master = navbar, text="Summary", command=showSummary)
    navSummary.pack(side=tk.LEFT,padx=5)

    #New Entry Frame

    #Transactions Frame

    #Summary Frame

    root.mainloop()

#Transition Functions
def showNewEntry():
    currFrame.pack_forget()
def showList():
    currFrame.pack_forget()
def showSummary():
    currFrame.pack_forget()

def show_frame(curr,next):
    curr.pack_forget()
    next.pack()
    currFrame = next


if __name__ == "__main__": 
    main()