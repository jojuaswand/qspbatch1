# # add +
# # print(1 + 2)
# print(1.5 + 2.5)
# print((1 + 2j) + (2 + 2j))
# # sub -
# # print(1 - 2)
# print(1.5 - 2.5)
# print((1 + 2j) - (2 + 2j))
# # div /
# # print(1 / 2)
# # print(1.5 / 2.5)
# print((1 + 2j) / (2 + 2j))
# print(2j / 2j)
# # mul *
# # print(1 * 2)
# # print(1.5 * 2.5)
# # print(1.0 * 2.0)
# print((1 + 2j) * (2 + 2j))
# print(2j * 2j)
# # floordiv //
# # print(1 // 2) #its giving us remainder value
# print(1.5 // 2.5)
# print((1 + 2j) // (2 + 2j)) TypeError: can't take floor of complex number.
# # modulus %
# # print(1 % 2) #its giving us coeficient value
# print(1.5 % 2.5) #its not giving directly the coeficient
# print(1+2j % 2+2j) TypeError: can't mod complex numbers.

b = True #1
c = False #0
print(b + c)
print(b - c)
# print(b / c) ZeroDivisionError: division by zero
print(c / b)
print(b * c)
# print(b // c) ZeroDivisionError: division by zero
print(c // b)
# print(b % c) ZeroDivisionError: division by zero
print(c % b)