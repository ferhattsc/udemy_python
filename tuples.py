
list1 = [1,3,5,13,3]

thistuple = (1,2,"altı",False,2)          #thistuple = 1,2,"altı",False   bu sekilde de kullanilabilir
thistuple2 = (1,4,"bes",True,2)

# print(type(list1))
# print(type(thistuple))

# print(list1[0])
# print(thistuple[2])

# print(len(list1))
# print(len(thistuple))

list1[0] = 6
# thistuple[0] = 7                       #demetler degistirilemez dizilerdir

list1.append(45)
# thistuple.append(23)                   #demete eleman eklenemez

# print(list1.count(3))
# print(thistuple.count(2))

print(thistuple + thistuple2)

list2 = tuple([6,8,3,12])

print(type(list2))
print(list2)


# print(list1)
# print(thistuple)

