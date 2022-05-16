
# def us_alma(a):
#     return a ** 2

# print(us_alma(5))

# lambda arguments : expression

# sonuc = (lambda a: a ** 2)(2)

# print(sonuc)

# us_alma = lambda a: a ** 2
# sonuc = us_alma(6)

# print(sonuc)

# tersCevir = lambda x: x[::-1]
# sonuc = tersCevir("Levent Ertunalilar")

# print(sonuc)

def fn1(n):
    return lambda a: a ** n

us_alma2= fn1(2)

sonuc = us_alma2(5)
print(sonuc)