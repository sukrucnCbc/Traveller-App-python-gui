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
    passwd="",
    database="gezgin_app")

def seferiEkle():
    global sorgu
    mycursor = veritabani.cursor()
    sorgu = "INSERT INTO seferler(sefer_kodu, firma_adi,kalkis_ist,varis_ist, sefer_tarihi, saat, fiyat, arac_plaka)" \
            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    deger = [skod.get(),
             firmalar1.get(),
             sehirler1.get(),
             sehirler2.get(),
             guncombo.get(),
             sgir7.get(),
             fiyat.get(),
             plaka.get()
             ]
    mycursor.execute(sorgu, deger)
    veritabani.commit()
    print(mycursor.rowcount, "Sefer Eklendi")
    bilgi = messagebox.showinfo("İşlem Tamamlandı", "Kayıt başarılı bir şekilde eklendi.")
    if bilgi == "ok":
        pass

    else:
        pass


sehirList1= ["Şehir Seç", "İSTANBUL", "ANKARA", "TRABZON", "İZMİR", "KOCAELİ", "RİZE", "GİRESUN", "ORDU", "SAMSUN","ÇORUM"]


print("Acente sefer ekleme ekranı açıldı")
seferEkleEkran = Tk()
seferEkleEkran.title("Acenete Sefer Ekleme Ekranı")

seferEkleEkran.geometry("700x800")
arkaCanvas1 = Canvas(seferEkleEkran, width=1350, height=720, bg="#9adbe8").place(x=0, y=0)
menuCanvas1 = Canvas(seferEkleEkran, width=600, height=550).place(x=50, y=100)

mainBanner=Label(seferEkleEkran, text="Gezgin Bilet Uygulaması >> Sefer Ekle",bg="#A7DFEA")
mainBanner.place(x=15, y=15)
mainBanner.config(font=("Arial", 28, "bold italic"))


#sefer kodu label
se1 = Label(seferEkleEkran, text="Sefer Kodu PNR")
se1.place(x=100, y=120)
se1.config(font=("Arial", 12, "bold"))
#sefer kodu entry
skod = Entry(seferEkleEkran, width=30, font=("Arial", 12, "bold"))
skod.place(x=250, y=120)

# firma adı label
firma = Label(seferEkleEkran, text="Firma Adı")
firma.place(x=100, y=170)
firma.config(font=("Arial", 12, "bold"))
# firma adı combobox
firmalar1 = ttk.Combobox(seferEkleEkran, width=30)
firmalar1['values'] = (
    "Firma Seç","Metro Turizm", "Ali Osman Ulusoy", "Mis Amasya Tur", "Nilüfer Turizm", "Kamil Koç Turizm"
)
firmalar1.place(x=250, y=170)
firmalar1.current(0)
firmalar1.config(font=("Arial", 12, "bold"))

#kalkış durağı label
se3 = Label(seferEkleEkran, text="Kalkış Durağı")
se3.place(x=100, y=210)
se3.config(font=("Arial", 12, "bold"))
#kalkış durağı combobox
sehirler1=ttk.Combobox(seferEkleEkran,width=30)
sehirler1['values'] = sehirList1
sehirler1.place(x=250, y=210)
sehirler1.current(0)
sehirler1.config(font=("Arial", 12, "bold"))

# varış durağı label
se4 = Label(seferEkleEkran, text="Varış Durağı")
se4.place(x=100, y=270)
se4.config(font=("Arial", 12, "bold"))
# varış durağı combobox
sehirler2 = ttk.Combobox(seferEkleEkran, width=30)
sehirler2['values'] = sehirList1
sehirler2.place(x=250, y=270)
sehirler2.current(0)
sehirler2.config(font=("Arial", 12, "bold"))




#tarih label
seferTarihi = Label(seferEkleEkran,text="Sefer Tarihi",font=("Arial", 12, "bold"))
seferTarihi.place(x=100, y=310)
guncombo = ttk.Combobox(seferEkleEkran, width=5)
guncombo['values'] = (
    "Gün", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
    "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"
)
guncombo.place(x=250,y=310)
guncombo.current(0)

aycombo = ttk.Combobox(seferEkleEkran, width=8)
aycombo['values'] = (
    "Ay", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım",
    "Aralık"
)
aycombo.place(x=330, y=310)
aycombo.current(0)

yilcombo = ttk.Combobox(seferEkleEkran, width=7)
yilcombo['values'] = (
    "Yıl", "2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008",
    "2007",
    "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996", "1995", "1994", "1993",
    "1992", "1991", "1990", "1989", "1988", "1988", "1987",
    "1986", "1985", "1984", "1983", "1982", "1981", "1980")
yilcombo.place(x=430,y=310)
yilcombo.current(0)

# saat label
saat = Label(seferEkleEkran, text="Saat", font=("Arial", 12, "bold"))
saat.place(x=100, y=350)
saat.config(font=("Arial", 12, "bold"))
# fiyat entry
sgir7 = Entry(seferEkleEkran, width=10, font=("Arial", 12, "bold"))
sgir7.place(x=250, y=350)

# fiyat label
se6 = Label(seferEkleEkran, text="Fiyat", font=("Arial", 12, "bold"))
se6.place(x=100, y=390)
se6.config(font=("Arial", 12, "bold"))
# fiyat entry
fiyat = Entry(seferEkleEkran, width=10, font=("Arial", 12, "bold"))
fiyat.place(x=250, y=390)

#araç plaka label
se2 = Label(seferEkleEkran, text="Araç Plaka", font=("Arial", 12, "bold"))
se2.place(x=100, y=420)
se2.config(font=("Arial", 12, "bold"))
#araç plaka entry
plaka = Entry(seferEkleEkran, width=30, font=("Arial", 12, "bold"))
plaka.place(x=250, y=420)

ekleButon = Button(seferEkleEkran, text="Seferi Ekle", width=15, height=2, compound=TOP, command=seferiEkle,bg='#ef6262')
ekleButon.place(x=300, y=450)
ekleButon.config(font=("Arial", 12, "bold"))

mainloop()
