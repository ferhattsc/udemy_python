
from pickle import SHORT_BINUNICODE


iller = ["Istanbul","Ankara","Izmir","Bursa"]

sonuc = iller
sonuc = iller[2]
sonuc = iller[0:2]
sonuc = iller[2:]
sonuc = iller[:3]
sonuc = iller[-1]
sonuc = iller[-3:-1]

iller[0] = "Tekirdag"
iller[-1] = "Balikesir"

sonuc = len(iller)

sonuc = iller + ["Adana","Antalya"]

del iller[0]

print(iller)