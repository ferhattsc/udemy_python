name = "Osman"
surname = "Kaya"
age = "36"
text = "Benim adim " + name + " soyadim " + surname + ". Yasim "+ age + "."

print(text)

print(text[0])  #B
print(text[1])  #e
print(text[-1]) #.

print(text[0:5]) 
print(text[6:17])
print(text[:10])    # baslangici belirtmeden bitise kadar
print(text[10:])    # bitisi belirtmeden baslangictan basla

print(text[-20:-1])
print(text[0:30:2]) # ikiser atlaya atlaya yaz

print(text[::2])    # baslangic bitis belirtmeden ikiser atlayarak yaz
print(text[::-1])   # sagdan sola yazar(tersten)