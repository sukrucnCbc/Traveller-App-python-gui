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

def seferEkran():
    import seferEkran

def pnrAra():
    import pnrSorEkran
veritabani=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gezgin_app")

def odeme():
    import odemeSayfasi


def listele():
    mycursor = veritabani.cursor()
    mycursor.execute("SELECT * FROM seferler WHERE kalkis_ist=" + sehir.get() and "SELECT * FROM seferler WHERE varis_ist=" + sehir2.get()
                     )
    sonuclar = mycursor.fetchall()
    for s in sonuclar:
        tree2.insert("", 'end', values=s)
        print(s)










sehirList = ["Şehir Seç", "'İSTANBUL'", "'ANKARA'", "'TRABZON'", "'İZMİR'", "'KOCAELİ'", "'RİZE'", "'GİRESUN'", "'ORDU'", "'SAMSUN'",
             "'ÇORUM'"]
ayList = ["'Ay'", "Ocak", "Subat", "Mart", "Nisan", "Mayis", "Haziran", "Temmuz", "Ağustos", "Eylul", "Ekim", "Kasim",
          "Aralik"]
gunList = ["'Gün'", "1", "2", "3", "4", "'5'", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18",
           "19",
           "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

ana = Tk()
ana.title("Ana sayfa")

ana.geometry("1360x720")
arkaCanvas = Canvas(ana, width=1350, height=720, bg="#9adbe8").place(x=0, y=0)
menuCanvas = Canvas(ana, width=1250, height=850).place(x=50, y=80)

biletAlBanner = Label(ana, text=">>Bilet Al", bg='#9adbe8')
biletAlBanner.place(x=15, y=15)
biletAlBanner.config(font=("Arial", 28, "bold italic"))

nereden = Label(ana, text="Nereden")
nereden.place(x=90, y=120)
nereden.config(font=("Arial", 12, "bold"))

sehir = ttk.Combobox(ana, width=20)
sehir['values'] = sehirList
sehir.place(x=160, y=120)
sehir.current(0)
sehir.config(font=("Arial", 15, "bold"), background="#509CCE")

nereye = Label(ana, text="Nereye")
nereye.place(x=425, y=120)
nereye.config(font=("Arial", 12, "bold"))

sehir2 = ttk.Combobox(ana, width=20)
sehir2['values'] = sehirList
sehir2.place(x=490, y=120)
sehir2.current(0)
sehir2.config(font=("Arial", 15, "bold"))

tarihSec = Label(ana, text="Gidiş Tarihi")
tarihSec.place(x=780, y=80)
tarihSec.config(font=("Arial", 15, "bold"))

gunSec = ttk.Combobox(ana, width=5)
gunSec['values'] = gunList
gunSec.current(0)
gunSec.place(x=760, y=120)
gunSec.config(font=("Arial", 15, "bold"))

aySec = ttk.Combobox(ana, width=7)
aySec['values'] = ayList
aySec.current(0)
aySec.place(x=850, y=120)
aySec.config(font=("Arial", 15, "bold"))

seferSorgu = Button(ana, text="Sefer Sorgula", width=13, pady=5, padx=5, bg='#ef6262', command=listele)
seferSorgu.place(x=965, y=110)
seferSorgu.config(font=("Arial", 25, "italic"))


odeme = Button(ana, text="Ödemeye ilerle", width=13, pady=5, padx=5, bg='#ef6262', command=odeme)
odeme.place(x=965, y=300)
odeme.config(font=("Arial", 25, "italic"))



pnrSorgu = Button(ana, text="PNR Sorgula", width=13, pady=5, padx=5, bg='#ef6262', command=pnrAra)
pnrSorgu.place(x=965, y=550)
pnrSorgu.config(font=("Arial", 25, "italic"))

tree2 = ttk.Treeview(ana)
tree2.config(height=20)
tree2['show']='headings'
tree2["columns"] = ("Sefer Kodu","Firma Adı", "Kalkış İstasyonu", "Varış İstasyonu", "Sefer Tarihi", "Sefer Saati")
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

tree2.place(x=130, y=250)



ana.mainloop()