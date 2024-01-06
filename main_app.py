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
    global frameNewEntry
    frameNewEntry = tk.Frame(root, width=1000, height=50, bg= "white")
    frameNewEntry.pack()
    currFrame=frameNewEntry

    #Initialize other frames
    global frameList
    frameList = tk.Frame(root, width=1000, height=50, bg= "white")

    global frameSummary
    frameSummary = tk.Frame(root, width=1000, height=50, bg= "white")

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
    global currFrame, frameList
    if currFrame != frameNewEntry:
        if currFrame == frameList:
            clearFrame(frameList)
        currFrame.pack_forget()
        frameNewEntry.pack()
        currFrame = frameNewEntry

def showList():
    global currFrame
    if currFrame != frameList:
        #Hide Previous Frame
        currFrame.pack_forget()
        currFrame = frameList


        #Populate List
        with open(entriesFile, newline = '') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                entryLine = tk.Label(master=frameList, text=row)
                entryLine.pack()
                
                
        #Show List
        frameList.pack()
def showSummary():
    currFrame.pack_forget()

#New Entry Functions
def submitNewEntry():
    entryData = []
    for field in newEntryForm:
        value = field.get()
        entryData.append(value)
    print(entryData)
    with open(entriesFile,'w',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(entryData)

#Clear Function
def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy() 

if __name__ == "__main__": 
    main()