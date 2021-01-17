import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import mysql
import mysql.connector
from tkinter import ttk
import os
import shutil

def odemeSayfasi():
    import odemeSayfasi

def anasayfa():
    import UYGULAMA

veritabani=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gezgin_app")



seferEkran=Tk()
seferEkran.title("Sefer Ekranı")
seferEkran.geometry("1200x700+10+10")

arkaCanvas1 = Canvas(seferEkran, width=1350, height=720, bg="#9adbe8").place(x=0, y=0)

seferlerBanner = Label(seferEkran, text="Gezgin Bilet>> Bilet Al>> Seferler", bg='#9adbe8')
seferlerBanner.place(x=15, y=15)
seferlerBanner.config(font=("Arial", 28, "bold italic"))








tree2 = ttk.Treeview(seferEkran)
tree2.config(height=15)










tree2["columns"] = ("Sefer Kodu","Firma Adı", "Kalkış İstasyonu", "Varış İstasyonu", "Sefer Tarihi", "Sefer Saati","Fiyat")
tree2.column("Sefer Kodu", width=80, anchor='sw')
tree2.column("Kalkış İstasyonu", width=150)
tree2.column("Varış İstasyonu", width=150)
tree2.column("Firma Adı", width=150, anchor='sw')
tree2.column("Sefer Tarihi", width=100, anchor='sw')
tree2.column("Sefer Saati", width=100, anchor='sw')
tree2.column("Fiyat", width=100, anchor='sw')

tree2.heading("Sefer Kodu", text="Sefer Kodu", anchor='sw')
tree2.heading("Kalkış İstasyonu",text="Kalkış İstasyonu", anchor='sw')
tree2.heading("Varış İstasyonu",text="Varış İstasyonu", anchor='sw')
tree2.heading("Firma Adı", text="Firma Adı", anchor='sw')
tree2.heading("Sefer Tarihi", text="Sefer Tarihi", anchor='sw')
tree2.heading("Sefer Saati", text="Sefer Saati", anchor='sw')
tree2.heading("Fiyat", text="Fiyat", anchor='sw')
tree2.place(x=50, y=150)
#imaj1 = PhotoImage(file="credit.gif")
#resim1 = imaj1.subsample(5, 5)
buton1=Button(seferEkran,text="Ödemeye İlerle",width=15,bg="#ef6262",command=odemeSayfasi)
buton1.place(x=890,y=500)
buton1.config(font=("Arial", 15, "bold"))

ana=Button(seferEkran,text="Anasayfaya Dön",width=15,bg="#ef6262")
ana.place(x=50,y=500)
ana.config(font=("Arial", 15, "bold"))

seferEkran.mainloop()

