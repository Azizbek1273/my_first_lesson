#   Set & Dictionary

# myset = set()
# print(type(myset))
# fruits = {"apple", "banana", "cherry"}
# print(fruits)

# numbers = [1,2,3,4,5,6,7,8,9]
# new_numbers =set(numbers)
# print(new_numbers)

# letters = set("Jamshidbek")
# letters2 = list["Jamshidbek"]
# letters3 = tuple("Jamshidbek")
# print(letters)
# print(letters2)
# print(letters3)

# numbers = {1,2,3,4,5,6,7,8,9}
# number2 = numbers.copy()
# print(number2)
# numbers.add("Aa")
# numbers.update("Bb","Cc")
# numbers.remove(2)
# numbers.discard(1)
# numbers.pop()
# numbers.copy()
# #numbers.clear()
# print(numbers)

# numbers = {1,2,3,4,5,6,7,8,9}
# numbers2 = {10,20,30,40,50,60,70,80,90}
# print(numbers | numbers2)
# print(numbers.union(numbers2))
# # print(len(numbers))

"""& = intersection= kesishma"""
# numbers = {1,2,3,4,5,6,7,8,9}
# numbers2 = {10,20,30,40,50,60,70,80,90,8,9}
# print(numbers & numbers2)
# print(numbers.intersection(numbers2))

# Farq Difference
# a = {1,2,3,4,5,6,7,8,9}
# b = {10,20,30,40,50,60,70,80,90,8,9}
# print(a - b)
# print(a.difference(b))

# Simmetrik farq (Symmetric Difference)--> kesishmani olmaydi xolos
# a = {1,2,3,4,5,6,7,8,9}
# b = {10,20,30,40,50,60,70,80,90,8,9}
# print(a ^ b)
# print(a.symmetric_difference(b))

"""a to‘plamidagi barcha elementlarni b da bo'lsa True qaytaradi"""
# a = {1,2,3,4,5,6,7,8,9}
# b = {10,20,30,40,50,60,70,80,90,8,9}
# print(a.issubset(b))
# print(b.issubset(a))

"""isdisjoint() — ikkita set (to‘plam) orasida umumiy elementlar mavjud 
yoki mavjud emasligini tekshiradi. agar umumiy elementi bo'lmasa True aks holda folse"""

# a = {1,2,3,4,5,6,7,8,9}
# b = {10,20,30,40,50,60,70,80,90}
# print(a.isdisjoint(b))

# Topshiriq
# 1-masala
# """Barcha o’quvchilar ro’yxatini toping"""
# backend = {"Azizbek", "Axror", "MuhammadQodir", "Foziljon"}
# frontend = {"Anvar", "Gani", "Vali", "Azizbek"}
# print(backend.union(frontend))
# print(backend | frontend)
# """ham backend, ham frontend kursida o’qiydigan o’quvchilarni toping"""
# print(backend & frontend)
# print(backend.intersection(frontend))
# """faqat backend kursida o’qiydigan o’quvchilarni toping"""
# print(backend - frontend)
# print(backend.difference(frontend))
# """faqat bitta kursda o’qidigan o’quvchilarni ro’yxatini chiqaring"""
# print(backend ^ frontend)
# print(backend.symmetric_difference(frontend))

# 2-masala
"""Sizning va qo’shningizning uyingizda ko’plab mevalar bor. 
Ularni ikki set to’plami orqali ifodalang va quyidagi topshiriqlarni bajaring"""

"""Jami necha turdagi mevalar mavjud?"""
# a = {"Olma", "Anor", "Nok", "Banan", "Bexi"}
# b = {"Olma", "Anor", "Apelsin", "Shaftoli"}
# print(a | b)
# print(len(a | b))

"""sizda ham, qo’shnigizda ham mavjud bo’lgan mevalar qaysi?"""

# a = {"Olma", "Anor", "Nok", "Banan", "Bexi"}
# b = {"Olma", "Anor", "Apelsin", "Shaftoli"}
# print(a & b)
# print(a.intersection(b))

"""faqat sizda bor, qo’shingizda bo’lmagan mevalar qaysi?"""

# a = {"Olma", "Anor", "Nok", "Banan", "Bexi"}
# b = {"Olma", "Anor", "Apelsin", "Shaftoli"}
# print(a - b)
# print(a.difference(b))

"""faqat qo’shningizda bor, sizda yo’q bo’lgan mevalar qaysi?"""

# a = {"Olma", "Anor", "Nok", "Banan", "Bexi"}
# b = {"Olma", "Anor", "Apelsin", "Shaftoli"}
# print(b - a)

# Dictionary
capitals = {
    "Germanya" : "Berlin",
    "Canada" : "Ottava",
    "England" : "London",
    "Uzbekistan" : "Tashkent"
}
print(capitals)
