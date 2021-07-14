from tkinter import *
root= Tk()
root.geometry("500x300")
def bala():
    print("form submitted");
Label(root, text="REGISTRATION FORM", font="arial 20 bold").grid(row=0, column=2)
name= Label(root, text="Name")
phone= Label(root, text="Phone")
gender= Label(root, text="Gender")
email= Label(root, text="Email")
password= Label(root, text="Password")

name.grid(row=1, column=1)
phone.grid(row=2, column=1)
gender.grid(row=3, column=1)
email.grid(row=4, column=1)
password.grid(row=5, column=1)

namevalue =StringVar
phonevalue =StringVar
gendervalue =StringVar
emailvalue =StringVar
passwordvalue =StringVar
checkvalue=IntVar

nameentry=Entry(root, textvariable=namevalue).grid(row=1, column=2)
phoneentry=Entry(root, textvariable=phone).grid(row=2, column=2)
genderentry=Entry(root, textvariable=gendervalue).grid(row=3, column=2)
emailentry=Entry(root, textvariable=emailvalue).grid(row=4, column=2)
passwordentry=Entry(root, textvariable=passwordvalue).grid(row=5, column=2)


checkbtn=Checkbutton(text="remember me !!!!!", variable=checkvalue).grid(row=6, column=2)

Button(text="submit", command=bala).grid(row=7, column=2)







root.mainloop()