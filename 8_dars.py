#1_topshiriq

ismlar=["Ali","Vali","Gani","Salim","Sattor"]
for ism in ismlar:
    print(f"Salom {ism}")
print(f"kod {len(ismlar)} marta takrorlandi")


#2_topshiriq

sonlar=list(range(11,100,2))
print(sonlar)
for son in sonlar:
    print(son**3)


#3_topshiriq

kinolar=[]
print("5 ta kinoni kiriting ")
for kino in range(5):
    kinolar.append(input(f"{kino+1}-kinoni kiriting "))
print(kinolar)


#4_topshiriq

odam_soni=int(input("bugun nechta odam bilan korishdiz?>>>"))
odam=[]
for ism in range(odam_soni):
    odam.append(input(f"{ism+1}-korgan odamizni ismi nima?>>>"))
print(odam)