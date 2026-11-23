# float -> int
# num = str(65.5)
# print(type(num))

# temperature = str(36.6)
# print(temperature)
# xato
# first_name = int(input("Ismingizni kiriting: "))
# print(type(first_name))

# 3 ta soni o'rta arifmtigini topish

# num1 = int(input("Birinchi soni kiriting: "))
# num2 = int(input("Ikkinchi soni kiriting: "))
# num3 = int(input("Uchinchi soni kiriting: "))
#
# natija = (num1 + num2 + num3)/3
# print(f"Sonlarni o'rta arifmetigi: {natija:.1f}")

# a va b tomonli to’g’ri to’rtburchak mavjud. Uning perimetrini toping. P = 2 * ( a + b )
#
# a = 4
# b = 5
# P = 2 * (a + b)
# print("To'g'ri to'rtburchak perimetri", P, " ga teng")

# a = float(input(" a tomoni kiriting: "))
# b = float(input(" b tomoni kiriting"))
# P = 2 * (a + b)
# print(f"To'rtburchak parametri {P} ga teng")

"""Foydalanuvchidan daqiqalar sonini kiritishni so'rang.
 Kiritilgan daqiqalarni soat va daqiqalarga ajratib chiqaring.
  Masalan: 140 daqiqa = 2 soat 20 daqiqa"""

# time = int(input("Daqiqani kiriting: "))
# soat = time // 60
# minut = time % 60
# print(soat,"soat",minut,"minut")

"""
Foydalanuvchidan 3 xonali son kiritishni so'rang. Kiritilgan sonning yuzliklar,
o'nliklar va birliklar xonasidagi raqamlarni alohida-alohida chiqaring.
"""
# son = int(input("Uch xonali soni kiriting: "))
# yuzlik = son //100
# onlik = (son % 100) // 10
# birlik = (son % 10)
# print("\n",yuzlik,"\n",onlik,"\n",birlik)

# "\n" --> yangi qatorga tushirar ekan

# a, b, c, d =1, 2, 3, 4
# print(max(a, b, c, d))

# print(min(23, 43, 21, 34))

#  Vazifa

""" 1)Foydalanuvchidan tug'ilgan yilini so'rang va uning yoshini hisoblab chiqaring."""
# from datetime import datetime
# tugulgan_yil = int(input("Tug'ulgan yilingizni kiriting: "))
#
# hozirgi_yil = datetime.now().year
#
# yosh = hozirgi_yil - tugulgan_yil
# print(f"sizning yoshingiz {yosh} da")

# 2-masala
"""kkita son kiritishni so'rang va ularning o'rta arifmetigini hisoblang."""
# num1 = int(input("Birinchi soni kiriting: "))
# num2 = int(input("Ikkinchi soni kiriting: "))
#
# natija = (num1 + num2) / 2
# print(natija)

# 3-masala
"""Foydalanuvchidan uchburchakning uchta tomonini kiritishni so'rang
 va uning perimetrini hisoblang."""

# a = int(input("a tomoni kiriting: "))
# b = int(input("b tomoni kiriting: "))
# c = int(input("c tomoni kiriting: "))
# P = a + b + c
# print(f"Uchburchak tomoni {P} ga teng")

# 4-masala
"""4. Foydalanuvchidan dollar( $ ) miqdorini so'rang va uni so'mga aylantiring.
Misol uchun kurs: 1 USD = 12 950 UZS."""

# dollar = float(input("Dollar miqdorini kiriting: "))
# kurs = 12950
# som = dollar * kurs
# print(f"So'mdagi qiymati: {som} uzs ga teng")

# 5-masala
"""
5. Foydalanuvchidan 3 xonali son oling va sonning eng kichik xona raqamini chiqaring.  
Misol uchun: 926 → 2,   761 → 1
"""
# sonlar = int(input("uch xonali son kiriting: "))
#
# birlik = sonlar % 10
# onlik = (sonlar % 100) // 10
# yuzlik = sonlar // 100
#
# kichik = min(birlik, onlik, yuzlik)
# print(kichik)

# 6-masala
"""
6. To'g'ri to'rtburchakning tomonlarini kiritishni so'rang
 va uning yuzasi va perimetrini hisoblang.  
    S = a * b   |    P = 2 * ( a + b)
# """
# a = int(input("a tomoni kiriting: "))
# b = int(input("b tomoni kiriting: "))
# s = a * b
# P = 2 * (a + b)
# print(f"To'rtburchakning yuzi S: {s} \n perimetri {P}")

# 7-masala
"""Foydalanuvchidan son kiritishni so'rang va uning kvadratini, kubini hisoblang."""

# son = int(input("Sonni kiriting: "))
# kvadrat = son ** 2    #kvadrat = son * son
# kub = son ** 3
# print(f"Soning kvadrat {kvadrat} ga teng, Soning kubi {kub} ga teng")

# 8-masala
"""
Ikkita son kiritishni so'rang
va ularning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaring.
"""
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# yegindi = a + b
# ayirma = a - b
# kopaytma = a * b
# bolinma = a / b
# print(yegindi, ayirma, kopaytma, bolinma)

# 9-masala
"""
Foydalanuvchidan Selsiy gradusini so'rang
 va uni Farangeytga o'tkazing. F = 1.8 * C + 32"""
# gradus = float(input("Selsiy gradusni kiriting: "))
# C = gradus
# F = 1.8 * C + 32
# print(F)

# 10-masala
"""Foydalanuvchidan 3 xonali son kiritishni so'rang
 va uning raqamlar yig'indisini hisoblang."""
# a = int(input("Uch xonali sonni kiriting: "))
# yuzlik = a // 100
# onlik = (a % 100) // 10
# birlik = a % 10
# yegindi = (yuzlik + onlik + birlik)
# print(yegindi)

# 11-masala
"""
a va b o’zgaruvchilarni e’lon qiling.
a ning qiymati b ga - b ning qiymati a ga o’zgarsin.
# """
# a = int(input("a= "))
# b = int(input("b= "))
# a, b = b, a
# print(f"a = {a}, b = {b}")

import math

r = float(input("Radusni kiriting: "))
R = math.pi * math.pow(r, 2)
print(R)


