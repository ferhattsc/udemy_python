
sayilar = [1,7,3,52,28,93,34]
harfler = ["b","a","v","k","d"]
isimler = ["ali","sercan","didem","eray","ahmet"]

sonuc = min(sayilar)
sonuc = max(sayilar)

sonuc = min(harfler)
sonuc = max(harfler)

sonuc = min(isimler)
sonuc = max(isimler)

sonuc = [len(isim) for isim in isimler]
sonuc = min([len(isim) for isim in isimler])
sonuc = max([len(isim) for isim in isimler])

sonuc = max(isimler, key=lambda n: len(n))
sonuc = min(isimler, key=lambda n: len(n))

araclar = [
    {"title":"Audi A4","price":500000},
    {"title":"Mercedes E","price":900000},
    {"title":"BMW 520","price":800000}
]

sonuc = min(araclar, key=lambda urun: urun["price"])
sonuc = max(araclar, key=lambda urun: urun["price"])
sonuc = min(araclar, key=lambda urun: urun["price"])["title"]
sonuc = max(araclar, key=lambda urun: urun["price"])["title"]

print(sonuc)

max = 0 

for urun in araclar:
    if urun["price"]>max:
        max = urun["price"]

print(max)