import random

def yaziTura():
    yaziTuraListesi = []
    for para in range(100000):
        yaziTuraListesi.append(random.randrange(1,3))
    return yaziTuraListesi

def altiDefaPespese():
    listem = yaziTura()

    altiliGrup = []
    n = 0
    altiDefaPesPeseTura = 0

    while len(listem) >= 6:
        sayi = []
        for counter in listem[0:6]:
            sayi.append(counter)
        if sayi[0] == 2 and sayi[1] == 2 and sayi[2] == 2 and sayi[3] == 2 and sayi[4] == 2 and sayi[5] == 2:
            altiDefaPesPeseTura = altiDefaPesPeseTura + 1
            print(altiDefaPesPeseTura,": ",sayi)

        altiliGrup.append(sayi)
        listem.pop(0)
    print("Peşpeşe 6 defa tura gelme miktari :", altiDefaPesPeseTura)
    #print(altiliGrup)

print(yaziTura())
altiDefaPespese()
