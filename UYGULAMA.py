import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import mysql
import mysql.connector
import datetime
from tkinter import ttk
import os
import shutil




#ekran gövde ve başlık düzenlemeleri
#arkaplan resim boyutlandırma
app=tk.Tk()
app.title("Gezgin Seyahat")
app.state('zoomed')

resim=Image.open("background.gif")
boyut=width,heigth=resim.size
yresim=resim.resize((1368,740))

yukle=ImageTk.PhotoImage(yresim)
gor=Label(app,image=yukle)
gor.place(x=0,y=0)
mainBanner=Label(app, text="Gezgin Bilet Uygulaması",bg="#A7DFEA")
mainBanner.place(x=15, y=15)
mainBanner.config(font=("Arial", 28, "bold italic"))

anlik = datetime.datetime.now()
tarihsaat = Label(
    app,
    bg="#A7DFEA",
    text=anlik,
    font=("Arial", "10")
)
tarihsaat.place(x=430,y=85 ,anchor=W)

#KeyFunctions
def joker():
    pass
veritabani=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="test")


def seferEkran():
    import seferEkran

def pnrAra():
    import pnrSorEkran

def uyeOl():
    import uyeOlSayfa

def sefer_ekle():
    import seferEklesayfası

def sehirGetir(event):

    print("sehir seçildi")

def giris():
    import giris

    mycursor = veritabani.cursor()
    mycursor.execute("SELECT * FROM kullanicilar WHERE e_posta=" +ePostaGiris.get() and "SELECT * FROM kullanicilar WHERE sifre=" +sifreGiris2.get())
    sonuclar = mycursor.fetchall()
    if sonuclar:
        import giris
    else:

        hata=messagebox.showerror("Hata", "Giriş bilgilerinizi kontrol edin.")


def acenteGir():

    print("Acente giriş ekranı açıldı")
    acenteGirisEkran = Toplevel(app)
    acenteGirisEkran.title("Acenete giriş sayfası")


    acenteGirisEkran.geometry("700x800")
    arkaCanvas1 = Canvas(acenteGirisEkran, width=1350, height=720, bg="#9adbe8").place(x=0, y=0)
    menuCanvas1 = Canvas(acenteGirisEkran, width=500, height=550).place(x=100, y=100)

    banner=Label(acenteGirisEkran, text="Gezgin Bilet >> Acente Giriş Ekranı" ,bg="#A7DFEA")
    banner.place(x=15, y=15)
    banner.config(font=("Arial", 30,"bold italic" ))

    # kullanıcı adı
    kulAdı = Label(acenteGirisEkran, text="Kullanıcı Adı")
    kulAdı.place(x=210, y=270)
    kulAdı.config(font=("Arial", 12, "bold"))

    kulAdıGiris = Entry(acenteGirisEkran, text="Kullanıcı Adı")
    kulAdıGiris.place(x=330, y=270)

    kulAdıGiris.config(font=("Arial", 12, "bold"))

    # Şifre giriş
    sifre = Label(acenteGirisEkran, text="Şifre")
    sifre.place(x=210, y=300)
    sifre.config(font=("Arial", 12, "bold"))

    sifreGiris = Entry(acenteGirisEkran, show="*")
    sifreGiris.place(x=330, y=303)
    sifreGiris.config(font=("Arial", 12, "bold"))

    girisButon1 = Button(acenteGirisEkran, text="GİRİŞ", width=15, height=2, compound=TOP, command=sefer_ekle, bg='#ef6262')
    girisButon1.place(x=280, y=450)
    girisButon1.config(font=("Arial", 15, "bold"))





#ANASAYFA GİRİŞ EKRANI
menuCanvas=Canvas(app,width=500,height=550)
menuCanvas.place(x=100, y=100)

uyeGirisiBanner=Label(app,text="Üye Girişi")
uyeGirisiBanner.place(x=290,y=200)
uyeGirisiBanner.config(font=("Verdana", 30))

img=ImageTk.PhotoImage(Image.open("iconmonstr-user-19.png"))
panel=Label(app,image=img).place(x=345, y=120)


ePosta = Label(app, text="E-Posta")
ePosta.place(x=110, y=300)
ePosta.config(font=("Tahoma", 15, "bold"))


ePostaGiris = Entry(app, text="AD SOYAD",width=30)
ePostaGiris.place(x=235, y=300)
ePostaGiris.config(font=("Arial", 15, "italic"))


sifre = Label(app, text="Şifre")
sifre.place(x=110, y=400)
sifre.config(font=("Tahoma", 15, "bold"))

sifreGiris2 = Entry(app,show="*",width=30)
sifreGiris2.place(x=235, y=400)
sifreGiris2.config(font=("Arial", 15, "italic"))

girisButon=Button(app,text="GİRİŞ",width=15,height=2,compound=TOP,command=giris,bg='#ef6262')
girisButon.place(x=280,y=450)
girisButon.config(font=("Arial", 15, "bold"))


uyeButon=Button(app,text="ÜYE OL",width=15,height=2,compound=TOP,command=uyeOl,bg='#ef6262')
uyeButon.place(x=280,y=525)
uyeButon.config(font=("Arial", 15, "bold"))


acenteButon=Button(app,text="Acente Giriş",width=15,height=2,compound=TOP,command=acenteGir,bg='#ef6262')
acenteButon.place(x=300,y=600)
acenteButon.config(font=("Arial", 11, "bold"))

app.mainloop()



