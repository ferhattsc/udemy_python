
# Identity Operator : is

# x = y = [1,2,3,4]
# z = [1,2,3,4]

# print(x == y)       #True
# print(x == z)       #True
# print(x is z)       #False
# print(x == y)       #True aynı bellekte yer aliyorlar

#Membership Operator : in

a = ["python","javascript"]

print("python" in a)
print("python2" in a)

email = "deneme@gmail.com"

print("@" in email)