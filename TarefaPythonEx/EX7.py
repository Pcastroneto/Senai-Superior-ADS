x = 17
y = 3.2

result1 = x / 4 + y
print("a) x / 4 + y =", result1)

result2 = x * y ** 6
print("b) x * y ** 6 =", result2)

result1 = x % 4
result2 = int(y * 10) // 4
result = (result1, result2)
print("c) (x % 4) , (((int) y * 10) // 4) =", result)

result = (x / 6 // x / 3) + 4
print("d) (x / 6 // x / 3) + 4 =", result)
