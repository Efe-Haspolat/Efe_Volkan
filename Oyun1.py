
import random

kalan_para = 1000
oynanacak_para = 50
bahis_rengi = 0
kalan_zaman = 300

def acilis_ekrani():
    print("                   OYUN KURALLARI")
    print("                   Oyuna 1000 Euro ile Başlıyoruz")
    print("                   Oyunda siyah ve kırmızı tercih seçeneğimiz var:")
    print("                   Oyun pulunuzu bunlardan birine yatıracaksınız")
    print("                   İlk oyun 50 Euro dan başlayacak")
    print("                   Kaybedince kaybettiğinin iki katı koyacaksın ")
    print("                   Kazandığın zaman Kazandığın kadar koyacaksın")
    print("                   Maximum 5 saat sürecek oyun")
    print("")
    print("                   Hazırsanız başlamak için bir tuşa ve  Enter basınız")
    input()


def oyuna_basla():
    global kalan_para
    global oynanacak_para
    global kalan_zaman
    sansli_renk = 0
    while True:
        try:
            while True:
                bahis_rengi = int(input("Rengini Seç :Kırmızı için 1 i Siyah için 2 yi giriniz: "))
                print("")
                if bahis_rengi > 2 or bahis_rengi == 0:
                    print("" * 2)
                    print("!!!!!  sadece 1 veya 2 rakamı lütfen !!!!!")
                else:
                    break
            sansli_renk = random.randrange(1, 3)

        except ValueError:
            print("Hatali giriş:Karekter girmeyiniz ve lütfen sadece 1 veya 2 rakamini giriniz")
            print("" * 2)
            print("Tekrar Giriniz")
        except Exception:
            print("beklenmeyen Hata")
            
        else:


            if bahis_rengi == sansli_renk:
                print("***  TEBRİKLER KAZANDINIZ  ***")
                print("")
                kalan_para = kalan_para + oynanacak_para
                oynanacak_para = oynanacak_para
                kalan_zaman = kalan_zaman - 5
                print("")

            else:
                print("***   ÜZGÜNÜM KAYBETTİNİZ  ***")
                print("")
                kalan_para = kalan_para - oynanacak_para
                oynanacak_para = oynanacak_para * 2
                kalan_zaman = kalan_zaman - 5
                print("")
            break



acilis_ekrani()
print("xxxxxxxxxxxxxxxxxx       Oyuna Başliyoruz      xxxxxxxxxxxxxx")

while True:
    print("Kalan Zamanınız: " , kalan_zaman,"dakika")
    print("Mevcut Paranız",kalan_para,"Euro")
    print("Oyuna süreceğin Para",oynanacak_para)
    if kalan_zaman == 0 or kalan_para == 0 or kalan_para < oynanacak_para:

        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx       oyun bitti         xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        break
    else:
        oyuna_basla()
