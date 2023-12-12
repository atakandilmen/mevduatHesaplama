
## Atakan Dilmen
#  Günlük Faiz Getirisi = (Anapara / 100) x (Faiz Oranı / 365) x Gün Sayısı
#  Aylık Faiz Getirisi = (Anapara / 100) x (Faiz Oranı / 12) x Ay Sayısı
#  Yıllık Faiz Getirisi = (Anapara / 100) x (Faiz Oranı) x Yıl Sayısı

def faiz_hesapla(mevduat_tutari, mevduat_gun, mevduat_faizi):
    faiz = (mevduat_tutari/100) * (mevduat_faizi / 365) * mevduat_gun
    return faiz

mevduat_tutari = float(input("Mevduat Tutarı: "))
mevduat_gun = int(input("Mevduat Gün: "))
mevduat_faizi = float(input("Mevduat Faizi: "))


faiz = faiz_hesapla(mevduat_tutari, mevduat_gun, mevduat_faizi)

toplam_mevduat = mevduat_tutari + faiz

print(f"{mevduat_gun} gün sonundaki mevduatınızın toplam getirisi: {faiz:.2f} TL, Hesabınızdaki toplam bakiye {toplam_mevduat:.2f} TL ")
