from tkinter import *
from PIL import ImageTk
from tkinter import messagebox


#Functionality Part
def open_loginPage():
    signup_window.destroy()
    import signin

def register():
    username = usernameEntry.get()
    password = passwordEntry.get()

    # Add your registration logic here
    # For simplicity, let's check if the username and password are not empty
    if username and password:
        messagebox.showinfo("Registration Successful", "Account created for " + username + "!")
        signup_window.destroy()
        import new
    else:
        messagebox.showerror("Registration Failed", "Please enter a valid username and password")

#GUI part
signup_window = Tk()
signup_window.geometry('990x660+50+50')
signup_window.title('Signup Page')
signup_window.resizable(0,0)

bgImage = ImageTk.PhotoImage(file='images/2.jpg')
bgLabel=Label(signup_window,image=bgImage)
bgLabel.grid()

frame = Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading = Label(frame,text='USER REGISTER',font=('Microsoft Yahei UI Light',18,'bold underline'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=55,pady=10)


#email
emailLabel = Label(frame,text='EMAIL',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=40,pady=(12,0))

emailEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
emailEntry.grid(row=2,column=0,sticky='w',padx=40)

#username
usernameLabel = Label(frame,text='USERNAME',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=40,pady=(12,0))

usernameEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
usernameEntry.grid(row=4,column=0,sticky='w',padx=40)

#password
passwordLabel = Label(frame,text='PASSWORD',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=40,pady=(12,0))

passwordEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
passwordEntry.grid(row=6,column=0,sticky='w',padx=40)

# confirm password
confirmpasswordLabel = Label(frame,text='CONNFIRM PASSWORD',font=('Microsost Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=40,pady=(12,0))

confirmpasswordEntry = Entry(frame,width=30,font=('Microsost Yahei UI Light',10,'bold'),bg='firebrick1',fg='white')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=40)

#terms and conditrions checkbox
termandconditions = Checkbutton(frame,text='I agree to the terms & conditions',font=('Microsost Yahei UI Light',8,'bold'),fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',cursor='hand2')
termandconditions.grid(row=9,column=0,padx=2,pady=13)

#signup button
signupButton = Button(frame,text='SignUp',font=('Open Sans',16,'bold'),bd=0,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=17,command=register)
signupButton.grid(row=10,column=0,pady=10)

#redirecteing to login
alreadyaccountLabel = Label(frame,text='Already Have An Account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
alreadyaccountLabel.grid(row=11,column=0,sticky='w',padx=25,pady=5)

loginButton = Button(frame, text='LogIN!', font=('Open Sans', 9, 'bold underline'), fg='blue', bg='white', cursor='hand2', bd=0, activeforeground='blue', activebackground='white',command=open_loginPage)
loginButton.place(x=190, y=385)



signup_window.mainloop()