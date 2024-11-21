import datetime #şu anki yılı almak için kütüphane

def yas_hesapla(dogum_yili):
    mevcut_yil = datetime.datetime.now().year #2024 seneye 2025
    yas = mevcut_yil - dogum_yili # yas = 2024-2004 seneye 2025-2004
    return yas #20

# Kullanıcıdan giriş alalım
dogum_yili = int(input("Doğum yılınızı girin: ")) #2004 

# Fonksiyonu çağır ve sonucu yazdır
yas = yas_hesapla(dogum_yili) #20 seneye 21
print(f"Yaşınız: {yas}") #20 seneye 21

#kütüphane sayesinde dinamik bir hesaplama fonksiyonu oluşturmuş olduk