import tkinter as tk
import csv

entriesFile = "entries.csv"

def main():
    global currFrame
    root = tk.Tk()
    root.title("Budget Tracker")
    
    #Navigation Bar Frame
    navbar = tk.Frame(root, width=1000, height=50, bg="gray")
    navbar.pack(side=tk.TOP, fill=tk.X)
    navNewEntry = tk.Button(master = navbar, text="New Entry", command=showNewEntry)
    navNewEntry.pack(side=tk.LEFT,padx=5)
    navList = tk.Button(master = navbar, text="Transactions", command=showList)
    navList.pack(side=tk.LEFT,padx=5)
    navSummary = tk.Button(master = navbar, text="Summary", command=showSummary)
    navSummary.pack(side=tk.LEFT,padx=5)

    #New Entry Frame
    frameNewEntry = tk.Frame(root, width=1000, height=50, bg= "white")
    frameNewEntry.pack()

    global newEntryForm
    newEntryForm=[]
    labels = [
        "Date",
        "Amount",
        "Reason",
        "Type"
    ]
    for i, text in enumerate(labels):
        label = tk.Label(master=frameNewEntry, text=text)
        entry = tk.Entry(master=frameNewEntry, width=50)

        label.grid(row=i, column=0, sticky="e")
        entry.grid(row=i, column=1)

        newEntryForm.append(entry)

    buttonSubmitNew = tk.Button(master=frameNewEntry, text="Submit",command=submitNewEntry)
    buttonSubmitNew.grid(row = 5, column = 1)

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

#New Entry Functions
def submitNewEntry():
    entryData = []
    for field in newEntryForm:
        value = field.get()
        entryData.append(value)
    print(entryData)
    with open('entries.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(entryData)

if __name__ == "__main__": 
    main()