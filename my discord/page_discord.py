from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

MyDiscord=Tk()
MyDiscord.geometry('990x660+450+200')
MyDiscord.resizable(0,0)
MyDiscord.title('MyDiscord')

bgImage=ImageTk.PhotoImage(file='bg_discord.jpg')

bgLabel= Label(MyDiscord,image=bgImage)
bgLabel.pack()

MyDiscord.mainloop()