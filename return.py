
# def adin_ne():
#     ad = input("Adinizi giriniz:")
#     print(ad)
#     return ad

# adin_ne()

# print("Sisteme hoş geldiniz",adin_ne())

# def topla():
#     return 20+30

# sonuc = topla() * 2

# print(sonuc)

saat = 15

def selamla():
    if (saat<12):
        return "Gunaydin"
    elif (saat>=12) and (saat<18):
        return "Iyi gunler"
    else:
        return "Iyi aksamlar"
    
sonuc = selamla() + ", Levent"

print(sonuc)