'''Enumerate methodunu araştırın ve aşağıdaki örneği enumerate methodu ile yapın.'''

meyveler = ["Elma", "Armut", "Kiraz", "Çilek"]

# enumerate ile indeks ve değerleri yazdırma
for index, meyve in enumerate(meyveler):
    print("{}. indexte bulunan meyve: {}".format(index, meyve))

# Çıktı:
# 0. indexte bulunan meyve: Elma
# 1. indexte bulunan meyve: Armut
# 2. indexte bulunan meyve: Kiraz
# 3. indexte bulunan meyve: Çilek