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


def yeni_kayit():
    global sorgu
    mycursor = veritabani.cursor()
    sorgu = "INSERT INTO kullanicilar(ad_soyad,e_posta,tel_no,sifre,sifre_tekrar)" \
            "VALUES(%s, %s, %s, %s, %s)"
    deger = (isimGiris.get(), ePostaGiris.get(), telNoGir.get(), sifreGiris.get(), sifreTekrarGiris.get())
    mycursor.execute(sorgu, deger)
    veritabani.commit()
    print(mycursor.rowcount, "Kişi Eklendi")
    bilgi = messagebox.showinfo("İşlem Tamamlandı", "Kayıt başarılı bir şekilde eklendi.")
    if bilgi == "ok":
        pass

    else:
        pass




print("Üye Ol ekranı açıldı")
uyeEkran = Tk()
uyeEkran.title("Üye Ol sayfa")
uyeEkran.geometry("700x800")



arkaCanvas = Canvas(uyeEkran, width=1350, height=720, bg="#9adbe8").place(x=0, y=0)
menuCanvas = Canvas(uyeEkran, width=500, height=550).place(x=100, y=100)

mainBanner=Label(uyeEkran, text="Gezgin Bilet Uygulaması",bg="#A7DFEA")
mainBanner.place(x=15, y=15)
mainBanner.config(font=("Arial", 28, "bold italic"))




# üye oluş ekranı
# ad-soyad
isim = Label(uyeEkran, text="AD SOYAD")
isim.place(x=130, y=190)
isim.config(font=("Arial", 12, "bold"))

isimGiris = Entry(uyeEkran, text="AD SOYAD")
isimGiris.place(x=330, y=190)
isimGiris.config(font=("Arial", 12, "bold"))

# eposta
ePosta = Label(uyeEkran, text="E-POSTA")
ePosta.place(x=130, y=230)
ePosta.config(font=("Arial", 12, "bold"))

ePostaGiris = Entry(uyeEkran, text="E-POSTA")
ePostaGiris.place(x=330, y=230)
ePostaGiris.config(font=("Arial", 12, "bold"))

# eposta giris
telNo = Label(uyeEkran, text="TELEFON NO")
telNo.place(x=130, y=270)
telNo.config(font=("Arial", "12", "bold"))

telNoGir = Entry(uyeEkran)
telNoGir.place(x=330, y=270)
telNoGir.config(font=("Arial", "12", "bold"))

# Şifre giriş
sifre = Label(uyeEkran, text="ŞİFRE")
sifre.place(x=130, y=310)
sifre.config(font=("Arial", 12, "bold"))

sifreGiris = Entry(uyeEkran, show="*", )
sifreGiris.place(x=330, y=310)
sifreGiris.config(font=("Arial", 12, "bold"))

# Şifre onay
sifreTekrar = Label(uyeEkran, text="ŞİFRE TEKRAR")
sifreTekrar.place(x=130, y=350)
sifreTekrar.config(font=("Arial", 12, "bold"))

sifreTekrarGiris = Entry(uyeEkran, show="*")
sifreTekrarGiris.place(x=330, y=350)
sifreTekrarGiris.config(font=("Arial", 12, "bold"))

uyeOlButon = Button(uyeEkran, text="ÜYE OL", bg='#ef6262',command=(yeni_kayit))
uyeOlButon.place(x=280, y=440)
uyeOlButon.config(font=("Arial", 15, "bold"))



uyeEkran.mainloop()