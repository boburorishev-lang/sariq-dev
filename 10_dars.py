#1_topshiriq

son=float(input("Juft son kiriting: "))
if son%2==0:
    print("Raxmat!")
else:
    print("Bu son juft emas.")


#2_topshiriq

yosh=int(input("Yoshingiz nikiriting: "))
if yosh<4 or yosh>60:
    narx=0
elif yosh<18:
    narx=10000
else:
    narx=20000

print(f"sizga kirish {narx} so'm")


#3_topshiriq

x=float(input("Birinchi soni kiriting: "))
y=float(input("Ikkinchi soni kiriting: "))

if x>y:
    print(f"{x}>{y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}={y}")


#4_topshiriq

mahsulotlar=['olma','nok',"uzum",'anjir','un','piva',"yog'","piyoz","tuxum","go'sht"]
savat=[]
for m in range(5):
    savat.append(input(f"Savatga {m+1}-mahsulotni qo'shing: "))

for t in savat:
    if t in mahsulotlar:
        print(f"Do'konimizda {t} bor")
    else:
        print(f"Do'konimizda {t} yo'q")


#5_topshiriq

mahsulotlar=['olma','nok',"uzum",'anjir','un','piva',"yog'","piyoz","tuxum","go'sht"]
savat=[]
bor_mahsulotlar=[]
mavjud_emas=[]
for m in range(5):
    savat.append(input(f"Savatga {m+1}-mahsulotni qo'shing: "))
for t in savat:
    if t in mahsulotlar:
        bor_mahsulotlar.append(t)
    else:
        mavjud_emas.append(t)
if mavjud_emas:
    print("Dokonimizda quyidagi mahsulotlar yo'q")
    for i in mavjud_emas:
        print(i)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


#6_topshiriq

foydalanuvchilar=["sway","bob","infinity_zero","nubik","admin"]
login=input("Yangi login tanlang: ")
if login.lower not in foydalanuvchilar:
    print("Xush kelibsiz!")
else:
    print("Login band, yangi login tanalng!")


#7_topshiriq

son=int(input("Istalgan butun son kiriting: "))

for i in range(2,11):
    if son%i==0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")