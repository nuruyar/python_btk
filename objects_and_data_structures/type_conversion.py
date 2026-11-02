x = input('1.sayı: ')
y = input('2.sayı: ')

toplam = int(x) + int(y) #bu dönüşüm yapılmazsa, inputtan gelen değerleri string olarak alır ve string olarak yan yana yazar.
print(toplam) 

z = 5
t = 2.5
name = "Çınar"
isOnline = True

print(type(z))
print(type(t))
print(type(name)) 
print(type(isOnline)) #tür kontrolü için

#int to float
z = float(z)
print(z)
print(type(z))

#float to int
t = int(t)
print(t)
print(type(t))

result = z + t
print(result)
print(type(result))

##bool to int
isOnline = int(isOnline)
print(isOnline)
print(type(isOnline))

##bool to string
isOnline = str(isOnline)
print(isOnline)
print(type(isOnline))

