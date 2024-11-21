# Kullanıcıdan isim ve şifre isteği
isim = input("Lütfen isminizi girin: ")
dogru_sifre = input("Lütfen şifrenizi belirleyiniz: ")

print("\n--- Şifreniz Belirlendi! ---\n")

hak = 3  # Kullanıcının şifre girme hakkı

# Şifre kontrolü
while hak > 0:
    girilen_sifre = input("Tekrar şifrenizi girin: ")
    
    if girilen_sifre == dogru_sifre:
        print(f"\nSevgili {isim} başarılı bir şekilde giriş yaptın!")
        break
    else:
        hak -= 1
        print(f"\nYanlış şifre girildi! Kalan hakkınız: {hak}")
        
    # Üç yanlış denemede bitirme
    if hak == 0:
        print("\nÜç kez yanlış şifre girdiniz, program sonlanıyor.")
