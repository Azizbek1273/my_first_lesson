# Topshiriq
"""first_name va last_name nomli ism
#  va familiyangizni saqlovchi o’zgaruvchilar yarating."""
# a = str(input(" first_name ni kiriting: "))
# b = str(input(" last_name ni kiriting: "))
# print(a,b)

# name = "Azizbek"
# print(name[1])
# print(len(name))
# print(name[-10::3])
# print(name[-3:-5:-1])

"""String Reversing— satrdagi belgilarni teskari tartibda chiqarish usuli. 
# Buning uchun slicing texnikasi va negativ qadam o‘lchovi (step) ishlatiladi."""
# text = "IT faqat hayvon emas"
# print(text[::-1])

# Topshiriq
"""1)Foydalanuvchidan ismini so'rang va quyidagi amallarni bajaring:"""
#1)ismning birinchi harfini chiqaring
#2)ismning oxirgi harfini chiqaring
#3)ismning 2 va 4-harflarini chiqaringi

# ism = str(input("Foydalanuvhi ismini kiriting: "))
# print(ism[0])
# print(ism[-1])
# print(ism[1])

"""2) Quyidagi matn berilgan: "Python dasturlash tili"""
#matndagi 'dasturlash' so'zini ajratib oling
#matndagi har ikkinchi harfni chiqaring
#matnni teskari tartibda chiqaring
# matn = "Python dasturlash tili"
# print(matn[7:17])
# print(matn[::2])
# print(matn[::-1])
#
"""3) Berilgan "programming" so'zining:"""
#dastlabki 3 ta harfini chiqaring
#oxirgi 4 ta harfini chiqaring
#o'rtadagi 'gram' qismini ajratib oling

# matn = "programming"
# print(matn[0:3])
# print(matn[:4])
# print(matn[3:7])

"""4. Foydalanuvchidan telefon raqamini kiriting (+998 XX XXX XX XX formatda). Undan:
    1)faqat raqamlarni ajratib oling (+ va bo'sh joylarni olib tashlang)
    2)oxirgi 4 raqamni chiqaring"""

# tel = str(input("Telefon raqamni kiriting: "))
# print(tel[1:])
# print(tel[-5:-1])


"""String Concatenation - bir nechta satrlarni birlashtirib, 
yangi satr yaratish jarayoni bo‘lib,
odatda operatori orqali amalga oshiriladi."""

# name = "Azizbek"
# familya = "Jo'raboyev"
# full_name = name + " " + familya
# print(full_name)

# 1) upper()
# text = "my name is Azizbek"
# text2 = "Azizbek"
# print(text.upper())
# print(text.lower())
# print(text.capitalize())
# print(text.title())
# print(text.find("o"))
# print(text.index("a"))
# print(text.count("z"))
# print(text.replace("Azizbek","Oyatillo"))
# print(text.strip())
# print(text2.isalpha())
# print(text2.isnumeric())
# print(text2.isdigit())

# Topshiriq
"""'8600 0804 1344 5555' karta raqamidagi bo’sh joylarni olib tashlang."""
# karta = "8600 0804 1344 5555"
# print(karta.replace(" ", ""))

""""Darsimiz tugadi vazifalarni keyingi darsgacha topshiring" - “keyingi”
 dan boshlab qirqib olib chiqaring.
 k ning indexsini methodlar yordamida aniqlang."""
# matn = "Darsimiz tugadi vazifalarni keyingi darsgacha topshiring"
# index = matn.find("keyingi")
# print(matn[index:])

# Vazifa
# 1) String ma’lumot turida 5 o’zgaruvchi e’lon qiling.
# ism = "Azizbek"
# familiya = "Jo'raboyev"
# shahar = "Farg'ona"
# kasb = "Dasturchi"
# til = "Python"
# print(ism)
# print(familiya)
# print(shahar)
# print(kasb)
# print(til)

# 2)O’zgaruvchi oching va qiymatiga quyidagi matnni ko’chirib yozing:
#     “String - matn ko’rinishidagi ma’lumot turi”
#1) satr uzunligini toping
# #2)  9-indeksdan oxirigacha bo’lgan qismini chiqaring
# a = "String - matn ko’rinishidagi ma’lumot turi"
# print(len(a))
# print(a[9:])

# 3) Ismingizni teskari holatda chiqaring.
# ism = "Azizbek"
# print(ism[::-1])

# 4) Foydalanuvchidan ism va familiyasini so’rab, u bilan salomlashadigan dastur tuzing.
# F-Stringdan foydalanin
# 4.1) ism va familiya qanday ko’rinishda
# kiritilsa ham - ularning faqat 1-harfi katta, qolgani kichik bo’lsin
#boshi va oxiridagi bo’sh joylar ham olib tashlansin

# ism = str(input("ismingizni kiriting: "))
# fam = str(input("Familyangizni kiriting: "))
# print(f"Assalomu aleykum {ism} {fam}")
# print(f"{ism.capitalize()} {fam.capitalize()}")
# print(f"{ism.strip()} {fam.strip()}")

# 5-masala. Foydalanuvchidan manzili so’ralsin.
# Kiritilgan manzilni barchasini katta harflarda chiqaring.
# manzil = str(input("manzilingizni kiriting: "))
# print(manzil.upper())

# 6-masala
"""Ixtiyoriy o’zgaruvchiga 3-4 so’zdan iborat qiymat bering. 
So’zlarning 1-harfini katta qolganlarini kichik holatda chiqaring."""

# a = "Hi my name is Adm"
# print(a.title())

# 7-masala
"""Foydalanuvchidan parol nomli input oling, 
uning faqat raqamlardan tashkil topgan yoki topmaganligini tekshiring."""

# parol = str(input("Parolni kiriting: "))
# print(parol.isdigit())
# print(parol.isnumeric())

# 8-masala--->chiqmadi
"""Foydalanuvchidan ismini input orqali oling.
 Ism ‘A’ harfidan boshlangan yoki yo’qligini string methodlaridan foydalanib aniqlang."""

# ism = str(input("Ismingizni kiriting: "))
# tekshirish = ism.isalpha()
# print(tekshirish)

# 9-masala
"""abc = ‘abcdefghijklmnopqrstuvxyz’ g harfidan t harfigacha kesib oling. 
Indexlarni o’zingiz kiritmang - harflar orqali aniqlang. """

# a = "abcdefghijklmnopqrstuvxyz"
# start = a.index("g")
# end = a.index("t")
# print(a[start:end])

# 10-masala--> chiqmadi
"""nums = '123456789' nums ichidan faqat juft sonlarni chiqaring."""
numbers = "123456789"
print(numbers[::-2])

# 11-masala --> ni ko'rsatishim kerak
"""“Yaponiya chiroyli mamlakat! Yaponiyada hamma baxtli yashaydi”. 
Matndagi “Yaponiya” o’rniga “O’zbekiston” nomini qo’yib chiqaring."""
#
# matn = "Yaponiya chiroyli mamlakat! Yaponiyada hamma baxtli yashaydi"
# print(matn.replace(" Yaponiya", "O'zbekiston"))

# matn2 = "Yaponiya chiroyli mamlakat! Yaponiyada hamma baxtli yashaydi"
# matn2 = matn2.replace("Yaponiya", "O'zbekiston")
# print(matn2)

# b = "Hello World"
# print(b.encode())
# print(b.center(15, "*"))