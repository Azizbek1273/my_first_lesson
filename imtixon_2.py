"""1-masala. Foydalanuvchi ismi va yoshini kiritsin.
Siz string formattingni ishlatib foydalanuvchi haqidagi ma’lumotni ekranga chiqaring. """
from itertools import count

# ism = input("ismingizni kiriting: ")
# age = int(input("yoshingizni kiriting: "))
# print(f"Sizni ismingiz {ism}, va yoshingiz {age} da")

"""2-masala. 23 ni 5 ga bo’lgandagi qoldiqni chiqarib beruvchi dastur tuzing."""

# print(23 % 5)

"""3-masala. Foydalanuvchi input orqali kiritgan sonning kvadratini hisoblab ekranga 
chiqaradigan dastur tuzing"""

# son = float(input("Soni kiriting: "))
# kvadrat = son ** 2
# print(kvadrat)

# def kvadrat(a):
#     b = a ** 2
#     return b
# print(kvadrat(3))
# print(kvadrat(4))

"""4-masala. Foydalanuvchidan input orqali ism, familiyasini qabul qiling. 
Ularning birinchi harflarini katta, qolganlarini kichik harfga 
o’zgartirib ekranga chiqaring. """

# name = input("Please enter your name:").title()
# surname = input("Please enter your surname:").title()
# print(name,surname)

"""5-masala. Foydalanuvchi tug’ilgan yilini kiritsin. 
Siz foydalanuvchining yoshini hisoblab ekranga chiqaring."""

# born_year = int(input("Please enter your born year: "))
# a = 2026 - born_year
# print(a)

"""6-masala. Sonlardan iborat tuple yarating. for loopdan foydalanib 
tupledagi 3 ga qoldiqsiz bo’linadigan sonlarni ekranga chiqaring."""

# sonlar = (1,2,3,4,5,6,7,8,9,10)
# for i in sonlar:
#     if i % 3 == 0:
#         print(i)

"""7-masala. a va b o’zgaruvchilar berilgan. 
a ning qiymatini b ga, b ning qiymatini a ga o’zgartirib ekranga chiqaring. """
# a = 5
# b = 6
# a, b = b, a
# print(f"a={a}, b={b}")

"""8-masala. Funksiyaga argument sifatida bir son bering. 
Funksiyangiz sonning toq yoki juftligini aniqlasin."""

# def juft_toq(a):
#     if a % 2 == 0:
#         print("a soni juft")
#     else:
#         print("a soni toq")
# juft_toq(1)
# juft_toq(2)

"""9-mavzu. 3 ta integer son berilgan. 
Ularning nechtasi musbat, nechtasi manfiyligini aniqlab ekranga chiqaring."""

# a = [1,2,3,-1]
# musbat = 0
# manfiy = 0
# for i in a:
#     if i > 0:
#         musbat += 1
#     else:
#         manfiy += 1
# print(musbat)
# print(manfiy)

"""10-masala. 1 dan 100 gacha bo’lgan sonlarni ekranga chiqaring. 
5 ga bo’linadigan sonlar tashlab ketilsin."""

# for i in range(1, 100):
#     if i % 5 == 0:
#         continue
#     print(i)

"""11-masala. Random orqali 1 dan 50 gacha bo’lgan sonlar orasidan tasodifiy son oling. 
Sonning juft yoki toq ekanligini aniqlang. """

# import random
# son = random.randint(1, 50)
# print(f"tasodifiy son : {son}")
# if son % 2 == 0:
#     print(f"Juft son : {son}")
# else:
#     print(f"Bu son toq: {son}")

"""12-masala. Tuple yarating. for loop dan foydalanib tuple elementlarini 
teskari tartibda chiqaradigan dastur tuzing."""

# sonlar = (1,2,3,4,5,6,7,8,9,10)
# for i in reversed(sonlar):
#     print(i)

# sonlar = (1,2,3,4,5,6,7,8,9,10)
# for i in sonlar[::-1]:
#     print(i)

"""13-masala. Foydalanuvchi a va n sonlarini kiritsin. 
a dan n gacha bo’lgan sonlar yig’indisini chiqaring."""

# a = int(input("a ni kiriting: "))
# n = int(input("n ni kiriting: "))
# yegindi = 0
# for i in range(a,n+1):
#     yegindi += i
# print(yegindi)

"""14-masala. Bir dictionary oching va ichiga 3 ta element yozing. 
Uchchala elementning ham valuelari integer sonlar bo’lsin. 
Tuzilgan dictionaryning valuelarini sort qilib ekranga chiqaring."""

# lugat = {
#     "first":5,
#     "second":2,
#     "third":3,
# }
# qiymatlar = sorted(lugat.values())
# print(qiymatlar)

"""15-masala. Kod qanday natija chiqarishini yozing. 
Kompyuter va telefonda ishlatib ko’rish mumkin emas. """
# sonlar = [4, 36, 13, 61, 72]
# for son in sonlar:
# 	print(son)
# 	if son == 13:
# 			continue

"""16-masala. 2 savatda mevalar bor. Har bir savatni alohida to’plam deb oling 
va ikkala savatda ham bor mevalarni chiqaring. for yoki while loopdan foydalanmang. """
# a = {"olma", "Anor","Bexi"}
# b = {"Sabsi","kartoshka","piyoz"}
# print(a | b)

"""17-masala. Faqat ismlardan iborat list oching. Foydalanuvchidan ism so’rang, 
kiritilgan ism listda bor bo’lsa, “Siz ro’yxatda borsiz” degan yozuv, aks holda 
ismni listga qo’shib, ism listga qo’shilgani haqida ekranga xabar chiqaring. """

# names = ["Azizbek","Soyibjon","Oyatillo","Axror"]
# a = input("Ismingizni kiriting: ")
# if a in names:
#     print("Siz ro'yhatda borsiz!")
# else:
#     names.append(a)
#     print("ismingiz ro'yhatga qo'shildi")
#     print(names)

"""18-masala. Input orqali kiritilgan ismlarni vergul yoki 
bo’sh joy bilan ajratib oling. Kiritilgan ismlarni alifbo tartibda chiqaring."""

# matn = input("Ismlarni kiriting:(vergul yoki bow joy bn yozing): ")
# ismlar = matn.replace(" ", "").split()
# ismlar = [ism.capitalize() for ism in ismlar]
# print("Alifbo tartibida:")
# for ism in sorted(ismlar):
#     print(ism)

"""19-masala. Ushbu kod qanday natija chiqarishini yozing. 
Kompyuter yoki telefonda ishlatib ko’rish mumkin emas."""

# son = 0
# for x in range(5):
# 	print(son + 1)

"""20-masala. Foydalanuvchi bitta ikki xonali son kiritsin. 
Uning raqamlari o’rnini almashtirishdan hosil bo’ladigan sonni ekranga chiqaring. 
Masalan: 64 → 46"""

# son = int(input("Ikki xonali son kiriting: "))
# birlik =
# onlik =
