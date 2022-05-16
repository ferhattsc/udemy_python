
yazi = "   Benim adim Recep Sahin. Antalya'da yasiyorum   "

# sonuc = yazi.upper()        # hepsi buyuk yaz
# sonuc = yazi.lower()        # hepsi kucuk yaz
# sonuc = yazi.title()        # butun kelimelerin bas harfini buyuk yaz
# sonuc = yazi.capitalize()   # bas harfi buyuk yaz
# sonuc = yazi.isupper()      # karakterlerin hepsi kucuk mu true-false 
# sonuc = yazi.strip()        # bastaki sondaki bosluklari kaldir
# sonuc = yazi.split(".")     # noktaya gore dizilerine ayirir
# sonuc = "-".join(yazi)      # her bir karakterin arasina "-" koyar
# sonuc = yazi.index("Sahin") # aranan karakterin hangi indexten basladigini soyler
# sonuc = yazi.startswith("B")# baslangic B mi true-false
# sonuc = yazi.endswith(" ")  # bitis bosluk mu true-false
# sonuc = yazi.replace("Antalya","Konya")   #Antalya yerine Konya yazildi
sonuc = yazi.replace("ı","i").replace("ş","s")




print(sonuc)
