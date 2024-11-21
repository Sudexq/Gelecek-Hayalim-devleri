import numpy as np

# Sıfırlardan oluşan array
zeros_array = np.zeros((2, 3), dtype=int)

# Birlerden oluşan array
ones_array = np.ones((2, 3), dtype=int)

print("\nSıfırlardan oluşan array:\n", zeros_array)
''' 
[[0 0 0]
 [0 0 0]]
 
'''
print("Birlerden oluşan array:\n", ones_array)
'''
[[1 1 1]
 [1 1 1]]
 
'''
# Arrayleri satır bazında birleştirme
concat_row = np.vstack((zeros_array, ones_array))
print("\nSatır bazında birleştirilmiş array:\n", concat_row)
'''
[[0 0 0]
 [0 0 0]
 [1 1 1]
 [1 1 1]]
 
'''
# Arrayleri sütun bazında birleştirme
concat_column = np.hstack((zeros_array, ones_array))
print("\nSütun bazında birleştirilmiş array:\n", concat_column)
'''
[[0 0 0 1 1 1]
 [0 0 0 1 1 1]]
 
'''
