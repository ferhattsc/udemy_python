
# liste = [1,2,3,4]
# print(len(liste))

# isim = "Levent Ertunalilar"
# print(len(isim))

class Urun:
    def __init__(self, urunkodu, urunadi, fiyati):
        self.urunkodu = urunkodu
        self.urunadi = urunadi
        self.fiyati = fiyati
    
    def __len__(self):
        return self.fiyati

    def __str__(self):
        return f"{self.urunkodu}, {self.urunadi} urun listelendi."

    def __del__(self):
        print("urun objesi silindi.")

urun1 = Urun("123123123","TV",5000)

print(len(urun1))
print(str(urun1))

del urun1