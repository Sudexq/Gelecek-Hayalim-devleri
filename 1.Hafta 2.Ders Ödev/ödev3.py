# Kullanıcıdan şifre isteği
while True:
    sifre = input("Şifrenizi oluşturun (5 ile 10 karakter arasında): ")
    
    # Şifre uzunluğunu kontrol etme
    if 5 <= len(sifre) <= 10:
        print("Hesabınız oluşturuldu.")
        break
    else:
        print("Lütfen şifreniz 5 haneden az, 10 haneden fazla olmasın!")
