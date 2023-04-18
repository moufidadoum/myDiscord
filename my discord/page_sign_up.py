from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#COULEUR
#BLEU #5466F4
#GRIS #555454
#NOIR #1E1F22

def clear():
    emailEntry.delete(0, END)
    usernameEntry.delete(0, END)
    passwordEntry.delete(0, END)
    confirmEntry.delete(0, END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or usernameEntry.get()=='' or passwordEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Erreur', 'Tous les champs doivent être remplis')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Erreur', 'Les mots de passe doivent être identique')
    elif check.get()==0:
        messagebox.showerror("Erreur", "Veuillez accepter nos conditions d'utilisation")
    else:
        try:
            con=pymysql.connect(host='localhost', user='root', password='mouf')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Erreur', 'Connexion à la base de donnée interrompu, veuillez réessayer')
            return
        try:
            query='create database mydiscord'
            mycursor.execute(query)
            query='use mydiscord'
            mycursor.execute(query)
            query='create table userdata(id int auto_increment primary key not null, email varchar(100), username varchar(100), password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use mydiscord')
        query='select * from userdata where username=%s'
        mycursor.execute(query,(usernameEntry.get()))
        row=mycursor.fetchone()
        if row !=None:
            messagebox.showerror('Erreur', 'Username déjà utilisé')
        else:
            query='select * from userdata where email=%s'
            mycursor.execute(query,(emailEntry.get()))
            roww=mycursor.fetchone()
            if roww !=None:
                messagebox.showerror('Erreur', 'Email déjà utilisé')
            else:

                query='insert into userdata(email,username,password) values(%s,%s,%s)'
                mycursor.execute(query,(emailEntry.get(), usernameEntry.get(), passwordEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Succès', 'Inscription est complète')
                clear()
                signupWindow.destroy()
                import page_sign_in


def login_page():
    signupWindow.destroy()
    import page_sign_in 

#interface graphique GIU
signupWindow=Tk()
signupWindow.geometry('990x660+450+200')
signupWindow.title("My Discord - S'inscrire")
signupWindow.resizable(False,False)

background=ImageTk.PhotoImage(file='bg2.jpg')
bgLabel=Label(signupWindow, image=background)
bgLabel.grid()

#----------FRAME DE LA BOXE D'INSCRIPTION---------------------------------------------------------------------#
frame=Frame(signupWindow, bg='#555454')
frame.place(x=348, y=112)
#-------------------------------------------------------------------------------------------------------------#


#-----------TITRE---------------------------------------------------------------------------------------------#
heading=Label(frame,text='CRÉER UN COMPTE', font=('Microsoft Yahei UI Light', 21, 'bold')
              , bg='#555454', fg='#5466F4')
heading.grid(row=0, column=0, padx=10, pady=10)
#-------------------------------------------------------------------------------------------------------------#


#-------------ENTRY INSCRIPTION-------------------------------------------------------------------------------#
emailLabel=Label(frame, text='Email', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='#555454',fg='#5466F4')
emailLabel.grid(row=1, column=0, sticky='w', padx=25, pady=(10,0))
emailEntry=Entry(frame, width=35, font=('Arial', 10, 'bold') 
                 ,fg='white', bg='#1E1F22', bd=0)
emailEntry.grid(row=2, column=0, sticky='w', padx=25)

usernameLabel=Label(frame, text='Username', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='#555454',fg='#5466F4')
usernameLabel.grid(row=3, column=0, sticky='w', padx=25, pady=(10,0))
usernameEntry=Entry(frame, width=35, font=('Arial', 10, 'bold') 
                 ,fg='white', bg='#1E1F22', bd=0)
usernameEntry.grid(row=4, column=0, sticky='w', padx=25)

passwordLabel=Label(frame, text='Mot de passe', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='#555454',fg='#5466F4')
passwordLabel.grid(row=5, column=0, sticky='w', padx=25, pady=(10,0))
passwordEntry=Entry(frame, width=35, font=('Arial', 10, 'bold') 
                 ,fg='white', bg='#1E1F22', bd=0)
passwordEntry.grid(row=6, column=0, sticky='w', padx=25)

confirmLabel=Label(frame, text='Confirmez le mot de passe', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='#555454',fg='#5466F4')
confirmLabel.grid(row=7, column=0, sticky='w', padx=25, pady=(10,0))
confirmEntry=Entry(frame, width=35, font=('Arial', 10, 'bold') 
                 ,fg='white', bg='#1E1F22', bd=0)
confirmEntry.grid(row=8, column=0, sticky='w', padx=25)
#-------------------------------------------------------------------------------------------------------------#


#-----------------S'INSCRIRE ou SE CONNECTER------------------------------------------------------------------#
check=IntVar()
termsandconditions=Checkbutton(frame, text="J'ai lu et j'accepte les Conditions d'Utilisation", font=('Microsoft Yahei UI Light', 7, 'bold'),
                                bg='#555454', fg='#5466F4', activebackground='#555454', activeforeground='#5466F4', cursor='hand2', variable=check)
termsandconditions.grid(row=9, column=0, pady=10, padx=20)

signupButton=Button(frame, text="S'inscrire", font=('Open Sans', 16, 'bold'), bd=0, bg='#5466F4', fg='white',
                     activebackground='#5466F4', activeforeground='white', width=17, command=connect_database)
signupButton.grid(row=10,column=0, pady=10)

alreadyaccount=Label(frame, text="Tu as déjà un compte?", font=('Open Sans','9', 'bold'),
                     bg='#555454', fg='white')
alreadyaccount.grid(row=11, column=0, sticky='w', padx=25, pady=10)

loginButton=Button(frame, text='Se connecter', font=('Open Sans', 9, 'bold underline')
                    ,bg='#555454', fg='#5466F4', bd=0, cursor='hand2', activebackground='#555454',
                    activeforeground='#5466F4', command=login_page)
loginButton.place(x=160, y=385)
#-------------------------------------------------------------------------------------------------------------#


signupWindow.mainloop()