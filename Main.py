import sys
v=sys.version
if "2.7" in v:
    from Tkinter import *
    import tkFileDialog
elif "3.3" in v or "3.4" in v:
    from tkinter import *
    import tkinter.tkFileDialog
root=Tk("Text Editor")

text=Text(root)
text.grid(row=1, columnspan=3)

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation=tkFileDialog.asksaveasfilename()
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

def openfile():
    global text
    readlocation=tkFileDialog.askopenfile(filetypes = (("basic text files","*.txt"),("all files","*.*")))
    print(readlocation)
    text.delete(1.0, END)
    text.insert(INSERT, readlocation.read())


button=Button(root, text="Open", command=openfile)
button1=Button(root, text="Save", command=saveas)
#button2=Button(root, text="Calculate", command=saveas)
button.grid(row=0, column=0, sticky=E)
button1.grid(row=0, column=1, sticky=N)
#button2.grid(row=0, column=2, sticky=W)
root.mainloop()