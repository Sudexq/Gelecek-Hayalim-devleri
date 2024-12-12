import pandas as pd

# Sözlükten DataFrame oluşturma
sozluk = {
    "Kategori": ["Giyim", "Giyim", "Ayakkabı", "Aksesuar", "Ayakkabı", "Giyim", "Aksesuar", "Aksesuar", "Ayakkabı", "Giyim"],
    "Ürün": ["Kazak", "T-shirt", "Sandalet", "Küpe", "Spor Ayakkabı", "Pantolon", "Kolye", "Yüzük", "Çizme", "Ceket"],
    "Fiyat": [300, 180, 450, 50, 700, 400, 150, 80, 850, 900]
}

df = pd.DataFrame(sozluk)

# 2. indexte bulunan kategori ve ürün bilgisi
kategori_2_index = df.loc[2, "Kategori"]
urun_2_index = df.loc[2, "Ürün"]

# 4. indexten 9. indexe kadar olan veriler
veriler_4_9 = df.loc[4:9]

# 1. indexten 6. indexe kadar olan ürünler
urunler_1_6 = df.loc[1:6, "Ürün"]

# Giyim, Ayakkabı ve Aksesuar kategorisindeki ürünler
giyim_urunleri = df[df["Kategori"] == "Giyim"]
ayakkabi_urunleri = df[df["Kategori"] == "Ayakkabı"]
aksesuar_urunleri = df[df["Kategori"] == "Aksesuar"]

# Giyim kategorisinde fiyatı 300'den fazla olan ürünler
giyim_fiyat_300 = df[(df["Kategori"] == "Giyim") & (df["Fiyat"] > 300)]

# Ayakkabı kategorisinde fiyatı 600'den az olan ürünler
ayakkabi_fiyat_600 = df[(df["Kategori"] == "Ayakkabı") & (df["Fiyat"] < 600)]

# Aksesuar kategorisinde fiyatı 100'den fazla olan ürünler
aksesuar_fiyat_100 = df[(df["Kategori"] == "Aksesuar") & (df["Fiyat"] > 100)]

# Sonuçları yazdırma
print("Kategori (2. index):", kategori_2_index)
print("Ürün (2. index):", urun_2_index)
print("\nVeriler (4-9 index):")
print(veriler_4_9)
print("\nÜrünler (1-6 index):")
print(urunler_1_6)
print("\nGiyim Ürünleri:")
print(giyim_urunleri)
print("\nAyakkabı Ürünleri:")
print(ayakkabi_urunleri)
print("\nAksesuar Ürünleri:")
print(aksesuar_urunleri)
print("\nGiyim Fiyat > 300:")
print(giyim_fiyat_300)
print("\nAyakkabı Fiyat < 600:")
print(ayakkabi_fiyat_600)
print("\nAksesuar Fiyat > 100:")
print(aksesuar_fiyat_100)
