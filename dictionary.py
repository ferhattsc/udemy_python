
# 34 => Istanbul
# 35 => Izmir

# sehirler = ["Istanbul","Izmir"]
# plakalar = [34,35]

# print(plakalar[0],sehirler[0])
# print(plakalar[1],sehirler[1])

# print(plakalar[sehirler.index("Istanbul")])
# print(plakalar[sehirler.index("Izmir")])

# key - value

# plakalar = {"Izmir":35, "Istanbul":34}

# print(plakalar["Izmir"])
# print(plakalar["Istanbul"])

# plakalar["Eskisehir"] = 26
# plakalar["Bursa"] = 16
# print(plakalar)

urunler = {
    100: {
        "urunAdi" : "Monitor",
        "urunAciklamasi" : "16 inc",
        "garantiSuresi" : 3,
        "fiyat" : [800,944]
    },
    101: {
        "urunAdi" : "SSD",
        "urunAciklamasi" : "256 GB",
        "garantiSuresi" : 2,
        "fiyat" : [1500,1770]
    }
}

sonuc = urunler[100]["fiyat"]

tutar = urunler[100]["fiyat"][1] + urunler[101]["fiyat"][1]


print(tutar)