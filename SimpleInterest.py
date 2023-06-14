from tkinter import *
window = Tk()

window.title("Simple Interest Calculator")
window.geometry("380x400")
window.configure(bg="lightgreen")

def calculateInterest():
    p=float(principleentry.get())
    r=float(rateentry.get())
    t=float(timeentry.get())
    i=p*r*t/100
    interest = round(i, 2)
    resultLabel.destroy()
    
    outputMessage = Label(resultframe, text=interest, bg="lightgreen", font=("Calibri",12), width=42)
    outputMessage.place(x=20, y=40)
    outputMessage.pack()

appLabel = Label(window, text="Interest Calculator", fg="black", bg="lightgreen", font=("Calibri",20), bd=5)
appLabel.place(x=50, y=20) 

principleLabel = Label(window, text="Enter principle", fg="black", bg="lightgreen", font=("Calibri",12))
principleLabel.place(x=20, y=140) 

principleentry = Entry(window, text="", bd=2, width=15)
principleentry.place(x=150, y=142) 

rateLabel = Label(window, text="Enter rate", fg="black", bg="lightgreen", font=("Calibri",12))
rateLabel.place(x=20, y=185) 

rateentry = Entry(window, text="", bd=2, width=15)
rateentry.place(x=150, y=187)

timeLabel = Label(window, text="Enter time (year)", fg="black", bg="lightgreen", font=("Calibri",12))
timeLabel.place(x=20, y=230) 

timeentry = Entry(window, text="", bd=2, width=15)
timeentry.place(x=150, y=232)

calculate = Button(window, text="Calculator", fg="black", bg="green", bd=4, command=calculateInterest)
calculate.place(x=20, y=295) 

resultframe = LabelFrame(window, text="Your Interest is:-", bg="lightgreen", font=("Calibri",12))
resultframe.place(x=20, y=300) 
resultframe.pack(padx=20, pady=20)

resultLabel = Label(resultframe, text="", bg="lightgreen", font=("Calibri",12), width=33)
resultLabel.place(x=20, y=20)
resultLabel.pack()



window.mainloop()