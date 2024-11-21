def faktoriyel(sayi):
    sonuc = 1
    for i in range(1, sayi + 1):
        sonuc *= i
    return sonuc

# Kullanıcıdan giriş alalım
sayi = int(input("Bir tamsayı girin: "))

# Fonksiyonu çağır ve sonucu yazdır
print(f"{sayi} sayısının faktöriyeli: {faktoriyel(sayi)}")
