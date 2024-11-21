import numpy as np

# İki boyutlu array
arr_2d = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)

# Üç boyutlu array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]], dtype=int)

# Array bilgileri
print("\nİki boyutlu array:\n", arr_2d)
'''
İki boyutlu array:
 [[1 2 3]
  [4 5 6]]
 
'''
print("Boyut:", arr_2d.ndim) #Boyut: 2
print("Eleman sayısı:", arr_2d.size) #Eleman sayısı: 6
print("Satır sayısı:", arr_2d.shape[0])  # Satır sayısı: 2
print("Sütun sayısı:", arr_2d.shape[1])  # Sütun sayısı: 3

print("\nÜç boyutlu array:\n", arr_3d)
'''
Üç boyutlu array:
 [[[1 2]
   [3 4]]

 [[5 6]
  [7 8]]]
  
'''
print("Boyut:", arr_3d.ndim) #Boyut: 3
print("Eleman sayısı:", arr_3d.size) #Eleman sayısı: 8
print("Şekil (Satır x Sütun x Derinlik):", arr_3d.shape) #Şekil (Satır x Sütun x Derinlik): (2, 2, 2)


# İki boyutlu array üzerinde indexleme
print("\nİki boyutlu array üzerinde indexleme:")
print("İlk satır, ikinci eleman:", arr_2d[0, 1])  # İlk satır, ikinci eleman: 2

# Üç boyutlu array üzerinde indexleme
print("\nÜç boyutlu array üzerinde indexleme:")
print("Birinci matrisin (0. eksen) ikinci satır, birinci sütunu:", arr_3d[0, 1, 0]) #Birinci matrisin (0. eksen) ikinci satır, birinci sütunu: 3

# Slicing (Dilimleme)
print("\nİki boyutlu array üzerinde slicing:")
print("İlk iki satır, tüm sütunlar:\n", arr_2d[:2, :])
'''
[[1 2 3]
 [4 5 6]]
 
'''
print("\nÜç boyutlu array üzerinde slicing:")
print("Birinci matrisin tüm satır ve sütunları:\n", arr_3d[0, :, :])
''' 
[[1 2]
 [3 4]]
 
'''
