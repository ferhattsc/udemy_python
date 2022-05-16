
# for item in liste:
#     if (kosul):
#         expression

# [expression for item in liste if kosul]

sayilar = [1,3,7,12,22,34]
sonuc = []

# for sayi in sayilar:
#     if(sayi % 2 == 0):
#         sonuc.append(sayi)

# sonuc = [sayi for sayi in sayilar if sayi % 2 == 0]
sonuc = [sayi if sayi%2==1 else "cift sayi" for sayi in sayilar]

print(sonuc)
