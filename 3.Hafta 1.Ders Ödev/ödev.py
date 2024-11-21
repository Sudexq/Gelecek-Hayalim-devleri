# Öğrenci notlarını içeren sözlük
ogrenci_notlari = {
    "Sude": {"Matematik": 85, "Fizik": 90, "Kimya": 78},
    "Esma": {"Matematik": 92, "Fizik": 88, "Kimya": 84},
    "Enise": {"Matematik": 75, "Fizik": 80, "Kimya": 65},
    "Bulut": {"Matematik": 89, "Fizik": 85, "Kimya": 90},
}

'''
###NOTE
ogrenci_notlari["Sude"]  ----> {'Matematik': 85, 'Fizik': 90, 'Kimya': 78}

ogrenci_notlari["Sude"]["Fizik"] ----> 90

'''

def ogrenci_notlari_islemleri():
    while True:
        print("\n--- İşlem Menüsü ---")
        print("1. Bir öğrencinin notlarını görüntüle")
        print("2. Bir öğrencinin notunu güncelle")
        print("3. Yeni bir öğrenci ekle")
        print("4. Çıkış")
        
        secim = input("Bir işlem seçin (1/2/3/4): ")
        
        # 1. Bir öğrencinin notlarını görüntüle
        if secim == "1":
            isim = input("Öğrencinin adını girin: ").capitalize()
            ders = input("Ders adını girin (Matematik/Fizik/Kimya): ").capitalize()
            if isim in ogrenci_notlari and ders in ogrenci_notlari[isim]:
                print(f"{isim} adlı öğrencinin {ders} notu: {ogrenci_notlari[isim][ders]}")
            else:
                print("Öğrenci veya ders bulunamadı.")
        
        # 2. Bir öğrencinin notunu güncelle
        elif secim == "2":
            isim = input("Notunu değiştirmek istediğiniz öğrencinin adını girin: ").capitalize()
            ders = input("Hangi dersin notunu değiştirmek istiyorsunuz? (Matematik/Fizik/Kimya): ").capitalize()
            if isim in ogrenci_notlari and ders in ogrenci_notlari[isim]:
                yeni_not = int(input(f"{isim} adlı öğrencinin {ders} dersine yeni not girin: "))
                ogrenci_notlari[isim][ders] = yeni_not
                print(f"{isim} adlı öğrencinin {ders} notu güncellendi: {yeni_not}")
            else:
                print("Öğrenci veya ders bulunamadı.")
        
        # 3. Yeni bir öğrenci ekle
        elif secim == "3":
            isim = input("Yeni öğrencinin adını girin: ").capitalize()
            if isim in ogrenci_notlari:
                print("Bu öğrenci zaten mevcut.")
            else:
                matematik_notu = int(input("Matematik notunu girin: "))
                fizik_notu = int(input("Fizik notunu girin: "))
                kimya_notu = int(input("Kimya notunu girin: "))
                ogrenci_notlari[isim] = {
                    "Matematik": matematik_notu,
                    "Fizik": fizik_notu,
                    "Kimya": kimya_notu,
                }
                print(f"{isim} adlı öğrenci eklendi.")
        
        # 4. Çıkış
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


# Sözlük üzerinde işlemler yapmak için fonksiyonu çağırıyoruz
ogrenci_notlari_islemleri()

###NOTE
#capitalize() , kelimenin ilk harfini büyük yapar ve geri kalan tüm harfleri küçük hale getirir ki yanlış anlaşılma olmasın