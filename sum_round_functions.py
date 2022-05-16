
sayilar = [24,5,3,16,72]

sonuc = sum(sayilar)
sonuc = sum(sayilar, 100)

urunler = [
    {"title":"kitap a","price":25},
    {"title":"kitap b","price":35},
    {"title":"kitap c","price":45},
    {"title":"kitap d","price":55}
]

toplamFiyat = sum(urun["price"] for urun in urunler)
sonuc = toplamFiyat / len(urunler)

sonuc = round(5.2)  # 5
sonuc = round(1.343434, 2)  # 1.34







print(sonuc)