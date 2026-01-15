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

# 7. 








