#1_topshiriq
cars=["toyota", "mazda", "huyundai", "gm", "kia"]
for car in cars:
    if car=="gm":
        print(car.upper())
    else:
        print(car.title())


#2_topshiriq

moshinalar=["toyota", "mazda", "huyundai", "gm", "kia"]
for moshina in moshinalar:
    if moshina!="gm":
        print(moshina.title())
    else: 
        print(moshina.upper())


#3_topshiriq

login=input("Loginizni kiriting >>> ")
if login.lower()=="admin":
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yzatini ko'rasizmi?")
else: print(f"Xush kelibsiz, {login}!")


#4_topshiriq

x=float(input("Birinchi son >>> "))
y=float(input("Ikkinchi son >>> "))
if x==y:
    print("Sonlar teng ekan")
else: print("Sonlar teng emas!")


#5_topshiriq

son=float(input("Hohalgan son kiriting >>> "))
if son<0:
    print("Manfiy son")
else:
    print("Musbat son")


#6_topshiriq

A=float(input("Son kiriting >>> "))
if A>0:
    print(f"{A} ing ildizi {A**(1/2)}")
else:
    print("Musbat son kiriting")