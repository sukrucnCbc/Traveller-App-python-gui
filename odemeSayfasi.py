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


def onay():

    global sorgu
    mycursor = veritabani.cursor()
    sorgu = "INSERT INTO odemeler(ad_soyad,e_posta,tel_no,kart_no,skt,cvv)" \
            "VALUES(%s, %s, %s, %s, %s, %s)"
    deger = (isimGiris.get(), ePostaGiris.get(), telNoGir.get(), kartNoGir.get(), sktNoGir.get(), cvvNoGir.get())
    mycursor.execute(sorgu, deger)
    veritabani.commit()
    print(mycursor.rowcount, "Ödeme Başarılı")
    bilgi = messagebox.showinfo("İşlem Tamamlandı", "Ödeme Başarılı bir şekilde gerçekleşti")
    if bilgi == "ok":
        pass

    else:
        pass


veritabani=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gezgin_app")

print("Ödeme ekranı açıldı")
odemeEkran = Tk()
odemeEkran.title("Ödeme sayfası")
odemeEkran.geometry("700x800")
arkaCanvas = Canvas(odemeEkran, width=1350, height=720, bg="#9adbe8").place(x=0, y=0)
menuCanvas = Canvas(odemeEkran, width=500, height=550).place(x=100, y=100)

mainBanner=Label(odemeEkran, text="Ödeme Ekranı",bg="#A7DFEA")
mainBanner.place(x=15, y=15)
mainBanner.config(font=("Arial", 28, "bold italic"))


# ödeme ekranı
# ad-soyad
isim = Label(odemeEkran, text="AD SOYAD")
isim.place(x=130, y=190)
isim.config(font=("Arial", 12, "bold"))

isimGiris = Entry(odemeEkran, text="AD SOYAD")
isimGiris.place(x=330, y=190)
isimGiris.config(font=("Arial", 12, "bold"))

# eposta
ePosta = Label(odemeEkran, text="E-POSTA")
ePosta.place(x=130, y=230)
ePosta.config(font=("Arial", 12, "bold"))

ePostaGiris = Entry(odemeEkran, text="E-POSTA")
ePostaGiris.place(x=330, y=230)
ePostaGiris.config(font=("Arial", 12, "bold"))

# tel giris
telNo = Label(odemeEkran, text="TELEFON NO")
telNo.place(x=130, y=270)
telNo.config(font=("Arial", "12", "bold"))

telNoGir = Entry(odemeEkran)
telNoGir.place(x=330, y=270)
telNoGir.config(font=("Arial", "12", "bold"))


# kart giris
kartNo = Label(odemeEkran, text="Kart NO")
kartNo.place(x=130, y=310)
kartNo.config(font=("Arial", "12", "bold" ))

kartNoGir = Entry(odemeEkran)
kartNoGir.place(x=330, y=310)
kartNoGir.config(font=("Arial", "12", "bold"))

# skt giris
sktNo = Label(odemeEkran, text=" CVV ve Son Kullanma Tarihi")
sktNo.place(x=130, y=360)
sktNo.config(font=("Arial", "12", "bold"))

sktNoGir = Entry(odemeEkran, width=6)
sktNoGir.place(x=435, y=360)
sktNoGir.config(font=("Arial", "12", "bold"))

cvvNoGir = Entry(odemeEkran, width=6)
cvvNoGir.place(x=355, y=360)
cvvNoGir.config(font=("Arial", "12", "bold"))


onayButon = Button(odemeEkran, text="ÖDEMEYİ ONAYLA", bg='#ef6262',command=(onay))
onayButon.place(x=280, y=440)
onayButon.config(font=("Arial", 15, "bold"))





odemeEkran.mainloop()