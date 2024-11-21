liste = ["Python", True, 9, "3", 8.4, "Hi-Kod", "False", 4.7]
#index:     0       1    2   3    4      5         6      7

'''Aşağıdaki işlemleri indexing ve slicing kullanarak liste üzerinde uygulayın.'''

# "3" değerine ulaşmak için indexleme
print(liste[3])  # Çıktı: "3"

# "Hi-Kod" değerine ulaşmak için indexleme
print(liste[5])  # Çıktı: "Hi-Kod"

# 4.7 değerine ulaşmak için indexleme
print(liste[7])  # Çıktı: 4.7

# 9, "3", 8.4, "Hi-Kod" değerlerine slicing ile ulaşmak
print(liste[2:6])  # Çıktı: [9, "3", 8.4, "Hi-Kod"]

# 8.4, "Hi-Kod", "False", 4.7 değerlerine slicing ile ulaşmak
print(liste[4:])  

# Çıktı: [8.4, "Hi-Kod", "False", 4.7]

