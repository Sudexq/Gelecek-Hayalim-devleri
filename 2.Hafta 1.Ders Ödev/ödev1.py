
def daire_alani_hesapla(pi, yaricap):
    alan = pi * (yaricap ** 2)
    return alan

# Kullanıcıdan giriş alalım
pi = float(input("Pi değerini girin: "))
yaricap = float(input("Dairenin yarıçapını girin: "))

# Fonksiyonu çağır ve sonucu yazdır
alan = daire_alani_hesapla(pi, yaricap)
print(f"Dairenin alanı: {alan:.2f}")
