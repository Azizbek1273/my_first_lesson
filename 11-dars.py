# mevalar = ["Olma", "Anor", "Nok", "Banan", "Kivi"]
# for i in mevalar:
#     print(i)

# soz = "My name is Azizbek"
# for harf in soz.split():
#     print(harf)

# for i in range(15):
#     print("Azizbek", end=" ")

#Topwiriq
"""1-masala. Shaharlar ro’yxatini yaratib, barcha ro’yxatlarni consolega chiqaring."""
from itertools import count

# cities = ["Dubay", "Manako", "Berlin", "Shvetsariya", "Istanbul"]
# for city in cities:
#     print(city)

"""2-masala. Ismingizdagi barcha harflarni alohida chiqaring."""
# ism = "Azizbek"
# for i in ism:
#     print(i)
"""3-masala. Sonlardan iborat to’plamdagi barcha sonlar yig’indisi toping."""
# sonlar = [1,2,3,4,5,6,7,8,9,10]
# yegindi = 0
# for i in sonlar:
#     yegindi = yegindi + i
# print(yegindi)

# numbers = list(range(2,31,2))
# print(numbers)

# Topshiriq
"""1-masala. 5 marta ismingizni konsolga chiqaring."""

# for i in range(5):
#     print("Azizbek", end=" ")

"""2-masala. 1 dan 20 gacha bo’lgan toq sonlarni chiqaring."""
# for i in range(1,20,2):
#     print(i,end =" ")

"""3-masala. Foydalanuvchidan n butun sonini input oling. 
1 dan n gacha sonlarni yig’indisini toping."""
# n = int(input("n sonini kiriting: "))
# yegindi = 0
# for i in range(1, n + 1):
#     yegindi = yegindi + i
# print(yegindi)

"""4-masala. Kiritilgan sonning faktorialini topuvchi dastur tuzing."""
# n = int(input("n sonini kiriting: "))
# factorall = 1
# for i in range(1, n + 1):
#     factorall = factorall * i
# print(f"factorall: {factorall}")

#Break & Continue

# for i in range(1,11):
#     if i == 5:
#       break
#     print(i)

# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     print(i,end=" ")

# for i in range(1, 4 + 1):
#     print("Son:", i)
# else:
#     print("Sikl tugadi.")

# Topshiriq
"""1-masala. Son topish o’yinini yarating. random modulidan foydalaning."""

# for i in range(1,11):
#     for j in range(1,11+1):
#         print(i, j, sep=' ')

# mevalar = ["olma", "banan", "anor"]
#
# for index, meva in enumerate(mevalar, start=1):
#     print(index, meva)

#Vazifa
"""1-misol. Salom" so‘zini 5 marta chiqaruvchi for loop yozing."""
# for  i in range(5):
#     print("salom", end=" ")

"""2-misol. 1 dan 10 gacha bo‘lgan sonlarni ekranga chiqaruvchi for loop yozing."""
# for i in range(1,10):
#     print(i)

"""3-misol. 1 dan 20 gacha bo‘lgan juft sonlarni ekranga chiqaring."""
# for i in range(2,20,2):
#     print(i)

"""4-misol. 1 dan 100 gacha bo‘lgan sonlarning yig‘indisini hisoblang."""
# yigindi = 0
# for i in range(1,100):
#     yigindi = yigindi + i
# print(yigindi)

"""5-misol. "Python" so‘zidagi harflarni alohida chiqaring."""
# for i in "Python":
#     print(i)

"""6-misol. Ranglarni saqlovchi to’plam yarating va 
elementlarni birma-bir chiqaruvchi for loop yozing."""

# colors = ["Qizil", "Pushti", "Qora", "Yashil"]
# for i in colors:
#     print(i)

"""7-misol. 1 dan 10 gacha bo‘lgan sonlarning kvadratini ekranga chiqaring."""
# for i in range(1,10):
#     print(f"{i} ning kvadrati: {i ** 2}")

# for i in range(1,10):
#     kvadrat = i * i
#     print(i, "-", kvadrat)

"""8-misol. 1 dan 20 gacha bo‘lgan sonlar ichida 3 ga 
karrali sonlarni chiqaruvchi kod yozing."""

# for i in range(1,20):
#     if i % 3 == 0:
#         print(i)

"""9-misol. Sonlardan iborat ro’yxat yarating va 
barcha sonlarning ko‘paytmasini hisoblang."""

# sonlar = [1,2,3,4,5,6,7,8,9,10]
# kopaytma = 1
# for i in sonlar:
#     kopaytma = kopaytma * i
# print(kopaytma)

"""10-misol. Sonlardan iborat ro’yxat yarating va 
ro’yxatda nechta musbat son borligini aniqlang."""

# sonlar =[1,2,3,4,5,6,7,8,9,-2,-3]
# musbatson = 0
# for i in sonlar:
#     if i > 0:
#         musbatson += 1
# print(musbatson)

"""11-misol. Foydalanuvchidan 5 ta son kiritishni so‘rang 
va ularning yig‘indisini chiqaring."""

# yigindi = 0
# for i in range(1,6):
#     son = float(input("sonni kiriting: "))
#     yigindi += son
# print(yigindi)

"""12-misol. 10 dan 1 gacha bo‘lgan sonlarni 
(teskari tartibda: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 kabi) chiqaring."""

# for i in range(10, 1,-1):
#     print(i, end=" ")

"""13-misol. Foydalanuvchidan biror matn oling va undagi 
unli harflar sonini hisoblang."""

# matn = input("Matn kiriting: ").lower()
# unlilar = "aoeiu"
# harflar_soni = 0
# for i in matn:
#     if i in unlilar:
#         harflar_soni = harflar_soni + 1
# print(harflar_soni)

"""14-misol. Foydalanuvchidan biror so‘z oling 
va uni teskarisiga chiqaruvchi for loop yozing."""

# soz = input("sozni kiriting:")
# for i in reversed(soz):
#     print(i, end=" ")

"""15-misol. Rasmdagi ko’rinishda 2 dan 9 gacha bo’lgan 
ko’paytirish jadvalini consolega chiqaring:"""

for i in range(2,10):
    for j in range(2,10):
        print(f"{i}x{j}")





