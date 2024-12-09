# @@@@@@@@@@@@@@@@@@@@@@@  PYTHON WHILE LOOPS  @@@@@@@@@@@@@@@@@
# Python has two primitive loop commands:
# while loops
# for loops


# Python For Loops

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)


# Looping Through a String

# for x in "banana":
#     print(x)

# The break Statement
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     fruits=[]+

# The continue Statement
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "apple":
#     continue
#   print(x)

# print(list(range(1,11)))


# The range() Function
# for x in range(6):
#   print(x)

# for x in range(2, 6):
#   print(x)

# for x in range(2, 30, 3):
#   print(x)

# Else in For Loop
# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# >>> Note: The else block will NOT be executed if the loop is stopped by a break statement <<<


# for x in range(6):
#   if x == 3:
#     break
#   print(x)
# else:
#   print("Finally finished!")


# Nested Loops
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for i in adj:
#   for j in fruits:
#     print(i, j)


# for i in range(1, 6):
#     for j in range(1, 6):
#         print(i,end='')
#     print()

# 11111
# 22222
# 33333
# 44444
# 55555


# The pass Statement
# for x in [0, 1, 2]:
#   if x == 0:
#       pass
# for i in range(1, 6):
#     for j in range(1, 6):
#         for k in range(1, 6):
#             print(i, j, k)

###############################################  PYTHON WHILE LOOPS    ##################################
# i = 5
# while i > 0:
#   print(i)
#   i -= 1

# !!!  Note: remember to increment i, or else the loop will continue forever.
# i = 1
# while i < 6:
#   print(i)

# The break Statement
# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1
# else:
#   print("i is no longer less than 6")

# The continue Statement
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)


# The else Statement
# i = 1
# while i < 6:
#   print(i)
#   i += 1


# @@@@@@@@@@@@@@@@@  Python If ... Else @@@@@@@@@@@@@@@@@@@@
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")

# ////////////////////  Indentation <<<<<<<<<<<<<<<<<<<<<
# a = 33
# b = 200
# if b > a:
# print("b is greater than a")

# if
# if
# if
# if
# if
# elif
# elif
# elif
# elif
# elif


# !!! Elif
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

# !!! ELSE
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# Short Hand If
# a = 2222
# b = 330
# if a > b: print("a is greater than b")

# Short Hand If ... Else
# a = 2
# b = 330
# print("A") if a > b else print("B")

# NOTE::This technique is known as Ternary Operators, or Conditional Expressions.
# a = 331
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

# And
# a = 200
# b = 33
# c = 500
# if a > b and c > a:
#   print("Both conditions are True")

# Or
# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")

# Not
# a = 33
# b = 200
# if not a > b:
#   print("a is NOT greater than b")

# Nested If
# x = 41
# if x > 10:
#   print("Above ten,")
#   if x > 20:
#     print("and also above 20!")
#   else:
#     print("but not above 20.")

# The pass Statement
# a = 33
# b = 200
#
# if b > a:
#   pass

# ====================================================================================================
#  Oddiy for loop bir qatorda

#
# for i in range(5): print(i, end=" ")

#  List Comprehension bilan
# squared = [x**2 for x in range(5)]

# Shart bilan List Comprehension
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)

# [print(f"Number: {x}") for x in range(3)]

# if-else sharti bilan qiymat tanlash
# Agar har bir element uchun shart tekshirib, qiymatni shartga qarab o'zgartirish kerak bo'lsa,
# if-elseni for loopdan oldin yozasiz.

# [expression_if_true if condition else expression_if_false for item in iterable]

# numbers = [1, 2, 3, 4, 5]
# result = ["even" if x % 2 == 0 else "odd" for x in numbers]
# print(result)


# if faqat filtrlash uchun ishlatilsa
# Agar elementlarni shart bo'yicha filtrlash kerak bo'lsa, faqat ifni ishlatib,
# elseni yozmaslik mumkin. Bu holda, if for loopdan keyin yoziladi.

# [expression for item in iterable if condition]

# numbers = [1, 2, 3, 4, 5]
# evens = [x for x in numbers if x % 2 == 0]
# print(evens)


# if-else va filtrlashni birlashtirish

# numbers = [1, 2, 3, 4, 5]
# result = [x**2 if x % 2 == 0 else x for x in numbers if x > 2]
# print(result)

#  Ko'p shartlar bilan ishlatish
# numbers = [1, 2, 3, 4, 5]
# result = ["small" if x < 3 else "medium" if x < 5 else "large" for x in numbers]
# print(result)

# !!!!  NOTE   !!!!!!!!!
# if-else faqat qiymat tanlash uchun ishlatiladi va for loopdan oldin joylashadi.
# Filtrlash uchun ishlatiladigan if for loopdan keyin yoziladi.
# Murakkab ishlovlar uchun oddiy for loop ishlatish yaxshiroq bo'lishi mumkin,
# chunki haddan tashqari uzun list comprehension kodni qiyinlashtiradi.


# !!! XATOLIK
# numbers = [1, 2, 3, 4, 5]
# result = [x for x in numbers if x % 2 == 0 else x * 2]

# Filtrlash va qiymat tanlashni ajratish:
# numbers = [1, 2, 3, 4, 5]
# result = [x * 2 for x in numbers if x % 2 != 0]
# print(result)

# 2. Bit darajasidagi operatorlar (&, |, ~, ^)
# Bu operatorlar butun sonlarning bitlari bilan ishlaydi.
#
# Operatorlar va ishlashi:
# & (AND): Ikkita sonning har bir bitiga mantiqiy AND amali bajaradi.
# | (OR): Ikkita sonning har bir bitiga mantiqiy OR amali bajaradi.
# ~ (NOT): Sonning bitlarini teskari qiladi.
# ^ (XOR): Ikkita sonning bitlari bir xil bo'lsa 0, farqli bo'lsa 1.


# x = 5  # 101 (2-lik sanoq tizimida)
# y = 3  # 011 (2-lik sanoq tizimida)
#
# print(x & y)  # 1 (001)
# print(x | y)  # 7 (111)
# print(~x)     # -6 (teskari bitlar)
# print(x ^ y)  # 6 (110)

# a = 5  # True (non-zero sonlar mantiqiy qiymatda True)
# b = 0  # False
#
# # Ba'zan mantiqiy operatorlar bilan bit operatorlarini birgalikda ishlatishingiz mumkin. '
# # Bunda natijalar turiga e')tibor berish kerak:
# print((a != 0) and (b != 0))  # False (mantiqiy operatorlar)
# print(a & b)  # 0 (bit operatorlar)

# Ma'lumot turi:
#
# and, or, not - faqat mantiqiy qiymatlar bilan ishlaydi.
# &, |, ~, ^ - faqat butun sonlar (integer) bilan ishlaydi.

# x = 5  # 101 (2-lik sanoq tizimida)
# y = 3  # 011 (2-lik sanoq tizimida)
#
# print(x & y)  # 1 (001)
# print(x | y)  # 7 (111)
# print(~x)     # -6 (teskari bitlar)
# print(x ^ y)  # 6 (110)
