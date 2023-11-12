from tkinter import *
from tkinter.font import Font
from tkinter.messagebox import showwarning

rt = Tk()
rt.title('Motion-cut ToDo List')
rt.geometry("500x700")

#Defining font
myFont = Font(family="Times New Roman", size = 30, weight='bold',slant="italic")

#create Frame
myFrame = Frame(rt)
myFrame.pack(pady=10)

#create listbox
myList = Listbox(myFrame, 
    font=myFont, 
    width=24, 
    height=5, 
    bg='#DFD0C0',
    bd=0, 
    fg='#202020',
    highlightthickness=0,
    selectbackground="#A6A6A6",
    activestyle='none')

myList.pack(side=LEFT, fill=BOTH)

#Create Scroll bar
myScrollbar = Scrollbar(myFrame)
myScrollbar.pack(side=RIGHT, fill=BOTH)

#Add ScrollBar
myList.config(yscrollcommand=myScrollbar.set)
myScrollbar.config(command=myList.yview)

#create a entry box to add items
taskLabel = Label(rt, text="Enter New Task")
taskLabel.pack()
myEntry = Entry(rt, font=("Helvetica",24))
myEntry.pack(pady=5)

desLabel = Label(rt, text="Description")
desLabel.pack()
descriptionEntry = Entry(rt, font=("Helvetica", 15))
descriptionEntry.pack(pady=5)

dueLabel = Label(rt, text="Due Date")
dueLabel.pack()
dueDateEntry = Entry(rt, font=("Helvetica", 15))
dueDateEntry.pack(pady=5)

priorLabel = Label(rt, text="Priorty")
priorLabel.pack()
priorityEntry = Entry(rt, font=("Helvetica", 15))
priorityEntry.pack(pady=5)

#create a button frame
buttonFrame = Frame(rt)
buttonFrame.pack(pady=20)

dic = {}
#Functions
def delete():
    myList.delete(ANCHOR)

def add():
    if myEntry.get() == "":
        showwarning(title="Warning!",message="Please enter some Text")
    else:
        task = myEntry.get()
        description = descriptionEntry.get()
        due_date = dueDateEntry.get()
        priority = priorityEntry.get()

        dic[task]={"Description":description,
                    "Due Date": due_date,
                    "Priority": priority}

        myList.insert(END, task)
    myEntry.delete(0, END)
    descriptionEntry.delete(0, END)
    dueDateEntry.delete(0, END)
    priorityEntry.delete(0, END)

def cross():
    #cross activity
    myList.itemconfig(
        myList.curselection(),
        fg="#DEDEDE")
    
    #removing selection bar
    myList.select_clear(0, END)

def uncross():
    #cross activity
    myList.itemconfig(
        myList.curselection(),
        fg="#202020")
    
    #removing selection bar
    myList.select_clear(0, END)

def delCross():
    count = 0
    while count<myList.size():
        if myList.itemcget(count, "fg") == "#DEDEDE":
            myList.delete(myList.index(count))
        count += 1

def show():
    index = myList.curselection()
    z = index[0]
    task = myList.get(z)
    try:
        showDic = Label(rt, text=f"{task} - Description: {dic[task]['Description']}, Due-date: {dic[task]['Due Date']}, Priority: {dic[task]['Priority']}")
        showDic.pack()
    except:
        tell = Label(rt, text="No Details Found")
        tell.pack()

def editDetails():
    index = myList.curselection()
    z = index[0]
    task = myList.get(z)

    rt = Tk()
    rt.title('Edit Details')
    rt.geometry("500x500")

    #create Frame
    myFrame = Frame(rt)
    myFrame.pack(pady=10)

    buttonFrame = Frame(rt)
    buttonFrame.pack(pady=20)

    desEditLabel = Label(rt, text="Description")
    desEditLabel.pack()
    descriptionEditEntry = Entry(rt, font=("Helvetica", 15))
    descriptionEditEntry.pack(pady=5)

    dueEditLabel = Label(rt, text="Due Date")
    dueEditLabel.pack()
    dueEditDateEntry = Entry(rt, font=("Helvetica", 15))
    dueEditDateEntry.pack(pady=5)

    priorEditLabel = Label(rt, text="Priorty")
    priorEditLabel.pack()
    priorityEditEntry = Entry(rt, font=("Helvetica", 15))
    priorityEditEntry.pack(pady=5)

    def done():
        descrip = descriptionEditEntry.get()
        due = dueEditDateEntry.get()
        prior = priorityEditEntry.get()
        if task not in dic:
            dic[task] = {}
        dic[task]["Description"] = descrip
        dic[task]["Due Date"] = due
        dic[task]["Priority"] = prior
        descriptionEditEntry. delete(0, END)
        dueEditDateEntry.delete(0, END)
        priorityEditEntry.delete(0, END)
        rt.destroy()

    doneButton = Button(buttonFrame, text="Done", command=done)
    doneButton.grid(row= 10,column=0)
    rt.mainloop()

#add some buttons
deleteButton = Button(buttonFrame, text="Delete", command=delete)
addButton = Button(buttonFrame, text="Add", command=add)
crossButton = Button(buttonFrame, text="Cross off", command=cross)
uncrossButton = Button(buttonFrame, text="Uncross", command=uncross)
delCrossButton = Button(buttonFrame, text="Delete Crossed", command=delCross)
showButton = Button(buttonFrame, text="Show Details", command=show)
editButton = Button(buttonFrame, text="Edit Details", command=editDetails)

deleteButton.grid(row=0, column=0)
addButton.grid(row=0, column=1, padx=20)
crossButton.grid(row=0, column=2)
uncrossButton.grid(row=0, column=3, padx=20)
delCrossButton.grid(row=0, column=4)
showButton.grid(row=1, column=0)
editButton.grid(row=1, column=1, padx=20)

rt.mainloop()