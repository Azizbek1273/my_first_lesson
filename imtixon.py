"""1-masala. 6 xonali butun son yarating.
Sonning 4-indeksgacha bo’lgan raqamlarini ekranga chiqaring (2 bal)"""

# son = input("6 xonali son kiriting: ")
# print(son[:4])

"""2-masala. Sonlardan iborat tuple va bitta butun son berilgan. 
Berilgan son tuple ichida necha marta qatnashganini toping. (4 bal)"""

# sonlar = (1,2,3,4,5,6,7,8,9,10,10)
# natija = sonlar.count(10)
# print(natija)

"""3-masala. 3 ta son berilgan. Sonlarning nechtasi juft, 
nechtasi toq son ekanligini toping. Masalan, a=12, b=35, c=7 sonlarib berilgan bo’lsa, 
“1 ta juft, 2 ta toq” kabi natija chiqsin. (6 bal)"""

# a= 12
# b= 35
# c= 7
# if a % 2 ==0 and b % 2 ==0 and c % 2 ==0:
#     print()
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
# if a

"""4-masala. Input orqali kiritilgan matndagi'.'(nuqta) larni ','(vergul) larga 
almashtirib ekranga chiqaring. (3 bal)"""

# belgilar = input("Belgilarni kiriting: ")
# new = belgilar.replace("'.'","','")
# print(new)

"""5-masala. Foydalanuvchi butun son kiritsin. Sonning teskarisini chiqaring. 
(Masalana: 6068 -> 8606).(3 bal)"""

# a = input("Son kiriting:")
# print(a[::-1])

"""6-masala. Ismlardan iborat list berilgan. Listni alifbo tartibida tartiblang."""

# ismlar = ["Ali", "Vali", "Gani", "Akmal", "Bobur", "Shaxzoda"]
# ismlar.sort()
# print(ismlar)

"""7-masala. Berilgan 3 xonali songa teskari bo’lgan sonni yasab, uni ekranga chiqaring. 
Hech qanday stringga oid amal bajarmang! Masalan, 532 → 235 (6 bal)"""

# a = int(input("3 xonali son kiriting: "))
# birlik = a % 10
# onlik = (a // 10) % 10
# yuzlik = a // 100
# teskari = birlik * 100 + onlik * 10 + yuzlik
# print(teskari)

"""8-masala. {“ism”: “Islom”, “talaba”:True, “kurs”:2} kabi dictionary berilgan. 
Foydalanuvchidan key va value uchun 2 ta input oling. Kiritilgan key 
allaqachon bor bo’lsa, valuesini o’zgartirib qo’ying, 
aks holda yangi key-value sifatida qo’shing va natijani ekranga chiqaring. (5 bal)"""

# a = {
#     "ism": "Islom",
#     "Talaba": "True",
#     "Kurs": "2"
# }
# key = input("key kiriting: ")
# value = input("value kiriting: ")
# a[key] = value
# print(a)

"""9-masala. Input orqali son oling va uning nechchi xonali ekanligini aniqlang. 
Masalan, kiritilgan son 493945 bo’lsa, natija “6 xonali son” bo’lsin. (4 bal)"""

# a = input(" son kiriting: ")
# print(len(a), "xonali son")

"""10-masala. random orqali 1 dan 50 gacha bo’lgan sonlar orasidan bir tasodifiy 
butun son chiqaring va uning faktorialini hisoblang. (5 bal)"""

# import random
# import math
# sonlar = random.randint(1,50)
# print(sonlar)
# sonlar = math.factorial(sonlar)
# print(sonlar)

"""11-masala. Ismlardan iborat list va bitta alohida ism berilgan. 
Ism list ichida bor bo’lsa, “Allaqachon mavjud”, aks holda ismni listga qo’shing 
va “Ism ro’yxatga qo’shildi” natijasini print qiling. (5 bal)"""

# names = ["Ali", "Vali", "gani", "Azizbek"]
# name = input("Ism kiriting: ")
# if name in names:
#     print("Allaqachon mavjud")
# else:
#     names.append(name)
#     print("Ismlar ro'yhatga qo'shildi!")
# print(names)

"""12-masala. Sonlardan iborat list berilgan. Listdagi eng kichik va eng katta 
sonlarni hisobga olmasdan sonlarning o’rta arifmetigini hisoblang. (5 bal)"""
# numbers = [1,2,3,4,5,6,7,8,9]
# numbers.remove(min(numbers))
# numbers.remove(max(numbers))
# orta = sum(numbers) / len(numbers)
# print(orta)

"""13-masala. Foydalanuvchi vergul bilan ismlar kiritsin va ularni listga saqlang. 
Kiritilgan ismlardan eng uzun va eng kaltasini chiqaring. (5 bal)"""

"""14-masala. Bir dictionary oching va ichiga 3 ta element yozing. 
Uchchala elementning ham valuelari integer sonlar bo’lsin. 
Tuzilgan dictionaryning valuelarini kamayish tartibida chiqaring. (5 bal)"""

# lugat = {
#     "son": 123456789,
#     "son1": 234502478,
#     "son2": 23456499
# }
# qiymatlar = list(lugat.values())
# qiymatlar.sort(reverse=True)
#
# print(qiymatlar)


