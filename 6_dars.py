ismlar=["Xasan"]
ismlar.insert(0,"Abror")
ismlar.append("Laziz")
print(f"Salom {ismlar[1]}, choyxonaga borasanmi?")
print(ismlar[0]+" bormidigan boldi.")
print(f"Borsang {ismlar[2]} bizni olib ketar ekan")
sonlar=[15,-12,8.75,7,5.6]
sonlar.remove(-12)
sonlar.append(8.88)
sonlar[0]=sonlar[0]+1000
del sonlar[4]
print(sonlar)
print(sonlar[1]+sonlar[3])
t_shaxarlar=["Xiva","Samarqand","Xorazim"]
z_shaxarlar=["Yaponiya","Rassiya","Xitoy"]
shaxar=t_shaxarlar.pop(1)
hujum=z_shaxarlar.pop(2)
print("Men agar otmishga qaysaam "+shaxar+"ga \nAmurtemur!")
print(f"{hujum}ga hujum qilma kuyasan degan bo'lar edim")
friends=[]
friends.append("Ali")
friends.append("Xasan")
friends.append("Ismo")
friends.append("Asad")
friends.append("Saman")
friends.append("Vali")
print(friends)
friends.remove("Ali")
friends.remove("Vali")
print(friends)
friends.append("Abror")
friends.insert(0,"Laziz")
friends.insert(2,"Abdushukur")
print(friends)
mehmonlar=[]
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(1))
print("\nKeladigan mehmaonlar: ", mehmonlar)