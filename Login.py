from tkinter import *
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk
import pymysql


background = "#06283D"
framebg = "#EDEDED"
framefg = "#06283D"

global trial_no
trial_no = 0

def trial():
    global trial_no
    trial_no += 1
    print(f"Trial no. is: {trial_no}")
    if trial_no == 3:
        messagebox.showwarning("Warning", "You have tried more than the specified limit!")
        root.destroy()  # Program closes itself if wrong credentials given for three times continuously.

def forgot_pass():
    def change_password():
        if adminkey_entry.get() == '' or user_entry.get() == '' or newpass_entry.get() == '' or confirmpass_entry.get() == '':
            messagebox.showerror('Error', 'All fields are required!', parent=root)
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('Error', 'Password and Confirm Password are not matching!!', parent=root)
        elif adminkey_entry.get() != "314159":
            messagebox.showerror("Error", "Invalid Admin Key!", parent=root)
        else:
            con = pymysql.connect(host='localhost', user='root', password='Patro202172112', database='heart_data')
            mycursor = con.cursor()
            query = 'select * from login where Username=%s'
            mycursor.execute(query, (user_entry.get()))
            row = mycursor.fetchone()

            if row == None:
                messagebox.showerror('Error', 'Incorrect Username!', parent=root)
            else:
                query = 'update login set Password=%s where Username=%s'
                mycursor.execute(query, (newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success', 'Password is reset, please login with new password', parent=root)
                root.destroy()

    root = Toplevel()
    root.title('Change Password')
    root.geometry("790x512+350+120")
    root.resizable(False,False)

    # icon image
    image_icon = PhotoImage(file="Images/icon2.png")
    root.iconphoto(False, image_icon)

    bgPic = ImageTk.PhotoImage(file='Images/background.jpg')
    bglabel = Label(root, image=bgPic)
    bglabel.grid()

    heading_label = Label(root, text='RESET PASSWORD', font=('arial', '18', 'bold'), bg='white', fg='magenta2')
    heading_label.place(x=480, y=60)

    adminkeyLabel = Label(root, text='Admin key', font=('arial', 11, 'bold'), bg='white', fg='orchid1')
    adminkeyLabel.place(x=470, y=120)

    adminkey_entry = Entry(root, width=25, fg='#FF00FF', font=('arial', 11, 'bold'), bd=0,show="*")
    adminkey_entry.place(x=473, y=150)

    Frame(root, width=250, height=2, bg='orchid1').place(x=473, y=170)

    userLabel = Label(root, text='Username', font=('arial', 11, 'bold'), bg='white', fg='orchid1')
    userLabel.place(x=470, y=180)

    user_entry = Entry(root, width=25, fg='#FF00FF', font=('arial', 11, 'bold'), bd=0)
    user_entry.place(x=473, y=210)

    Frame(root, width=250, height=2, bg='orchid1').place(x=473, y=230)

    passwordLabel = Label(root, text='New Password', font=('arial', 11, 'bold'), bg='white', fg='orchid1')
    passwordLabel.place(x=470, y=240)

    newpass_entry = Entry(root, width=25, fg='#FF00FF', font=('arial', 11, 'bold'), bd=0)
    newpass_entry.place(x=473, y=270)

    Frame(root, width=250, height=2, bg='orchid1').place(x=473, y=290)

    confirmpassLabel = Label(root, text='Confirm New Password', font=('arial', 11, 'bold'), bg='white', fg='orchid1')
    confirmpassLabel.place(x=470, y=300)

    confirmpass_entry = Entry(root, width=25, fg='#FF00FF', font=('arial', 11, 'bold'), bd=0)
    confirmpass_entry.place(x=473, y=330)

    Frame(root, width=250, height=2, bg='orchid1').place(x=473, y=350)

    submitButton = Button(root, text='Submit', bd=0, bg='magenta2', fg='white', font=('Open Sans', '16', 'bold'),
                          width=19, cursor='hand2', activebackground='#FF00FF', activeforeground='white',
                          command=change_password)
    submitButton.place(x=477, y=420)

    root.mainloop()
def loginuser():
    username = user.get()
    password = code.get()

    if (username == "" or username == "UserID") or (password == "" or password == "Password"):
        messagebox.showerror("Entry Error", "Type Username or Password")

    else:
        try:
            mydb = mysql.connector.connect(host="localhost", user="root", password="Patro202172112", database="heart_data")
            mycursor = mydb.cursor()
            print("Connected to database!!")

        except:
            messagebox.showerror("Connection", "Database connection not established!!")
            return

    command = "use heart_data"
    mycursor.execute(command)

    command = "select * from login where Username=%s and Password=%s"
    mycursor.execute(command,(username, password))
    myresult = mycursor.fetchone()
    print(myresult)

    if myresult == None:
        messagebox.showinfo("Invalid!!", "Invalid Username and Password!!")

        #User may try several times and be successful in cracking the password, hence we have to make it so that only three tries are allowed
        trial()

    else:
        messagebox.showinfo("Login", "Logged in successfully!")
        root.destroy()
        import main_test


def register():
    root.destroy()
    import register


root = Tk()
root.title("Login Page")
root.geometry("1250x700+130-90")
root.config(bg=background)
root.resizable(False,False)


# icon image
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)


# background image
frame = Frame(root, bg="red")
frame.pack(fill=Y)

backgroundimage = PhotoImage(file="Images/Login_page.png")
Label(frame, image=backgroundimage).pack()


##############user entry################
def user_enter(e):
    user.delete(0, "end")

def user_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "UserID")


user = Entry(frame, width=18, fg="#fff", border=0, bg="#375174", font=("Arial bold", 24))
user.insert(0,"UserID")
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=500, y=315)


##############password entry################
def password_enter(e):
    code.delete(0, "end")

def password_leave(e):
    if code.get() == "":
        code.insert(0, "Password")


code = Entry(frame, width=18, fg="#fff", border=0, bg="#375174", font=("Arial bold", 24))
code.insert(0,"Password")
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=500, y=410)


###########Hide and show button############
button_mode = True

def hide():
    global button_mode
    if button_mode:
        eyeButton.config(image=closeeye, activebackground="white")
        code.config(show="*")
        button_mode = False
    else:
        eyeButton.config(image=openeye, activebackground="white")
        code.config(show="")
        button_mode = True


openeye = PhotoImage(file="Images/openeye.png")
closeeye = PhotoImage(file="Images/close eye.png")
eyeButton = Button(frame, image=openeye, bg="#375174", border=0, command=hide)
eyeButton.place(x=780, y=410)

##########################################################

loginButton = Button(root, text="LOGIN", bg="#1f5675", fg="white", width=10, height=1, font=("Boulder", 20, "bold"), bd=0, command=loginuser)
loginButton.place(x=543, y=593)

label = Label(root, text="Don't have an account?", fg="#fff", bg="#00264d", font=("Microsoft Yahei UI Light", 9))
label.place(x=500, y=500)

registerButton = Button(root, width=10, text="add new user", border=0, bg="#00264d", cursor="hand2", fg="#57a1f8", command=register)
registerButton.place(x=645, y=501)

forgotButton = Button(root, width=13, text="Forgot password?", border=0, bg="#00264d", cursor="hand2", fg="#57a1f8", command=forgot_pass)
forgotButton.place(x=720, y=470)


root.mainloop()
