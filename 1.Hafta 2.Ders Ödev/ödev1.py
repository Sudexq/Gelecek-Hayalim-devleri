# Kullanıcıdan maaş bilgisini alıyoruz
maas = float(input("Maaşınızı girin: "))

# Vergi kesintisi hesaplama
if maas <= 10000:
    kesinti = maas * 0.05  # %5
elif maas <= 25000:
    kesinti = maas * 0.10  # %10
elif maas <= 45000:
    kesinti = maas * 0.25  # %25
else:
    kesinti = maas * 0.30  # %30

# Yeni maaşı hesaplama
yeni_maas = maas - kesinti

# Sonucu yazdırma
print(f"Yeni maaşınız: {yeni_maas} TL")
