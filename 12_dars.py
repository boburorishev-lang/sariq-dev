#1_topshiriq

# odam={"ism":"Bobur",
#       "yil":"2001",
#       "tugilgan_joy":"Toshkent"
#       }
# print(f"Mani ismim {odam['ism']}, {odam['yil']}-yilda, {odam['tugilgan_joy']} shaxrida tug'ilganman")


#2_topshiriq

# bollar={"Xasan":"osh",
#         "Husan":"beshbarmoq",
#         "Ali":"shorva",
#         "Vali":"lag'mon",
#         "G'ani":"manti"
#         }
# print(f"Xasanning sevimli taomi {bollar['Xasan']}")
# print(f"Alining sevimli taomi {bollar['Ali']}")
# print(f"G'anining sevimli taomi {bollar["G'ani"]}")


#3_topshiriq

python={"int":"butun son",
        "float":"o'nlik son",
        "str":"matn",
        "bool":"mantiqi son",
        "list":"royhat",
        "dict":"lugat",
        "if":"agar",
        "else":"aksholda",
        "in":"ichida",
        "for":"tsikl"
        }


#4_topshiriq

# soz=input("Kalit so'zni kiriting: ").lower()
# print(python.get(soz,"Bunday so'z mavjut emas"))


#5_topshiriq

soz=input("Kalit so'zni kiriting: ").lower()
tarjima=python.get(soz)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{soz.title()} so'zi {tarjima} deb tarjima qilinadi")