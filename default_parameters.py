
# def selamla(isim="Kullanici",mesaj="Hosgeldin"):
#     print(f"{mesaj} {isim}")

# selamla("Mehmet","Merhaba")
# selamla("Selin")
# selamla()

# def usAlma(taban,us=2):
#     return taban ** us

# sonuc = usAlma(2)

# print(sonuc)

def carpma(a,b):
    return a * b

def toplama(a,b):
    return a + b

def islem(a,b,fn):
    return fn(a,b)

sonuc = islem(10,5,toplama)

print(sonuc)