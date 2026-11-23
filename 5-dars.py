"""Shart operatori: if .. elif .. else"""

# age = int(input("Yoshingizni kiriting: "))
# if age > 18:
#     print("Pasport olishingiz mumkin")
# elif age < 18:
#     print("Pasport olish mumkin emas")
# else :
#     print("Siz O'zbekiston fuqorosi emasiz")

# a = 10
# b = 20
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")

#    Topshiriq
# a = 3
# b = 5
# if a == b:
#     print("Ikkalasi teng")
# elif a > b:
#     print("a katta")
# else :
#     print("b katta")

# a = 5
# b = 6
# if a != b:
#     print("Ikkala son bir birga teng emas")
# elif a >= b:
#     print("kichik yoki teng")
# else:
#     print("katta yoki teng")

# x = 10
# y = 10
# if x > y:
#     print("x katta y dan")
# elif x < y:
#     print("x kichik y dan")
# else :
#     print("x va y teng")

# age = int(input("Yoshingizni kiriting: "))
# if age < 7:
#     print("SIz boqchaga borasiz")
# elif age >= 7 and age <=18:
#     print("Siz maktabga borasiz")
# elif age > 18:
#     print("Siz voyaga yetgansiz")

# Topshiriq

#1. Foydalanuvchidan uning yoshini so'rang va quyidagi shartlarga ko'ra javob qaytaring:
    # - Agar yoshi 12 dan kichik bo'lsa "Siz hali bolasiz" deb chiqaring
    # - Agar yoshi 13-18 orasida bo'lsa "Siz yoshsiz" deb chiqaring
    # - Agar yoshi 18-25 orasida bo’lsa “O’rta yoshlisiz” deb chiqaring
    # - Agar yoshi 26 dan katta bo'lsa "Ulg’ayibsiz" deb chiqaring

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh < 12:
#     print("Siz hali bolasiz")
# elif yosh >=13 and yosh <=18:
#     print("Siz yoshsiz")
# elif yosh >=19 and yosh <=25:
#     print("Siz o'rta yoshlisiz")
# else:
#     print("Ulg'ayibsiz")

"""2. Foydalanuvchidan son kiritishini so'rang. Agar son musbat bo'lsa 
"Musbat son", manfiy bo'lsa "Manfiy son", nolga teng bo'lsa "Nol" deb chiqaring."""

# son = int(input("Son kiriting: "))
# if son > 0:
#     print("Son musbat")
# elif son < 0:
#     print("son manfiy")
# else:
#     print("Nol")
#
# age = int(input("Yoshingizni kiriting: "))
# if age >= 18:
#     print("Siz ovoz berishingiz mumkin")
# else:
#     print("Kechirasiz siz hali ovoz berish yoshiga yetmagansiz")

#    Topshiriq
"""Foydalanuvchidan ikkita son kiritishini so'rang. 
Agar birinchi son ikkinchisidan katta bo'lsa "Birinchi son katta", aks holda 
"Ikkinchi son katta" deb chiqaring. 
sonlar teng bo'lsa "Sonlar teng" deb chiqaring."""

# a = int(input("Birrinchi soni kiriting: "))
# b = int(input("Ikkinchi soni kiriting: "))
# if a > b:
#     print("Birrinchi son katta")
# elif a < b:
#     print("Ikkinchi son katta")
# else:
#     print("Ikkala son teng")

"""Foydalanuvchidan hafta kunini raqam ko'rinishida kiritishini so'rang (1-7). 
Kiritilgan raqamga mos kunni chiqaring. 
Masalan, 1 - "Dushanba", 2 - "Seshanba" va hokazo. 
Agar 1-7 oralig'ida bo'lmagan son kiritilsa 
"Noto’g’ri hafta kuni kitildi" deb chiqaring."""

# kun = int(input("Hafta kunini kiriting: "))
# if kun == 1:
#     print("Dushanba")
# elif kun == 2:
#     print("Seshanba")
# elif kun == 3:
#     print("Chorshanba")
# elif kun == 4:
#     print("Payshanba")
# elif kun == 5:
#     print("Juma")
# elif kun == 6:
#     print("shanba")
# elif kun == 7:
#     print("Yakshanba")
# else:
#     print("Bunday hafta mavjud emas")

