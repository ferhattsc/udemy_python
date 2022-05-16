
# int
# float
# str
# bool

from unicodedata import name


age = 28
weight = 55.6
name = "Sinem"    #tek tirnak da kullanilabilir
isStudent = False

print(type(age))
print(type(weight))
print(type(name))
print(type(isStudent))

# int to float

result = float(age)
print(result)

# float to int
result = int(weight)
print(result)

# bool to str

result = str(isStudent)
print(result)
print(type(result))

# bool to int

result = int(isStudent)
print(result)
print(type(result))