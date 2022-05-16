# list
# tuple
# dictionary
# sets      => indekslenemez, siralanamaz

markalar = {"Audi","Mercedes","Bmw","Honda"}
markalar2 = {"Renault","Toyota","Mazda"}

# sorgulama

sonuc = "Bmw" in markalar

markalar.add("Opel")        #rastgele atar siralama onemsiz
markalar.update(["Toyoya","Scoda"])

# sonuc = len(markalar)

# markalar.remove("Opel")

# sonuc = markalar.pop()
# markalar.clear()

sonuc = markalar.union(markalar2)

print(sonuc)