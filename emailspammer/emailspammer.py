import smtplib
from tkinter import *


window = Tk()
window.geometry('200x300')
window.title("Email Spammer")
window.config(bg="#555555")
window.resizable(0,0)

image = PhotoImage(file='mail.png')


def main():
    for i in range(int(number.get())):
        reciver = emailstr.get()
        body = bodystr.get()


        spammer = smtplib.SMTP("smtp.gmail.com", 587)
        spammer.ehlo()
        spammer.starttls()

        my_email = senderr.get()

        spammer.login(my_email, passwordstr.get())
        spammer.sendmail(my_email, emailstr.get(), bodystr.get())
        spammer.close()

        print('1 email done')


def stop():
    window.quit()


label = Label(window, bg='#555555', image=image)
label.pack()

box = LabelFrame(window,text="Reciver", bg='#555555', fg='white')
box.pack(pady=5, padx=5)

box1 = LabelFrame(window, text="Sender", bg='#555555', fg='white')
box1.pack(pady=5, padx=5)

box2 = LabelFrame(window, text="", bg='#555555', fg='#555555')
box2.pack(pady=5, padx=5)

email = Entry(box)
email.pack(side="top", padx=5, pady=5)

body = Entry(box)
body.pack(side="top", padx=5, pady=5)

number = Entry(box)
number.pack(side="top", padx=5, pady=5)

senderr = Entry(box1)
senderr.pack(side="top", padx=5, pady=5)

password = Entry(box1, show='*')
password.pack(side="top", padx=5, pady=5)

send = Button(box2, text="Spam", command=main)
send.pack(side='left',  padx=2, pady=2)

stop = Button(box2, text="Stop", command=stop)
stop.pack(padx=2, pady=2)

bodystr = StringVar()
emailstr = StringVar()
senderrstr = StringVar()
passwordstr = StringVar()
numberint = IntVar()

emailstr.set("Reciver Email")
bodystr.set("Email body")
senderrstr.set("Your gmail")
passwordstr.set("Your password")
numberint.set("Amount of emails")

email["textvariable"] = emailstr
body["textvariable"] = bodystr
password["textvariable"] = passwordstr
senderr["textvariable"] = senderrstr
number["textvariable"] = numberint

window.mainloop()
