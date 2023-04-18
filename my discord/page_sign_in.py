from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
#COULEUR
#BLEU #5466F4
#GRIS #555454


#Fonctions

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Erreur', 'Tous les champs doivent être remplis')
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='mouf')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Erreur', 'Connexion à la base de donnée interrompu, veuillez réessayer')
            return
        query='use mydiscord'
        mycursor.execute(query)
        query = 'select * from userdata where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Erreur', "Nom d'utilisateur ou mot de passe incorrect")
        else:
            messagebox.showinfo('Bienvenu', 'Connecté avec succès')
            LoginWindow.destroy()
            import page_discord


def forget_pass():
    def change_password():
        if user_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Erreur', 'Tous les champs doivent être remplis', parent=window)
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('Erreur', 'Mots de passe non identique', parent=window)
        else:
            con=pymysql.connect(host='localhost', user='root', password='mouf', database='mydiscord')
            mycursor=con.cursor()
            query='select * from userdata where username=%s'
            mycursor.execute(query, (user_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Erreur', "Nom d'utilisateur incorrect", parent=window)
            else:
                query = 'update userdata set password=%s where username=%s'
                mycursor.execute(query,(newpass_entry.get(), user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Succès', 'Votre mot de passe a bien été modifié, vous pouvez vous connecter.', parent=window)
                window.destroy()


    window = Toplevel()
    window.title('Réinitialiser son mot de passe')
    window.resizable(0,0)
    window.geometry('790x512+540+300')
    bgPic = ImageTk.PhotoImage(file='bg_fp.jpg')
    bgLabel=Label(window, image=bgPic)
    bgLabel.grid()

    heading_label = Label(window, text='RÉINITIALISER MDP', font=('arial', '18', 'bold'),
                          bg='#555454', fg='#5466F4')
    heading_label.place(x=480, y=60)

    userLabel=Label(window, text='Username', font=('arial', 12, 'bold'), bg='#555454', fg='white')
    userLabel.place(x=470, y=130)
    user_entry=Entry(window, width=25, fg='#5466F4',font=('arial', 11, 'bold'), bd=0, bg='#555454')
    user_entry.place(x=470, y=160)
    Frame(window, width=250, height=2, bg='#5466F4').place(x=470, y=180)

    password=Label(window, text='Nouveau mot de passe', font=('arial', 12, 'bold'), bg='#555454', fg='white')
    password.place(x=470, y=210)
    newpass_entry=Entry(window, width=25, fg='#5466F4',font=('arial', 11, 'bold'), bd=0, bg='#555454')
    newpass_entry.place(x=470, y=240)
    Frame(window, width=250, height=2, bg='#5466F4').place(x=470, y=260)

    confirmpass=Label(window, text='Confirmer le mot de passe', font=('arial', 12, 'bold'), bg='#555454', fg='white')
    confirmpass.place(x=470, y=290)
    confirmpass_entry=Entry(window, width=25, fg='#5466F4',font=('arial', 11, 'bold'), bd=0, bg='#555454')
    confirmpass_entry.place(x=470, y=320)
    Frame(window, width=250, height=2, bg='#5466F4').place(x=470, y=340)

    SubmitButton = Button(window , text='Soumettre', bd=0, bg='#5466F4', fg='white', font=('Open Sans', '16', 'bold')
                          ,width=19, cursor='hand2', activebackground='#5466F4', activeforeground='white'
                          ,command=change_password)
    SubmitButton.place(x=470, y=390)

    window.mainloop()







def signup_page():
    LoginWindow.destroy()
    import page_sign_up

def user_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get()=='Mot de passe':
        passwordEntry.delete(0, END)

def hide():
    openeye.config(file='closeeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)

#interface graphique GIU
LoginWindow=Tk()
LoginWindow.geometry('990x660+450+200')
LoginWindow.resizable(0,0)
LoginWindow.title('MyDiscord - Se connecter')

bgImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel= Label(LoginWindow,image=bgImage)
bgLabel.pack()

#----------------------TITRE LOGIN USER----------------------------------------------------------------------#
heading=Label(LoginWindow,text='CONNEXION', font=('Microsoft Yahei UI Light', 23, 'bold')
              , bg='#555454', fg='#5466F4')
heading.place(x=605,y=120)
#-------------------------------------------------------------------------------------------------------------#


#----------------------ENTRY DE L'USERNAME--------------------------------------------------------------------#
usernameEntry=Entry(LoginWindow, width=25, font=('Microsoft Yahei UI Light', 11, 'bold')
                    , bd=0, bg='#555454', fg='white')
usernameEntry.place(x=585, y=200)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

frame1=Frame(LoginWindow, width=230, height=2, bg='#5466F4')
frame1.place(x=585, y=222)
#-------------------------------------------------------------------------------------------------------------#


#----------------------ENTRY DU MOT DE PASSE-------------------------------------------------------------------#
passwordEntry=Entry(LoginWindow, width=25, font=('Microsoft Yahei UI Light', 11, 'bold')
                    , bd=0, bg='#555454', fg='white')
passwordEntry.place(x=585, y=260)
passwordEntry.insert(0, 'Mot de passe')

passwordEntry.bind('<FocusIn>', password_enter)

frame2=Frame(LoginWindow, width=230, height=2, bg='#5466F4')
frame2.place(x=585, y=282)

openeye=PhotoImage(file='openeye.png')
eyeButton=Button(LoginWindow, image=openeye, bd=0, bg='#555454', activebackground='#555454',
                 cursor='hand2', command=hide)
eyeButton.place(x=790, y=255)

forgetButton=Button(LoginWindow, text='Mot de passe oublié?', bd=0, bg='#555454', activebackground='#555454',
                 cursor='hand2', font=('Arial', 9, 'bold'), fg='#5466F4', activeforeground='#5466F4', command=forget_pass)
forgetButton.place(x=690, y=295)
#-------------------------------------------------------------------------------------------------------------#


#----------------------SE CONNECTER BOUTON--------------------------------------------------------------------#
loginButton=Button(LoginWindow, text='Se Connecter', font=('Open Sans', 16, 'bold'),
                    fg='white', bg='#5466F4', activeforeground='white',
                      activebackground='#5466F4', cursor='hand2', bd=0, width=18, command=login_user)
loginButton.place(x=585, y=350)

ouLabel=Label(LoginWindow, text='--------------- OU ---------------', font=('Open Sans', 16), fg='#5466F4', bg='#555454')
ouLabel.place(x=575, y=400)

facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(LoginWindow, image=facebook_logo, bg='#555454')
fbLabel.place(x=640, y=440)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(LoginWindow, image=google_logo, bg='#555454')
googleLabel.place(x=690, y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(LoginWindow, image=twitter_logo, bg='#555454')
twitterLabel.place(x=740, y=440)
#-------------------------------------------------------------------------------------------------------------#

signupLabel=Label(LoginWindow, text="Besoin d'un compte?", font=('Open Sans',9, 'bold' ), fg='white', bg='#555454')
signupLabel.place(x=600, y=500)

newaccountButton=Button(LoginWindow, text="S'inscrire", font=('Open Sans', 9, 'bold underline'),
                    fg='#5466F4', bg='#555454', activeforeground='#5466F4',
                      activebackground='#555454', cursor='hand2', bd=0, command=signup_page)
newaccountButton.place(x=725, y=500)


LoginWindow.mainloop()