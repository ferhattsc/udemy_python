
# a = 10
# b = 20
# c = 30

# a, b, c = 10, 20, 30

# a, b = b, a

# a += 5          #a = a + 5
# b -= 5          #b = b - 5
# c %= 5          #c = c % 5
# a **= 5         #a = a ** 5
# a //= 5         #a = a // 5

sayilar = (1,2,3,4,5,6)       #yeterli duzeyde eleman yoksa hata verir

# a,b,*c = sayilar
a,*b,c = sayilar

print(a, b, c)