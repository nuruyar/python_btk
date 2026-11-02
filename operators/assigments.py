# x = 5
# y = 10
# z = 20

x, y, z = 16, 10, 20
print(x, y, z)

x, y = y, x
print(x, y, z)

x = x + 5
print(x)
x += 5
print(x)
x -= 5
print(x)
x *= 5
print(x)
x /= 5
print(x)
x %= 5
print(x)
y //= 5 #bölmenin tam kısmını alır.
print(y)
y **= 5
print(y)
y *= z
print(y)

values = (1,2,3)
print(values)
print(type(values))

x, y, z = values
print(x, y, z)

values = (1,2,3,4,5)
x, y, *z = values #fazla olan tüm elemanlar yıldızlıya gider, * olmazsa hata.
print(x, y, z)
print(x, y, z[1])