"""If with Booleans"""
# is_merried = False
# is_merried = True
# if is_merried:
#     print("Uylangan")
# else:
#     print("Uylanmagan")

# Topshiriq
"""confirmed nomli boolean o’zgaruvchi e’lon qiling. Agar qiymat True bo’lsa 
“Arizangiz qabul qilindi”, False bo’lsa “Arizangiz bekor qilindi” kabi chiqaring."""

# confirmed = False
# if confirmed:
#     print("Arizangiz qabul qilindi!")
# else:
#     print("Arizangiz bekor qilindi!")

#  Logical Operators
# and, or, not
# age = int(input("Yoshingizni kiriting: "))
# nation = input("Milatingizni kiriting: ").capitalize()
# if age >=18 and nation in "O'zbek":
#     print("Ovoz berishingiz mumkin")
# else:
#     print("Ovoz berishingiz mumkin emas")

# salary = float(input("Oylik daromadingizni kiriting: "))
# age = int(input("Yoshingizni kiriting: "))
# if salary >= 300  and age >= 21:
#     print("Kridit olishingiz mumkin")
# else:
#     print("Kridit olishingiz mumkin emas")<

# age = int(input("Yoshingizni kiriting: "))
# if age <= 7 or  70 <= age:
#     print("Yo'l haqi bepul")
# else:
#     print("Yo'l haqi 3 000 so'm")


# age = int(input("Yoshingizni kiriting: "))
# if not age >= 18:
#     print("Voyagq yetgansiz")
# else:
#     print("voyaga yetmagansiz")

# sunny = False
# if not sunny:
# 		print("Havo salqin!")

# Topshiriq
"""Foydalanuvchidan ob-havo va temperaturani qabul qilib oling. 
Agar ob-havo “quyoshli” va temperatura 30 dan yuqori bo’lsa 
- “Bugun cho’milishli havo”, aks holda “Bugun cho’mila olmaymiz” kabi matn chiqsin!"""

# ob_havo = input("Ob havoni kiriting: ")
# temperatura = float(input("Temperaturani kiriting: "))
# if temperatura > 30 and  ob_havo == "Quyoshli":
#     print("Bugun cho'milish mumkin")
# else :
#     print("Bugun cho'milish mumkin emas")

"""in - elementning biror to'plamda, ro'yxatda yoki string( satr )da 
mavjudligini tekshiradi. 
Agar element mavjud bo'lsa, True, aks holda False qaytaradi."""

# if "o" in "Python":
#     print("Mavjud")
# else:
#     print("No")

# Topshiriq
"""- Topshiriq
1.Foydalanuvchidan baholarini so'rang va quyidagi shartlarni tekshiring:
        - Agar baholar 60 dan yuqori bo'lsa, "Siz imtihondan o'tdingiz!" deb yozing.
        - Agar baholar 85 dan yuqori bo'lsa, "Siz a'lo baho oldingiz!" deb qo'shing."""
#
# baxo = int(input("Baxolaringizni kiriting: "))
# if baxo > 60:
#     print("Siz imtixondan o'tdingiz")
#     if baxo > 85:
#         print("Siz a'lo baho oldingiz")

# Vazifa
"""Foydalanuvchidan butun son input olib, 
toq yoki juft ekanligini aniqlovchi dastur tuzing."""

#    1-masala
# son = int(input("Sonni kiriting: "))
# if son % 2 ==0:
#     print("Son juft")
# else:
#     print("To'q")

#    2-masala
"""Temperaturani input qilib oling va qiymati 36.6 dan katta bo’lsa ham, 
kichik bo’lsa ham “Tana haroratingiz normal emas” deb chiqaring."""

# harorat = float(input("haroratni kiritib oling: "))
# if harorat > 36.6:
#     print("haroratingiz normal emas")
# elif harorat == 36.6:
#     print("haroratingiz normal")
# else:
#     print("haroratingiz normal emas")

# 3-masala
"""Foydalanuvchidan 3 ta son qabul qiling. 
Ularning eng kichigini topib beruvchi dastur tuzing."""
#
# a= float(input("a=sonini kiriting: "))
# b= float(input("b=sonini kiriting: "))
# c= float(input("c=sonini kiriting: "))
#
# if a > b and a > c:
#     print("a=soni katta")
# elif b > a and b > c:
#     print("b=soni katta")
# else:
#     print("c=soni katta")

