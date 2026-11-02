x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?

sayi1 = int(input('1. sayi: '))
sayi2 = int(input('2. sayi: '))
toplam = x + y + z
print((sayi1 * sayi2) - toplam)

# 2- y'nin x'e kalansız bölümünü hesaplayınız.

result = y//x
print(result)

# 3- (x,y,z) toplamının mod3'ü nedir?

result = toplam % 3
print(result)

# 4- y'nin x. kuvvetini hesaplayınız.

result = y**x
print(result)

# 5- x, *y, z = numbers işlemine göre z'nin kübü kaçtır?

x, *y, z = numbers
print(z**3)

# 6- x, *y, z = numbers işlemine göre y'nin değerleri toplamı kaçtır?

result = y[0] + y[1] + y[2]
print(result)
