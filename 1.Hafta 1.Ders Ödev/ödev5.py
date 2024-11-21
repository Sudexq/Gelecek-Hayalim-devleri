# Metin tanımlama
text = "Hi-Kod Veri Bilimi Atölyesi"

# Kelimeleri seçme
words = text.split()  # Boşluklardan ayırma
print(words)  # ['Hi-Kod', 'Veri', 'Bilimi', 'Atölyesi']

# Büyük harfe çevirme
uppercase_text = text.upper()
print(uppercase_text)  # 'HI-KOD VERİ BİLİMİ ATÖLYESİ'

# Küçük harfe çevirme
lowercase_text = text.lower()
print(lowercase_text)  # 'hi-kod veri bilimi atölyesi'

# Sayılardan çift ve tek sayıları ayırma
numbers = "0123456789"
even_numbers = ''.join([ch for ch in numbers if int(ch) % 2 == 0])
odd_numbers = ''.join([ch for ch in numbers if int(ch) % 2 != 0])

print("Çift sayılar:", even_numbers)  # "02468"
print("Tek sayılar:", odd_numbers)    # "13579"
