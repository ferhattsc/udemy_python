
sayilar = [1,3,9,14,28,36,3,36]
harfler = ["a","b","f","k","s","v","s"]

# sonuc = min(sayilar)    #en kucuk sayi
# sonuc = max(sayilar)    #en buyuk sayi
# sonuc = min(harfler)    #alfabenin ilk harfi
# sonuc = max(harfler)    #alfabenin son harfi

# #ekleme
# sayilar.append(20)      #dizinin sonuna 20 ekler
# harfler.append("l")
# sayilar.insert(3,12)    #dizinin 3. indeksine 12 ekler devam eder
# harfler.insert(5,"e")

# #silme
# sayilar.pop()           #dizinin son elemanini siler
# harfler.pop()
# sayilar.remove(14)      #"14" elemanini siler
# harfler.remove("f")     #"f"  elemanini siler

# #siralama
# sayilar.sort()          #sayilari siralar
# harfler.sort()          #alfabeye gore siralar
# sayilar.reverse()       #buyukten kucuge siralar
# harfler.reverse()       #alfabeyi sondan basa siralar

print(sayilar.count(3))   #3'un kac kere gectigini soyler
print(sayilar.index(3))   #3'un kacinci indekste gectigini soyler

sayilar.clear()
harfler.clear()

print(sayilar)
print(harfler)