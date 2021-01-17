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

veritabani=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gezgin_app")


pnr=Tk()
pnr.title("Pnr Sor Ekran")
pnr.geometry("1200x700+15+15")
arkaCanvas1 = Canvas(pnr, width=1350, height=720, bg="#A7DFEA").place(x=0, y=0)

pnrBanner = Label(pnr, text="Gezgin Bilet>> PNR Sorgu", bg='#9adbe8')
pnrBanner.place(x=15, y=15)
pnrBanner.config(font=("Arial", 28, "bold italic"))



def ara():
    mycursor = veritabani.cursor()
    mycursor.execute("SELECT * FROM seferler WHERE sefer_kodu=" + pnrGiris.get())
    sonuclar = mycursor.fetchall()
    for g in sonuclar:
        tree2.insert("", 'end', values=g)
        print(g)
tree2=ttk.Treeview(pnr)
tree2['columns']=("Sefer Kodu","Firma Adı","Kalkış İstasyonu","Varış İstasyonu", "Sefer Tarihi", "Sefer Saati")


# pnr sorgulama
pnrKodu = Label(pnr, text="PNR Kodu Giriniz")
pnrKodu.place(x=85, y=85)
pnrKodu.config(font=("Arial", 12, "bold"))

pnrGiris = Entry(pnr, text="PNR KODU")
pnrGiris.place(x=250, y=85)
pnrGiris.config(font=("Arial", 12, "bold"))

ara = Button(pnr, text="PNR SORGULA",command=(ara),bg='#ef6262')
ara.place(x=85, y=150)
ara.config(font=("Arial", 15, "bold"))

tree2 = ttk.Treeview(pnr)
tree2.config(height=10)

tree2["columns"] = ("Sefer Kodu","Firma Adı", "Kalkış İstasyonu", "Varış İstasyonu", "Sefer Tarihi", "Sefer Saati", )
tree2.column("Sefer Kodu", width=80, anchor='sw')
tree2.column("Kalkış İstasyonu", width=150)
tree2.column("Varış İstasyonu", width=150)
tree2.column("Firma Adı", width=150, anchor='sw')
tree2.column("Sefer Tarihi", width=100, anchor='sw')
tree2.column("Sefer Saati", width=100, anchor='sw')


tree2.heading("Sefer Kodu", text="Sefer Kodu", anchor='sw')
tree2.heading("Kalkış İstasyonu",text="Kalkış İstasyonu", anchor='sw')
tree2.heading("Varış İstasyonu",text="Varış İstasyonu", anchor='sw')
tree2.heading("Firma Adı", text="Firma Adı", anchor='sw')
tree2.heading("Sefer Tarihi", text="Sefer Tarihi", anchor='sw')
tree2.heading("Sefer Saati", text="Sefer Saati", anchor='sw')

tree2.place(x=50, y=200)


pnr.mainloop()