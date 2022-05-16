# value types => string, number

sayi1 = 10
sayi2 = 20

sayi1 = sayi2

sayi2 = 30

print(sayi1,sayi2)

#reference types => list

a = ["python","javascript"]
b = ["python","javascript"]

a = b                   #ayni adres icerisinde tutulmaya baslaniyor
b[0] = "html"           #a dizisi de bundan etkilenir

print(a,b)

