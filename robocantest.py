# 1-masala
"""
Ikkita butun son A va B ning yig'indisini hisoblang
"""
# a = int(input())
# b = int(input())
# print(a + b)

# 2-masala
"""Dasturchilar kuni yilning 255-kunida nishonlanadi(bunda 1 - yanvar 
nolinchi kun deb hisoblanadi). Berilgan yildagi dasturchilar kuni 
sanasini aniqlaydigan dastur yozishingiz kerak.
Grigorian taqvimida kabisa yili hisoblanadi:
yil raqami 400 ga bo'linadigan yil
yil raqami 4 ga bo'linadigan, ammo, 100 ga bo'linmaydigan yil"""

# yil = int(input())
# if yil % 400 == 0 or (yil % 4 == 0 and yil % 100 != 0):
#     kun = 12
# else:
#     kun = 13
#
# print(f"{kun:02d}/09/{yil:04d}")

# 3-masala
#Minimum va maksimum yig'indi
"""Beshta musbat butun son berilgan, ulardan to'rttasini ajratib olinganda 
umumiy yig'indisi bo'lishi mumkin bo'lgan minimum qiymat va maksimum qiymatni aniqlang.

"""
# sonlar = list(map(int, input().split()))
# jami = sum(sonlar)
# eng_kichik = jami - max(sonlar)
# eng_katta = jami - min(sonlar)
#
# print(eng_kichik, eng_katta)

"""4-masala. Oxirgi raqamni topish"""
# M011C
# raqam = int(input())
# a = raqam % 10
# print(a)

"""5-masala. Sizga butun sonlar to'plami berilgan. To'plamda 
1 ta elementdan tashqari barchasini jufti bor. 
To'plamdagi yagona jufti bo'lmagan yolg'iz sonni toping.
Masalan: 
[1,2,3,4,3,2,1] to'plamida yolg'iz son 4 sonidir."""

# toplam = [1,2,3,4,3,2,1]
# son = 0
# for i in toplam:
#     son = son ^ i
# print(son)

"""Sonni kvadratni topish"""
# def kvadrat(a):
#     return a ** 2
# n = int(input())
# print(kvadrat(n))
