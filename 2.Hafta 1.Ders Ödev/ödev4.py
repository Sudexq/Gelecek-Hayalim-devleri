import datetime


def emeklilik_hesapla(dogum_yili, isim):
    
    #fonsiyon içinde fonksiyon
    def yas_hesapla(dogum_yili):
        mevcut_yil = datetime.datetime.now().year
        yas = mevcut_yil - dogum_yili 
        return yas 
    
    yas = yas_hesapla(dogum_yili) 
    
    #65 ten büyükse emekli
    if(yas>=65):
        print("Emekli oldunuz.")
    #değilse emeksiz
    else:
        print(f"{isim} emekli olmanıza {65-yas} yıl var.")
    
#değerleri alıyoruz
isim = input("Lütfen isminizi giriniz: ")
dogum_yili = int(input("Doğum yılınızı girin: ")) 

#Hesaplatıyoruz
emeklilik_hesapla(dogum_yili , isim)