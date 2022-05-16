
#And Operation

x = 15

sonuc = (x > 10) and (x < 20)       # sonuc = 10 < x < 20

# True and True => True
# True and False => False
# False and False => False

karne_notu = 90
devamsizlik = 3

sonuc = (karne_notu >= 50) and (devamsizlik < 10)

#Or Operation

# True or True => True
# True or False => True
# False or False => False

sonuc = (x < 10) or (x % 3 == 0)

#Not Operation

x = -15
sonuc = not(x > 0)

ceza_bilgisi = False

sonuc = (karne_notu >= 85) and (devamsizlik < 10) and (ceza_bilgisi == False)

print(sonuc)