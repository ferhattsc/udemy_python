
sayilar = [-1,-3,-5,8,12]
str_sayilar = ["1","3","5","8","12"]
isimler = ["ayca","yagmur","kemal","tolga"]

kullanilar = [
    {"ad": "yagmur", "soyad": "yalcin"},
    {"ad": "kemal", "soyad": "solmaz"}
]

kareleri = []

# for sayi in sayilar:
#     kareleri.append(sayi ** 2)

# print(kareleri)

def kareAl(sayi):
    return sayi ** 2

sonuc = list(map(kareAl, sayilar))
sonuc = list(map(lambda sayi: sayi ** 2, sayilar))
sonuc = list(map(int, str_sayilar))
sonuc = list(map(abs, sayilar))
sonuc = list(map(float, sayilar))
sonuc = list(map(str.capitalize, isimler))
sonuc = list(map(str.upper, isimler))
sonuc = list(map(len, isimler))
sonuc = list(map(lambda x: x["ad"], kullanilar))
sonuc = list(map(lambda x: x["soyad"], kullanilar))

print(sonuc)