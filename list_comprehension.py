
sayilar = []

# for i in range(10):
#     sayilar.append(i)
# print(sayilar)

# [exression for item in list]

# sayilar = [i for i in range(10)]
# sayilar = [i*2 for i in range(10)]
# sayilar = [i*i for i in range(10)]

liste = [3,8,5,12,40]

sayilar = [i*2 for i in liste]
sonuc = [str(sayi) for sayi in liste]

isim = "Levent"
isimler= ["Ayca","Doga","Kaan","Melih"]

sonuc = [a.upper() for a in isim]
sonuc = [i.lower() for i in isimler]


print(sonuc)