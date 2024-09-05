from tkinter import *

root=Tk()
root.title("Registration")
root.geometry("600x470")
root.resizable(False,False)

def register():
    print("registered")

Label(root,text="Python Registration Form",font="arial 25").pack(pady=50)

Label(text="Name",font=23).place(x=100,y=150)
Label(text="Email",font=23).place(x=100,y=250)
Label(text="Age",font=23).place(x=100,y=200)

#entry
nameValue=StringVar()
emailValue=StringVar()
ageValue=StringVar()

nameEntry=Entry(root,textvariable=nameValue,width=30,bd=2,font=20)
emailEntry=Entry(root,textvariable=emailValue,width=30,bd=2,font=20)
ageEntry=Entry(root,textvariable=ageValue,width=30,bd=2,font=20)

nameEntry.place(x=200,y=150)
emailEntry.place(x=200,y=250)
ageEntry.place(x=200,y=200)

#check button
checkValue=IntVar
checkbtn=Checkbutton(text="remember me?",variable=checkValue)
checkbtn.place(x=200,y=340)

Button(text="Register",font=20,width=11,height=2,command=register).place(x=250,y=380)


root.mainloop()
