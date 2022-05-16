
arabaAudi = {
    "marka" : "Audi",
    "model" : "A5",
    "yil"   : 2019
}

#degerlere erisme

# sonuc = arabaAudi["marka"]
# sonuc = arabaAudi.get["marka"]

#sorgualama islemleri

# sonuc = "marka" in arabaAudi        #marka arabaAudi icinde var mi true-false

# sonuc = len(arabaAudi)

# #ekleme islemi

# arabaAudi["renk"] = "siyah"

# #silme islemi

# arabaAudi.pop("yil")
# arabaAudi.popitem()                 #son elemani sil

# del arabaAudi["marka"]

# #del arabaAudi                        #objeyi siler

# arabaAudi.clear()                     #icerisindeki degerleri siler

# # objeyi kopyalama

# araba = arabaAudi.copy()

# araba["marka"] = "mercedes"
# araba["model"] = "amg"

# deger guncelleme

arabaAudi.update({
    "marka" : "BMW",
    "renk"  : "beyaz"
})
print(arabaAudi)