# 6-masala
"""Imtihon balini input qilib oluvchi va 
quyidagicha oraliqda ballarni baholab beradigan dastur tuzing:"""

# ball = int(input("Balingizni kiriting: "))
# if 86 <= ball <= 100 :
#     print("5 baxo")
# elif 72 <= ball <= 85 :
#     print("4 baxo")
# elif 56 <= ball <= 71 :
#     print("3 baxo")
# elif 32 <= ball <= 55 :
#     print("2 baxo")
# elif 0 <= ball <= 31 :
# #else :
#     print("1 baxo")

# 8-masala
# topa olmadim

# 9-masala
"""Foydalanuvchidan yilni kiritishini so'rang. 
Agar kiritilgan yil kabisa yili bo'lsa "Kabisa yili" deb chiqaring, 
aks holda "Kabisa yili emas" deb chiqaring. 
(Eslatma: Kabisa yili 4 ga qoldiqsiz bo'linadigan yillar, 
lekin 100 ga bo'linadigan yillar orasidan faqat 
400 ga qoldiqsiz bo'linadiganlari kabisa yili hisoblanadi."""

# yil = int(input("Yilni kiriting: "))
# if yil % 4 == 0:

#10-masala
"""Foydalanuvchidan uchta son kiritishini so'rang. 
Agar bu sonlar uchburchakning tomonlari bo'la olsa, 
"Uchburchak yasash mumkin" deb chiqaring. Aks holda, 
"Uchburchak yasab bo'lmaydi" deb xabar bering. 
Eslatma: Uchburchak yasash uchun har qanday ikki tomonning yig'indisi 
uchinchi tomondan katta bo'lishi kerak."""

# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
#
# if a + b > c and a + c > b and b + c > a:
#     print("Uchburchak yasash mumkin")
# else:
#     print("Uchburchak yasash mumkin emas")

# 11-masala
"""Foydalanuvchidan biror oyning raqamini (1-12) kiritishini so'rang. 
Kiritilgan raqamga mos oyning nomini va u oyda necha kun borligini chiqaring. 
Kabisa yilini hisobga olmang (ya'ni, fevral oyida 28 kun deb hisoblang)."""

# oy = int(input("Oy raqamini kiriting (1-12): "))
#
# if oy == 1:
#     print("Yanvar — 31 kun")
# elif oy == 2:
#     print("Fevral — 28 kun")
# elif oy == 3:
#     print("Mart — 31 kun")
# elif oy == 4:
#     print("Aprel — 30 kun")
# elif oy == 5:
#     print("May — 31 kun")
# elif oy == 6:
#     print("Iyun — 30 kun")
# elif oy == 7:
#     print("Iyul — 31 kun")
# elif oy == 8:
#     print("Avgust — 31 kun")
# elif oy == 9:
#     print("Sentabr — 30 kun")
# elif oy == 10:
#     print("Oktabr — 31 kun")
# elif oy == 11:
#     print("Noyabr — 30 kun")
# elif oy == 12:
#     print("Dekabr — 31 kun")
# else:
#     print("Noto'g'ri oy raqami! 1 dan 12 gacha son kiriting.")

# 12-masala
"""Foydalanuvchidan ikkita son va ular orasida bajariladigan arifmetik amal belgisini 
(+, -, *, /) kiritishini so'rang. Kiritilgan ma'lumotlarga qarab tegishli 
arifmetik amalni bajaring va natijani chiqaring. Agar noto'g'ri amal belgisi kiritilsa, 
"Noto'g'ri amal" deb ogohlantiring."""

# son1 = float(input("Birinchi sonni kiriting: "))
# amal = input("Arifmetik amalni kiriting (+, -, *, /): ")
# son2 = float(input("Ikkinchi sonni kiriting: "))
#
# if amal == "+":
#     print("Natija:", son1 + son2)
# elif amal == "-":
#     print("Natija:", son1 - son2)
#
# elif amal == "*":
#     print("Natija:", son1 * son2)
# elif amal == "/":
#     if son2 != 0:
#         print("Natija:", son1 / son2)
#     else:
#         print("Nolga bo'lish mumkin emas!")
# else:
#     print("Noto'g'ri amal")







