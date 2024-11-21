liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]

'''Verilen listede bulunan string veri tipindeki öğeleri yeni_liste isimli listeye eklenir.'''

# Yeni listeyi oluşturma
yeni_liste = [eleman for eleman in liste if isinstance(eleman, str)]
print(yeni_liste)  

# Çıktı: ["Python", "3", "Hi-Kod", "False"]
