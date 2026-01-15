#1. Sonlar ro‘yxati berilgan.
# `map()` va `lambda` yordamida har bir sonni 3 ga ko‘paytiring.

# l = [2, 6, 8, 6, 56, 21, 53, 57]

# k = list(map(lambda x: x * 3, l))
# print(k)

# 2. Sonlar ro‘yxatidan `map()` orqali
# har bir sonning kvadratini hisoblang.

# def kv(i):
#     return i * i
#
#
# l = [2, 6, 8, 6, 56, 21, 53, 57]
#
# k = list(map(kv, l))
# print(k)

# 3. Berilgan satrlar ro‘yxatida
# `map()` yordamida har bir satrni katta harflarga o‘tkazing.

# words = ["ziyoda", "salom", "toxir", "python"]
#
# text = list(map(str.upper, words))
# print(text)

# 4. Ismlar ro‘yxatidan `map()` orqali
# har bir ismning uzunligini hisoblang.

# names = ["Ziyoda", "Diyora", "Ibrohim", "Jasur"]
#
# n = list(map(len, names))
# print(n)

# 5. Sonlar ro‘yxatida `map()` yordamida
# manfiy sonlarni musbatga aylantiring (`abs` ishlatilmasin).
#
# l = [2, -6, 8, 6, -56, 21, -53, 57]
#
# musbat = list(map(lambda i: i * -1 if i < 0 else i, l))
#
# print(musbat)

# 6. Narxlar ro‘yxati berilgan.
# `map()` orqali har bir narxga 15% qo‘shilgan holatini hisoblang.

# prices = [4500, 6500, 10000, 7800, 1000]
#
# new_prices = list(map(lambda i: (i * 0.15) + i, prices))
#
# print(new_prices)

# 7. Sonlar ro‘yxatida `map()` yordamida
# juft sonlarni 0 ga, toq sonlarni esa o‘z holicha qoldiring.

# l = [1, 99, -6, 8, 9, 6, -56, 21, -53, 57]
#
# o = list(map(lambda i: i * 0 if i % 2 == 0 else i, l))
#
# print(o)

# 8. Satrlar ro‘yxatida `map()` orqali
# har bir satr oxiriga `!` belgisi qo‘shing.

# words = ["Ziyoda", "salom", "Toxir", "Python"]
#
# new_words = list(map(lambda x: x + "!", words))
#
# print(new_words)

# 9. Sonlar ro‘yxatidan `filter()` yordamida
# faqat juft sonlarni ajrating.

# def juft(num):
#     return num % 2 == 0


# l = [1, 2, 10, 99, -6, 8, 9, 6, -56, 21, -53, 57]
#
# new_l = list(filter(juft, l))
#
# print(new_l)

# 10.  Sonlar ro‘yxatidan
# 0 dan katta bo‘lgan sonlarni `filter()` bilan oling.

# def katta(num):
#     return num > 0
#
#
# l = [1, 2, -10, 99, -6, 8, 9, 6, -56, 21, -53, 57]
#
# l_katta = list(filter(katta, l))
#
# print(l_katta)

# 11. Satrlar ro‘yxatidan
# uzunligi 5 ta belgidan katta bo‘lgan so‘zlarni ajrating.

# def belgi(word):
#     return len(word) > 5
#
#
# words = ["ziyoda", "salom", "toxir", "python", "stol", "telefon"]
#
# new_w = list(filter(belgi, words))
#
# print(new_w)

# 12. Sonlar ro‘yxatidan `filter()` yordamida
# 5 ga bo‘linadigan sonlarni tanlab oling.


# def bolish(num):
#     return num % 5 == 0
#
#
# l = [1, 20, -10, 99, -6, 8, 9, 60, -56, 21, -50, 57]
#
# l1 = list(filter(bolish, l))
# print(l1)

# 13. Ismlar ro‘yxatidan
# `A` harfi bilan boshlanadigan ismlarni ajrating.

# names = ["Ziyoda", "Azim", "Diyora", "Abror", "Ibrohim", "Jasur", "Aziz"]
#
# a_names = list(filter(lambda name: name.startswith("A"), names))
#
# print(a_names)

# 14. Sonlar ro‘yxatidan
# manfiy bo‘lmagan (0 va musbat) sonlarni `filter()` bilan oling.

# l = [1, 20, -10, 99, -6, 8, 9, 60, -56, 21, -50, 57, 0]
#
# musbat = list(filter(lambda son: son >= 0, l))
#
# print(musbat)

# 15. Satrlar ro‘yxatidan
# ichida `python` so‘zi bor bo‘lgan satrlarni `filter()` orqali toping.

words = ["ziyoda", "python", "salom", "toxir", "python", "stol", "telefon", "python"]

p_w = list(filter(lambda word: "python" in word, words))

print(p_w)