
# -*- coding: utf-8 -*-
class Dosya:
    def __init__(self,dosya):
        self.dosya = dosya    
    def otomasyon(self):    
        self.dosya = open("ogrenci_bilgileri.txt")
        print("""
        Öğrenci Otomasyonuna Hoş Geldiniz
        ----------Yapabileceğiniz İşlemler----------
            1- Öğrenci Kayıt
            2- Öğrenci Sorgulama
            3- Öğrenci Kayıt Silme
        """)

        secim = int(input("Yapmak istediğiniz işlemi seçin: "))

        while True:
            if secim == 1:
                self.dosya = open("ogrenci_bilgileri.txt","a")
                isim = input("Eklemek isdeğiniz öğrencinin adı:")
                soyisim = input("Eklemek isdeğiniz öğrencinin soyadı:")
                id = input("Eklemek isdeğiniz öğrencinin kullanıcı adı:")
                sinif = input("Eklemek isdeğiniz öğrencinin sınıfı:")
                yas = int(input("Eklemek isdeğiniz öğrencinin yaşı:"))
                cinsiyet = input("Eklemek isdeğiniz öğrencinin cinsiyeti:")
                self.dosya.write("Öğrencinin adı:"+isim)
                self.dosya.write("\t")
                self.dosya.write("Öğrencinin soyadı:"+soyisim)
                self.dosya.write("\t")
                self.dosya.write("Öğrencinin kullanıcı adı:"+id)
                self.dosya.write("\t")
                self.dosya.write("Öğrencinin sınıfı:"+sinif)
                self.dosya.write("\t")
                self.dosya.write("Öğrencinin yaşı:"+str(yas))
                self.dosya.write("\t")
                self.dosya.write("Öğrencinin cinsiyeti:"+cinsiyet)
                self.dosya.write("\n")
                break
            
            elif secim == 2:
                sorgu = input("Hangi öğrenciyi sorgulamak istiyorsun:")
                self.dosya = open("ogrenci_bilgileri.txt","r")
                
                for i in self.dosya:
                    if sorgu in i:
                        print("Öğrenci hakkında bilgiler:\n",i)
                self.dosya.close()
                break
            
            elif secim == 3:
                a = int(input("Silmek istediğiniz satır:"))
                self.dosya = open("ogrenci_bilgileri.txt","r")
                lines = self.dosya.readlines()
                self.dosya.close()

                del lines[a]

                self.yeni_dosya = open("ogrenci_bilgileri.txt","w+")
                for line in lines:
                    self.yeni_dosya.write(line)
                    
                self.yeni_dosya.close()
                break
            
            else:
                print("Hatalı seçim yaptınız!!!")
                break
nesne = Dosya("dosya")
nesne.otomasyon()            