
# def userInfo(*args):
#     print(type(args))

# userInfo()

# def userInfo(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     for key,value in kwargs.items():
#         print(f"{key}: {value}")
#         print("\n")

# userInfo(userName="leventert")
# userInfo(userName="leventert",password="123456",email="abc@gmail.com")

def siralama(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(*args)
    print(*kwargs)

siralama(1,2,3,4,5,6,key1="value1",key2="value2")
