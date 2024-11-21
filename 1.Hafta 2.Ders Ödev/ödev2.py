# Kullanıcıdan şifre uzunluğunu kontrol etme
sifre = input("6 haneli şifrenizi oluşturun: ")

if len(sifre) >= 6:
    print("Hesabınız oluşturuldu.")
else:
    print("Şifreniz en az 6 haneli olmalıdır.")
