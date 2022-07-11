from tkinter import *
root = Tk()
def send():
    send="you:"+e.get()
    txt.insert(END,"\n"+send)
    if (e.get()=="hi"):
        txt.insert(END,"\n"+"me: hello")
    elif (e.get()=="hii"):
        txt.insert(END,"\n"+"me: Hello ")
    elif (e.get()=="how are you"):
        txt.insert(END,"\n"+"me: fine and u ")
    elif (e.get()=="fine"):
        txt.insert(END,"\n"+" me:okay ")
    elif (e.get()=="what are you doing"):
        txt.insert(END,"\n"+" me:studying and you ")
    elif (e.get()=="i am going to movie"):
        txt.insert(END,"\n"+" me:which movie are you going")
    elif (e.get()=="rowdy boys"):
        txt.insert(END,"\n"+" me:ohh okay,carry on")
    elif (e.get()=="okay bye"):
        txt.insert(END,"\n"+" me:see you soon ")
    # else:
    #     txt.insert(END,"\n"+" : glad to meet you ")
    e.delete(0,END)
txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("CHATBOT")
root.mainloop()