
sonuc = all([True,True,True])
sonuc = any([True,False,True])

# True and True => True => All()
# True or False => True => Any()

sayilar = [0,1,4,7,8,10,15]
sonuc = [bool(sayi) for sayi in sayilar]
sonuc = any([bool(sayi) for sayi in sayilar])
sonuc = all([bool(sayi) for sayi in sayilar])
sonuc = all([bool(sayi) for sayi in sayilar if sayi%2==1])
sonuc = all([sayi%2==0 for sayi in sayilar])
sonuc = any([sayi%2==0 for sayi in sayilar])

isimler = ["ali","arda","mehmet","didem"]

sonuc = [isim[0]=="a" for isim in isimler]
sonuc = any([isim[0]=="a" for isim in isimler])


sonuc = print(sonuc)