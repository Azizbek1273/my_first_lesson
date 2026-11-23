import math
# 16 ning kvadrat ildizi
# print(math.sqrt(16))

# 2 ning 3-darajasi  2 ** 3
# result = math.pow(2,3)
# print(result)

# result = math.factorial(5)
# print(result)

# Sonning modulini topish
# print(math.fabs(-24))

# Pi'ning asl qiymati
# print(math.pi)

# math.floor(x)dan kichik yoki teng butun sonni qaytaradi.
#
# print(math.floor(4.5)) # sonni pastga qarab yaxlitledi
# print(math.ceil(4.5))

# Topshiriq
"""Radiusni input orqali olib doiraning yuzini hisoblang. S = pi * r^2"""
#
# r = float(input("Radiusni kiriting: "))
# S = math.pi * math.pow(r,2)
# print(S)

"""Sonlar o’qida A va B nuqta berilgan ular orasidagi masofani aniqlang. """

# A = float(input("A nuqtani kiriting: "))
# B = float(input("B nuqtani kiriting: "))
#
# masofa = abs(A - B)
# print(masofa)

import random
# a va b oralig‘idagi (a ≤ x ≤ b) butun son.
# print(random.randint(1,9))

# a va b oralig‘idagi float tasodifiy son.

# print(random.uniform(0, 5)) # 1.5 va 5.5 orasidagi tasodifiy kasr son

# 0 va 1 oralig‘ida (0 ≤ x < 1) bo‘lgan tasodifiy son
# print(random.random())

# a va b oralig‘idagi (a ≤ x < b) butun son.

# print(random.randrange(1,10))

#Vazifa
# 1-masala
"""math modulidan foydalanib, sonning ildizini hisoblang."""
# import math
#
# A = float(input("sonni kiriting: "))
# ildiz = math.sqrt(A)
# print(ildiz)

# 2-masala
"""random modulidan foydalanib, 1 dan 10 gacha bo‘lgan tasodifiy son chiqaring."""
# import random
# print(random.randint(1,10))

# 3-masala
"""random yordamida 1 dan 50 gacha 2 ta son oling. Qaysi biri katta ekanini toping."""
# import random
# a = random.randint(1,50)
# b = random.randint(1,50)
# print(f"Birinchi son: {a}")
# print(f"Ikkinchi son: {b}")

# 4-masala
"""3 ta son kiritilsin. Ularning o‘rtacha qiymatini toping."""
# a = random.randint(1,5)
# b = random.randint(1,5)
# c = random.randint(1,5)
# natija = (a + b + c) / 3
# print(natija)

# 5-masala
# """Foydalanuvchidan doira radiusini so'rang.
# Doira uzunligi va yuzasini hisoblab, natijani chiqaring.
# S = π * r^2    |    L = 2 * π * r"""
# import math
# r = float(input("Doira radusni kiriting: "))
# S = math.pi * math.pow(r, 2)
# L = 2 * math.pi * r
# print(f"Doira yuzasi {S} ga teng va uzunligi {L} ga teng")

# 6-masala
"""Foydalanuvchidan yoshini so’rang va tug’ilgan yilini chiqaruvchi dastur tuzing."""
# yosh = int(input("Yoshingizni kiriting: "))
# print(2026 - yosh)

# 7-masala
"""1 - 9 oraliqda tasodifiy butun son oling va uning factorialini hisoblang."""
# import random
# import math
# a = random.randint(1,9)
# b = math.factorial(a)
# print(b)

# 8-masala
# import math
# a = float(input("a ni kiriting: "))
# b = float(input("b ni kiriting: "))
# c = math.sqrt(math.pow(a,2) + math.pow(b,2))
# print(c)

# import math
# print(math.floor(4))
