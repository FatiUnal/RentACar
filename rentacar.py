class RentACar():
    def __init__(self,ad):
        self.ad = ad
        self.work = True

    def Program(self):
        seçenek = self.Menü()
        if seçenek == 1:
            self.ElemanEkle()
        if seçenek == 2:
            self.ElemanÇıkar()
        if seçenek == 3:
            self.AlınanArabalar()
        if seçenek == 4:
            self.SatılanArabalar()
        if seçenek == 5:
            self.ElemanListesi()
        if seçenek == 6:
            self.Çıkıs()
    
    def Menü(self):
        try:
            seçenek = int(input(f" {self.ad} Hoş Lütfen yapmak istediğiniz işlemi seçiniz\n1-Eleman Ekle\n2-Eleman çıkar\n3-Alınan Arabalar\n4-Satılan Arabalar\n5-Eleman Listesi\n6-Çıkış\nLütfen seçiniz:"))
        except ValueError:
            print("Lütfen sayı giriniz..")
        else:
            while seçenek >6 or seçenek <1:
                seçenek = int(input(f"Lütfen 1 ile 6 arasında seçim yapınız... "))
            return seçenek
    
    
    
    def ElemanEkle(self):
        Ad = input("İsim: ")
        Soyad = input("Soyadı: ")
        Yas = input("Yas: ")
        id = 1
        

        with open("Elemanlar.txt","r",encoding="utf-8") as dosya:
            xElemanlar = dosya.readlines()

        if len(xElemanlar) == 0:
            id = 1
        else:
            with open("Elemanlar.txt","r") as dosya:
                id = int(dosya.readlines()[-1].split(")")[0]) +1

        with open("Elemanlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(f"{id}){Ad}-{Soyad}-{Yas}\n")



    def ElemanÇıkar(self):
        with open("Elemanlar.txt","r") as dosya:
            elemanlar = dosya.readlines()

        cElemanlar = []
        for eleman in elemanlar:
            cElemanlar.append("".join(eleman.split("\n")))
        
        for i in cElemanlar:
            print(i)
            
            

        secim = int(input("Lütfen çıkarmak istediğiniz ıd yi seçiniz: "))
        while secim<1 or secim > len(elemanlar):
            secim = int(input(f"Lütfen 1 ile {len(elemanlar)} arasında bir seçim yapınız:  "))
        
        elemanlar.pop(secim-1)

        sayac = 1
        dEleman = []

        for eleman in elemanlar:
            dEleman.append(str(sayac)+")"+eleman.split(")")[1])
            sayac +=1


        with open("Elemanlar.txt","w",encoding="utf-8") as dosya:
            dosya.writelines(dEleman)
            


    def AlınanArabalar(self):
        marka = input("markasını giriniz: ")
        yıl = input("yılını giriniz: ")
        değer = input("değerini giriniz: ")
        no = 1
        
        with open("Arabalar.txt","r",encoding="utf-8") as dosya:
            ArabaListesi = dosya.readlines()

        if len(ArabaListesi) == 0:
            no = 1
        else:
            with open("Arabalar.txt","r") as dosya:
                no = int(dosya.readlines()[-1].split(")")[0])+1
            
        with open("Arabalar.txt","a",encoding="utf-8") as dosya:
            dosya.write(f"{no}) {marka}-{yıl}-{değer}\n")
    
    
    
    
    
        
    
    def SatılanArabalar(self):
        with open("Arabalar.txt","r") as dosya:
            araba = dosya.readlines()

        gAraba = []
        sayac = 1
        for car in araba:
            gAraba.append(str(sayac)+")"+car.split(")")[1])
            sayac+=1

        for i in gAraba:
            print("".join(i.split("\n")))

        secim = int(input("Lütfen satmak istediğiniz arabanın id numarasını yazınız:  "))
        while secim<1 or secim > len(gAraba):
            secim = int(input(f"Lütfen 1 ile {len(gAraba)} arasında bir seçim yapınız:  "))
        gAraba.pop(secim-1)

        with open("Arabalar.txt","w",encoding="utf") as dosya:
            dosya.writelines(gAraba)

        
    

    def ElemanListesi(self):
        with open("Elemanlar.txt","r") as dosya:
            elemans =dosya.readlines() # dosyayı okudum ve satırlar şeklinde eleman haline getirdim
        

        elemanlar = []
        for calısan in elemans:
            elemanlar.append(calısan)  # yeni bi liste olusturup okuduklarımı listeye aktardım

        for x in elemanlar:
            print("".join(x.split("\n")))  #burda \n den ayırıp birleştirdim bu sayede \n leri yok edebildim ve for la yazdıgımda 2 si arasında boşluğu kaldırdım 




    def Çıkıs(self):
        self.work = False


rent = RentACar("FaCar")
while rent.work:
    rent.Program()