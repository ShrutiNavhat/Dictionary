
# from tkinter import*
# root = Tk ()
# # root.title("Chat Box")
# # root.geometry("400*500")
# # # menu=Menu(root)
 

from tkinter import*
root=Tk()
root.title("Chat Bot")
root.geometry("800x800")
e=Entry(root,width=30,fg="black")
e.grid(row=0,column=1)


def clickme():
    mylable=Label(root,text="Hello")
    mylable.grid(row=3,column=1)
    e.delete(0,END)
    

    

mybutton=Button(root,text="Enter",padx=10,pady=10,bg="white",fg="green",command=clickme)
mybutton.grid(row=2,column=1)



root.mainloop()


# from curses import tigetflag
# from tkinter import*
# root=Tk()
# root.title("MY MENU APP")
# root.geometry("500x500")

# Radiobutton(root,text="option 1",variable= ,value=1)