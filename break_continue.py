
# isim = "Levent Ertunalilar"

# for harf in isim:
#     if (harf == "v"):
#         break
#     print(harf)

i = 0
while (i < 10):
    i += 1
    if (i == 5):
        continue
    print(i)
print("dongu bitti")

#1-100 arasindaki tek sayilarin toplami

i = 0
toplam = 0

while(i <= 100):
    i += 1
    if (i % 2 == 0):
        continue
    toplam += i
print(f'toplam: {toplam}')